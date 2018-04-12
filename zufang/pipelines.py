# -*- coding: utf-8 -*-

from scrapy.conf import settings
import pymongo

# 保存信息到mongoDB中
class MongoDBPipelines(object):

    def __init__(self):
        host = settings['MONGODB_HOST']
        port = settings['MONGODB_PORT']
        dbName = settings['MONGODB_DBNAME']

        client = pymongo.MongoClient(host=host, port=port)
        tdb = client[dbName]

        self.post = tdb[settings['MONGODB_DOCNAME']]

    def process_item(self, item, spider):
        # 将item转换为一个字典
        i = self.post.count()
        item['_id'] = i+1
        news_info = dict(item)
        # 插入到数据库中
        self.post.insert(news_info)
        return item
