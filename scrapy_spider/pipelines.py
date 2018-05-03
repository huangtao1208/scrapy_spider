# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import MySQLdb
import MySQLdb.cursors
# 设置字符集，防止编码参数出错
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

# 提交数据到mysql
class DataSubmitMySQLPipeline(object):
    def __init__(self):
        # 填写数据库用户名、数据库名、数据库用户密码、数据库url
        self.conn = MySQLdb.connect(user='root', db='spider_db', passwd='root',
                                    host='127.0.0.1',charset="utf8", use_unicode=True)

        self.cursor = self.conn.cursor()

    def process_item(self, item, spider):
        insert_sql = """
                insert into a_test(title, url)
                values(%s,%s)
            """
        self.cursor.execute(insert_sql, (item["title"], item["url"]))
        self.conn.commit()