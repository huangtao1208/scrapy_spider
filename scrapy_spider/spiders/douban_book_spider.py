#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# **********************************************************
# * Author        : huangtao
# * Email         : huangtao@yimian.me
# * Create time   : 2018/4/16 下午10:05
# * Last modified : 2018/4/16 下午10:05
# * Filename      : douban_book_spider.py.py
# * Description   : 获取豆瓣读书的书籍信息
# **********************************************************


import scrapy
from scrapy.selector import Selector
from scrapy_spider.items import DoubanBookListItem


class DoubanBookSpider(scrapy.Spider):
    name = "douban_book_spider"
    allowed_domains = ["book.douban.com"]

    def __init__(self, *args, **kwargs):
        super(DoubanBookSpider, self).__init__(*args, **kwargs)
        self.start_urls = ['https://book.douban.com/latest?icn=index-latestbook-all']

    def parse(self, response):
        sel = Selector(response)
        book_list = sel.xpath('//ul[@class="cover-col-4 clearfix"]/li')
        for book_ele in book_list:
            book_item = DoubanBookListItem()
            # 书籍背景图片地址
            cover_url = book_ele.xpath('./a[@class="cover"]/img/@src').extract()[0]
            # 书籍详细页地址
            url = book_ele.xpath('./a[@class="cover"]/@href').extract()[0]
            # 书籍名称
            book_name = book_ele.xpath('./div[@class="detail-frame"]/h2/a/text()').extract()[0]
            # 书籍作者，我们发现这样获取到的信息包含了书籍作者、出版社和发布时间三个值，
            # 比如"[美] 彼得·布雷瓦 / 后浪丨文化发展出版社 / 2017-11"，它们是通过/进行累加的
            book_author_str = book_ele.xpath('./div[@class="detail-frame"]//p[@class="color-gray"]/text()').extract()[0]
            book_author_array = book_author_str.split("/")
            book_author = book_author_array[0].strip()
            # 发布时间
            publish_time = book_author_array[2].strip()
            # 书籍介绍
            book_detail = book_ele.xpath('./div[@class="detail-frame"]//p[@class="detail"]/text()').extract()[0]
            book_item["cover_url"] = cover_url.strip()
            book_item["url"] = url.strip()
            book_item["book_name"] = book_name.strip()
            book_item["book_author"] = book_author.strip()
            book_item["publish_time"] = publish_time.strip()
            book_item["book_detail"] = book_detail.strip()

            # 进到书籍详细页去获取书籍页数和价格信息
            yield scrapy.Request(url=url, meta={'book_item': book_item}, callback=self.parse_detail)

    # 书籍详细页
    def parse_detail(self, response):
        # response.meta.get("book_item", "")
        book_item = response.meta['book_item']
        sel = Selector(response)
        # 书籍页数
        book_page_num_str = sel.xpath(u'//div[@id="info"]//span[text()="页数:"]').extract()
        if book_page_num_str:
            book_page_num = sel.xpath(u'//div[@id="info"]//span[text()="页数:"]/following::text()[1]').extract()[0]
        else:
            book_page_num = ''
        # 书籍价格
        book_price_str = sel.xpath(u'//div[@id="info"]//span[text()="定价:"]').extract()
        if book_price_str:
            book_price = sel.xpath(u'//div[@id="info"]//span[text()="定价:"]/following::text()[1]').extract()[0]
        else:
            book_price = ''

        book_item["book_page_num"] = book_page_num.strip()
        book_item["book_price"] = book_price.strip()

        # print '书籍信息如下>>>>>>>>'
        # print book_item["cover_url"]
        # print book_item["url"]
        # print book_item["book_name"]
        # print book_item["book_author"]
        # print book_item["publish_time"]
        # print book_item["book_detail"]
        # print book_item["book_page_num"]
        # print book_item["book_price"]

        yield book_item