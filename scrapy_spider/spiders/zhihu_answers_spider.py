#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# **********************************************************
# * Author        : huangtao
# * Create time   : 2018/5/9 下午8:02
# * Last modified : 2018/5/9 下午8:02
# * Filename      : zhihu_answers_spider.py
# * Description   : 知乎问答
# **********************************************************

import datetime
import scrapy
from scrapy_spider.items import ZhihuAnswersItem
from scrapy.selector import Selector
import json


class ZhihuAnswersSpider(scrapy.Spider):
    name = "zhihu_answers_spider"

    headers = {
        'Host': 'www.zhihu.com',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36',
    }

    def __init__(self, *args, **kwargs):
        super(ZhihuAnswersSpider, self).__init__(*args, **kwargs)
        self.start_urls = ['https://www.zhihu.com/people/huangxiaoguai/answers']

    def parse(self, response):
        sel = Selector(response)
        zhihu_answers_item = ZhihuAnswersItem()
        answer_data = sel.xpath('//div[@id="data"]/@data-state').extract_first()
        try:
            answer_data = json.loads(answer_data)['entities']['answers']
        except Exception as e:
            answer_data = {}
        for k, v in answer_data.iteritems():
            publish_time = datetime.datetime.fromtimestamp(v['updatedTime'])
            title = v['question']['title']
            url = 'https://www.zhihu.com/question/%s/answer/%s' % (v['question']['url'].replace('http://www.zhihu.com/questions/', ''), \
                v['url'].replace('http://www.zhihu.com/answers/', ''))
            zhihu_answers_item['title'] = title
            zhihu_answers_item['url'] = url
            zhihu_answers_item['publishTime'] = publish_time

            print '====='
            print zhihu_answers_item['title']
            print zhihu_answers_item['url']
            print zhihu_answers_item['publishTime']

            #yield zhihu_answers_item