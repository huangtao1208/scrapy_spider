#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# **********************************************************
# * Author        : huangtao
# * Create time   : 2018/4/17 下午8:09
# * Last modified : 2018/4/17 下午8:09
# * Filename      : jianshu_user_article_spider.py
# * Description   : 简书用户发布的文章
# **********************************************************

import scrapy
from scrapy_spider.items import JianShuUserArticleItem
import json
from dateutil import parser
from scrapy.http import Request
import requests
from lxml import etree

#简书作者最新文章
class JianShuUserArticleSpider(scrapy.Spider):
    name = "jianshu_user_article_spider"

    def __init__(self, *args, **kwargs):
        super(JianShuUserArticleSpider, self).__init__(*args, **kwargs)
        self.start_urls = ['https://www.jianshu.com/u/c34455009dd8']

    header_homepage = {
        'user-agent': "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36",
        'Host': 'www.jianshu.com',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Connection': 'keep-alive',
        'Accept-encoding': 'gzip, deflate, br',
        'Accept-language': 'zh-CN,zh;q=0.9',
        'Cache-Control': 'max-age=0',
        'Upgrade-Insecure-Requests': '1'
    }

    def start_requests(self):
        agent = "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36"
        for start_url in self.start_urls:
            response = requests.get(start_url,headers=self.header_homepage)
            ele = etree.HTML(response.text)
            id_url = ele.xpath('//div[@class="main-top"]/a[@class="btn btn-hollow"]/@href')[0]
            id_url = id_url.split('mail_to=')[-1]
            task_indeed_url = "https://www.jianshu.com/mobile/users/{}/public_notes?page=1&count=60&order_by=shared_at".format(id_url)
            header = {
                'user-agent': agent,
                'Host': 'www.jianshu.com',
                'Accept': 'application/json',
                'Proxy-Connection': 'keep-alive',
                'Accept-encoding': 'gzip, deflate',
                'Accept-language': 'zh-CN,zh;q=0.9',
            }
            yield Request(task_indeed_url, callback=self.parse, headers=header)

    # parse api
    def parse(self, response):
        content_list = json.loads(response.body)
        jianshu_user_article_item = JianShuUserArticleItem()
        for i in range(len(content_list)):
            url = content_list[i]['object']['data']['slug']
            url = 'http://www.jianshu.com/p/{}'.format(url)
            title = content_list[i]['object']['data']['title']
            picture_url = content_list[i]['object']['data']['list_image_url']
            day = content_list[i]['object']['data']['first_shared_at']
            day = day.replace('T',' ')[:19]
            info_time = parser.parse(day)

            jianshu_user_article_item['pictureUrls'] = picture_url
            jianshu_user_article_item['title'] = title
            jianshu_user_article_item['url'] = url
            jianshu_user_article_item['publishTime'] = info_time
            yield jianshu_user_article_item
