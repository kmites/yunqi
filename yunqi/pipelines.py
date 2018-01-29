# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from pymongo import MongoClient
from .items import BookHotItem,BookInfoItem

class YunqiPipeline(object):

    def open_spider(self,spider):
        self.client = MongoClient('mongodb://localhost:27017/')
        self.db = self.client['yunqi']

    def process_item(self, item, spider):
        if isinstance(item,BookInfoItem):
            self.save_book_info(item)
        elif isinstance(item,BookHotItem):
            self.save_book_hot(item)

    def close_spider(self,spider):
        self.client.close()

    def save_book_info(self,item):
        self.db.BookInfo.insert(dict(item))

    def save_book_hot(self,item):
        self.db.BookHot.insert(dict(item))