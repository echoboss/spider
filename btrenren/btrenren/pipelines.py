# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from datetime import datetime
from scrapy.conf import settings
import pymongo

class BtrenrenPipeline(object):
    def __init__(self):
        self.host = settings['MONGODB_HOST']
        self.port = settings['MONGODB_PORT']
        self.dbname = settings['MONGODB_DBNAME']
        self.client = pymongo.MongoClient(host=self.host,port=self.port)
        self.mdb = self.client[self.dbname]
        self.post = self.mdb[settings['MONGODB_DOCNAME']]

    def process_item(self, item, spider):
        self.post.insert(dict(item))

        return item
