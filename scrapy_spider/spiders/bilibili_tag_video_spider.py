#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# **********************************************************
# * Author        : huangtao
# * Create time   : 2018/11/11 11:25 PM
# * Last modified : 2018/11/11 11:25 PM
# * Filename      : bilibili_tag_video_spider.py
# * Description   : 哔哩哔哩tab标签的视频，比如https://www.bilibili.com/tag/31971
# **********************************************************

import time
import scrapy
import json


class BilibiliTagVideoSpider(scrapy.Spider):
    name = "bilibili_tag_video_spider"
    allowed_domains = ["bilibili.com"]

    def __init__(self, *args, **kwargs):
        super(BilibiliTagVideoSpider, self).__init__(*args, **kwargs)
        self.start_urls = ['https://api.bilibili.com/x/web-interface/tag/top?jsonp=jsonp&pn=2&ps=20&tid=31971&callback=__jp0']

    def parse(self, response):
        content = json.loads(response.body)
        _vlist = content["data"]["archives"]
        _len = len(content["data"]["archives"])
        for x in range(_len):
            _title = _vlist[x]["title"]
            _url = 'https://www.bilibili.com/video/av' + str(_vlist[x]["aid"])
            _picture_url = _vlist[x]["pic"]
            _created = _vlist[x]["pubdate"]
            _time_str = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(_created))

            print _picture_url
            print _title
            print _url

