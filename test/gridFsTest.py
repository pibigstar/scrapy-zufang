# --* coding=utf-8 *--
from cStringIO import StringIO
from pymongo import MongoClient
import gridfs
import os
import matplotlib.pyplot as plt
import matplotlib.image as iming
import bson.binary
import numpy as np
if __name__ == '__main__':
        connect = MongoClient('127.0.0.1', 27017)  # 创建连接点
        db = connect.Spider
        # print db.collection_names() 打印出集合中所有的字段名
        imgput = gridfs.GridFS(db)

        dirs = 'F:\image'
        files = os.listdir(dirs)
        for file in files:
            filesname = dirs + '\\' + file
            print filesname
            f = file.split('.')
            datatmp = open(filesname, 'rb')
            data = StringIO(datatmp.read())

            insertimg = imgput.put(data, content_type=f[1], filename=f[0])
            datatmp.close()