# encoding=utf-8
import redis
from demo.scrapy_redis.BloomfilterOnRedis import BloomFilter
from scrapy.utils.request import request_fingerprint
from scrapy import Request

rconn = redis.Redis('127.0.0.1', 6379)
bf = BloomFilter(rconn, 'spider_1:dupefilter')


if __name__ == '__main__':
    # while True:
        url = 'http://www.baidu.com/'
        request = Request(url)
        fp = request_fingerprint(request)
        print (fp)
        if bf.isContains(fp):
            print ('exist!')
        else:
            print ('not exist!')



