# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
'''面积：91.1平米房屋户型：3室2厅2卫 楼层：高楼层 (共7层)房屋朝向：南 北
地铁：暂无数据
小区：普罗旺世地中海 - 6套出租中
位置：金水 庙李
时间：8天前发布'''

class ZuFangItem(scrapy.Item):

    _id = scrapy.Field() # id
    name = scrapy.Field() # 房名
    url = scrapy.Field() # 详细链接
    rent = scrapy.Field() # 租金
    area = scrapy.Field() #面积
    household_type = scrapy.Field() # 房屋户形
    housing_facing = scrapy.Field() # 房屋朝向
    storey = scrapy.Field() # 楼层
    metro = scrapy.Field() # 地铁
    village = scrapy.Field()# 小区
    position = scrapy.Field() #位置
    release_time = scrapy.Field() #发布时间


