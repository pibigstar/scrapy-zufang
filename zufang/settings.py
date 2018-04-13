# -*- coding: utf-8 -*-

# 爬虫名字
BOT_NAME = 'zufang'

SPIDER_MODULES = ['zufang.spiders']
NEWSPIDER_MODULE = 'zufang.spiders'

# 设置下载管道 300是优先级，数越小优先级越高
ITEM_PIPELINES = {
'zufang.pipelines.MongoDBPipelines': 300,
'zufang.monitor.statscol.SpiderRunStatspipeline': 301   # 监控配置
}

# 设置请求头
DEFAULT_REQUEST_HEADERS = {
  'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
  'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
  'Accept-Encoding': "gzip, deflate, sdch"
}

# 设置中间件，随机更换User-Agent
DOWNLOADER_MIDDLEWARES = {
    'zufang.monitor.statscol.StatcollectorMiddleware': 200,  # 监控配置
    "zufang.middlewares.UserAgentMiddleware": 401
}
# 间隔时间
DOWNLOAD_DELAY = 0.5

# 不读取robots.txt
#ROBOTSTXT_OBEY = False

# 禁止重定向
# REDIRECT_ENABLED = False

# 禁用cookie
# COOKIES_ENABLED = False

# 重试次数
RETRY_ENABLED = True
RETRY_TIMES = 3
# 遇到哪些返回码会重新重试
RETRY_HTTP_CODECS = {500, 503}


# mongoDB
MONGODB_HOST = '127.0.0.1'
MONGODB_PORT = 27017
MONGODB_DBNAME = 'Spider'
MONGODB_DOCNAME = 'zufang'

# redis
# 修改scrapy默认的调度器为scrapy重写的调度器 启动从reids缓存读取队列调度爬虫
# SCHEDULER = 'zufang.scrapy_redis.scheduler.Scheduler'
# 调度状态持久化，不清理redis缓存，允许暂停/启动爬虫
SCHEDULER_PERSIST = True
# 请求调度使用优先队列（默认)
# SCHEDULER_QUEUE_CLASS = 'zufang.scrapy_redis.queue.SpiderPriorityQueue'
REDIE_URL = None
REDIS_HOST = '127.0.0.1'
REDIS_PORT = 6379

# 将信息保存到文件中
# FEED_URI = 'file://F:/MongoDb/news.csv'
# FEED_FORMAT = 'csv'

# 运行多个爬虫配置
COMMANDS_MODULE = 'zufang.commands'

# 监控装置
STATS_KEYS = ['downloader/request_count', 'downloader/response_count','downloader/response_status_count/200', 'item_scraped_count']

# 断点续爬配置
SPIDER_MIDDLEWARES = {
   'zufang.scrapy_deltafetch.middleware.DeltaFetch': 50,
   'scrapy_magicfields.middleware.MagicFieldsMiddleware': 51,
}
DELTAFETCH_ENABLED = True
MAGICFIELDS_ENABLED = True
MAGIC_FIELDS = {
    "url": "scraped from $response:url",
}