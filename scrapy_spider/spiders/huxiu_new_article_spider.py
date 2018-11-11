#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# **********************************************************
# * Author        : huangtao
# * Email         : 807250120@qq.com
# * Create time   : 2018/11/12 12:02 AM
# * Last modified : 2018/11/12 12:02 AM
# * Filename      : huxiu_new_article_spider.py
# * Description   : 虎嗅最新文章
# **********************************************************

import scrapy
from scrapy.selector import Selector
from dateutil import parser

class HuXiuSpider(scrapy.Spider):
    name = 'huxiu_new_article_spider'

    def __init__(self, object_urls=None, *args, **kwargs):
        super(HuXiuSpider, self).__init__(*args, **kwargs)
        self.start_urls = ['https://m.huxiu.com/maction/article_list']

    def parse(self, response):
        sel = Selector(response)
        content_list = sel.xpath('//div[@class="related-article"]/ul/li')
        task_source = response.meta
        for content_ele in content_list:
            url = 'https://www.huxiu.com%s' % content_ele.xpath('./a/@href').extract_first()
            title = content_ele.xpath('./a/text()').extract_first()
            day = content_ele.xpath('./span/text()').extract_first()
            info_time = parser.parse(day)

            print title
            print url
            print info_time
