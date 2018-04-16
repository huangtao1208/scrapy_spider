# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


# 豆瓣读书
class DoubanBookListItem(scrapy.Item):
    # 书籍背景图片地址
    cover_url = scrapy.Field()
    # 书籍详细页地址
    url = scrapy.Field()
    # 书籍名称
    book_name = scrapy.Field()
    # 书籍作者
    book_author = scrapy.Field()
    # 书籍介绍
    book_detail = scrapy.Field()
    # 书籍页数
    book_page_num = scrapy.Field()
    # 书籍价格
    book_price = scrapy.Field()
    # 发布时间
    publish_time = scrapy.Field()



# 简书的全站用户信息
class JianshuUserItem(scrapy.Item):
    # 用户名称
    name = scrapy.Field()
    # 关注数
    followNumber = scrapy.Field()
    # 粉丝数
    fansNumber = scrapy.Field()
    # 文章数
    articleNumber = scrapy.Field()
    # 字数
    wordCount = scrapy.Field()
    # 收获喜欢数
    likeNumber = scrapy.Field()