# 分布式租房爬虫系统

## 用到的模块
- scrapy
- redis
- mongoDB
- redis
- scrapy-redis
- flask

* scrapy不会安装的可参考:[https://blog.csdn.net/junmoxi/article/details/70519598](https://blog.csdn.net/junmoxi/article/details/70519598) *

## 使用步骤

1. 启动MongoDB服务
2. 启动Redis服务
3. 运行monitor下的app.py启动监控系统
4. 运行lpush.py将起始URL压入队列
5. 运行start.py

## 监控系统

将monitor目录clone到spiders的同级目录下
在 scrapy的settings.py中添加下列设置
1. 添加DOWNLOADER_MIDDLEWARES
> monitor.statscol.StatcollectorMiddleware
2. 添加ITEM_PIPELINES
> monitor.statscol.SpiderRunStatspipeline
3. 添加STATS_KEYS
> STATS_KEYS = ['downloader/request_count', 'downloader/response_count','downloader/response_status_count/200', 'item_scraped_count']


### 效果图
![监控图片](https://github.com/pibigstar/scrapy-zufang/blob/master/监控.png)