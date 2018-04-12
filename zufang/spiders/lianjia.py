# -*- coding: utf-8 -*-
import redis
import scrapy

from  zufang.items import ZuFangItem
from scrapy.selector import Selector
from scrapy.http import Request
from scrapy_redis.spiders import RedisSpider

# 普通爬虫继承的是 scrapy.Spider
class LianJiaSpider(RedisSpider):
    name = "lianjia"
    #   start_urls = ["https://zz.zu.anjuke.com/fangyuan/p1"]
    #   allowed_domains = ["news.sogou.com"]
    redis_key = "lianjia"

    def parse(self, response):
        # response包含网页的各种参数 body源代码 url
        html_body = bytes.decode(response.body, encoding='utf-8')
        sel = Selector(text=html_body, type='html')
        ul = sel.xpath('//*[@id="house-lst"]')
        lis = ul.xpath('li')
        for li in lis:
            try:
                item = ZuFangItem()
                url = li.xpath('div[2]/h2/a/@href').extract()
                if len(url) > 0:
                    url = url[0]
                    item['url'] = url
                    print url
                    request = Request(url=str(url), callback=self.parse_info, meta={'item': item}, dont_filter=True)
                    yield request
            except Exception:
                continue

    def parse_info(self, response):

        html_body = bytes.decode(response.body, encoding='utf-8')
        sel = Selector(text=html_body, type='html')
        item = response.meta['item']

        name = sel.xpath('/html/body/div[4]/div[1]/div/div[1]/h1/text()').extract()
        rent = sel.xpath('/html/body/div[4]/div[2]/div[2]/div[1]/span[1]/text()').extract()
        area = sel.xpath('/html/body/div[4]/div[2]/div[2]/div[2]/p[1]/text()').extract()
        household_type = sel.xpath('/html/body/div[4]/div[2]/div[2]/div[2]/p[2]/text()').extract()
        housing_facing = sel.xpath('/html/body/div[4]/div[2]/div[2]/div[2]/p[4]/text()').extract()
        storey = sel.xpath('/html/body/div[4]/div[2]/div[2]/div[2]/p[3]/text()').extract()
        metro = sel.xpath('/html/body/div[4]/div[2]/div[2]/div[2]/p[5]/text()').extract()
        village = sel.xpath('/html/body/div[4]/div[2]/div[2]/div[2]/p[6]/a[1]/text()').extract()
        position = sel.xpath('/html/body/div[4]/div[2]/div[2]/div[2]/p[7]/a[1]/text()').extract()
        release_time = sel.xpath('/html/body/div[4]/div[2]/div[2]/div[2]/p[8]/text()').extract()

        print self.get_value(name)
        item['name'] = self.get_value(name)
        item['rent'] = self.get_value(rent)
        item['area'] = self.get_value(area)
        item['household_type'] = self.get_value(household_type)
        item['housing_facing'] = self.get_value(housing_facing)
        item['storey'] = self.get_value(storey)
        item['metro'] = self.get_value(metro)
        item['village'] = self.get_value(village)
        item['position'] = self.get_value(position)
        item['release_time'] = self.get_value(release_time)

        yield item
        
    ''''判断是否有值，如果有则返回第一个值'''
    def get_value(self, value):
        if len(value) > 0:
            return value[0]
        else:
            return value











