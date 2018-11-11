#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# **********************************************************
# * Author        : huangtao
# * Email         : 807250120@qq.com
# * Create time   : 2018/11/11 11:45 PM
# * Last modified : 2018/11/11 11:45 PM
# * Filename      : bilibili_article_spider.py
# * Description   : bilibili的最新文章
# **********************************************************

import time
import scrapy
import json
import re

class BilibiliArticleSpider(scrapy.Spider):
    name = "bilibili_article_spider"
    allowed_domains = ["bilibili.com"]

    def __init__(self, *args, **kwargs):
        super(BilibiliArticleSpider, self).__init__(*args, **kwargs)
        self.start_urls = ['https://www.bilibili.com/v/fashion/makeup/#/72003']

    def parse(self, response):
        content_data = re.findall(r'<script>window.__INITIAL_STATE__=(.*?)</script>', response.text)
        content_data = json.loads(content_data[0].replace(
            ';(function(){var s;(s=document.currentScript||document.scripts[document.scripts.length-1]).parentNode.removeChild(s);}());',
            ''))
        content_list = content_data.get('tagList')
        for content_ele in content_list:
            playnums = content_ele.get('stat').get('view')
            if playnums / 10000 >= 1:
                url = 'https://www.bilibili.com/video/av%s' % content_ele.get('aid')
                title = content_ele.get('title')
                picture_url = content_ele.get('pic')
                print picture_url
                print title
                print url
