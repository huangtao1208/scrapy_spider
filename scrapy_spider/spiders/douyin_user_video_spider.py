#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# **********************************************************
# * Author        : huangtao
# * Email         : huangtao@yimian.me
# * Create time   : 2018/4/17 下午8:09
# * Last modified : 2018/4/17 下午8:09
# * Filename      : douyin_user_video_spider.py
# * Description   : 抖音用户视频
# **********************************************************

import scrapy
from scrapy_spider.items import JianShuUserArticleItem
import json
from dateutil import parser
from scrapy.http import Request
import requests
from lxml import etree


class DouYinUserVideoSpider(scrapy.Spider):
    name = "douyin_user_video_spider"

    def __init__(self, *args, **kwargs):
        super(DouYinUserVideoSpider, self).__init__(*args, **kwargs)
        # 用户的喜欢数，可以使用下面的API，也可以使用https://www.douyin.com/aweme/v1/aweme/favorite/?user_id=70561933500&count=21
        #self.start_urls = ['https://aweme.snssdk.com/aweme/v1/aweme/favorite/?iid=30373511894&device_id=35781128184&os_api=18&app_name=aweme&channel=App%20Store&idfa=811A8841-030F-4AEA-B934-C2A56489C32D&device_platform=iphone&build_number=17805&vid=17CB0ACF-09CF-422B-9669-DE8FC0052C56&openudid=b2d5f585e9fd80f4dc494871aad41224c395f48b&device_type=iPhone7,2&app_version=1.7.8&version_code=1.7.8&os_version=11.2.5&screen_width=750&aid=1128&ac=WIFI&count=21&max_cursor=0&min_cursor=0&user_id=70561933500&mas=0036ad698700fec1a1f507f1d86551e80d66ba4c6fb23279fad4e8&as=a1653d4db8457a4b660858&ts=1524030296']
        #self.start_urls = ['https://www.douyin.com/aweme/v1/aweme/favorite/?user_id=2613650662&count=21']
        # 用户发布的视频
        # self.start_urls = ['https://aweme.snssdk.com/aweme/v1/aweme/post/?iid=30373511894&device_id=35781128184&os_api=18&app_name=aweme&channel=App%20Store&idfa=811A8841-030F-4AEA-B934-C2A56489C32D&device_platform=iphone&build_number=17805&vid=17CB0ACF-09CF-422B-9669-DE8FC0052C56&openudid=b2d5f585e9fd80f4dc494871aad41224c395f48b&device_type=iPhone7,2&app_version=1.7.8&version_code=1.7.8&os_version=11.2.5&screen_width=750&aid=1128&ac=WIFI&count=12&max_cursor=1524018155000&user_id=70561933500&mas=0097eee2efe5d6bdbdb7aec4fdef7fb288d66e9b949e1e9d7eca91&as=a1c56eada861eaf7560320&ts=1524033304']

        # 某个话题下的视频
        self.start_urls = ['https://www.douyin.com/aweme/v1/challenge/aweme/?ch_id=1574030716416014&count=40']
        # 'ch_id=1591906182997012'

    def parse(self, response):
        content_json = json.loads(response.body)
        aweme_list = content_json.get('aweme_list')
        print len(aweme_list)
        for aweme in aweme_list:
            print '================'
            print '标题：',aweme.get('desc')
            print '作者：',aweme.get('author').get('nickname')
            print '作者ID：',aweme.get('author_user_id')