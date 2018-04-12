# -*- coding: utf-8 -*-
import redis
'''将URL压入队列'''

try:
    r = redis.Redis(host='localhost', port=6379)
    for i in range(1, 50):
        r.lpush("anjuke", "https://zz.zu.anjuke.com/fangyuan/p" + str(i))
    for i in range(1, 100):
        r.lpush("lianjia", "https://zz.lianjia.com/zufang/pg" + str(i))
    print("push url success!")

except Exception as e:
    print e
    print("push url failed！")