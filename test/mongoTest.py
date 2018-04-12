# -*- coding: utf-8 -*-
import pymongo


connect = pymongo.MongoClient(host='127.0.0.1', port=27017)

# 数据库名为ceshi
tdb = connect['ceshi']
# 表名为lei
post_info = tdb['lei']

firstInfo = {'name': u'哈哈', 'url': 'http://www.jikexueyuan.com/'}

# 插入数据  要是一个字典，可以用dict() 函数转换
post_info.insert(firstInfo)

i = post_info.count()

post_info.remove({'name': u'哈哈'})


print i
print u'插入成功'


