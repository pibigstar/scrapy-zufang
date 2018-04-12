# coding: utf-8
'''
多线程爬虫示例
'''
from Queue import Queue
import threading
import urllib2
import time
import json
import codecs
from bs4 import BeautifulSoup

urls_queue = Queue()
data_queue = Queue()
lock = threading.Lock()
f = codecs.open('out.txt', 'w', 'utf8')


class ThreadUrl(threading.Thread):

    def __init__(self, queue):
        threading.Thread.__init__(self)
        self.queue = queue

    def run(self):
        pass


class ThreadCrawl(threading.Thread):

    def __init__(self, url, queue, out_queue):
        threading.Thread.__init__(self)
        self.url = url
        self.queue = queue
        self.out_queue = out_queue

    def run(self):
        while True:
            item = self.queue.get()
            data = self._data_post(item)
            try:
                req = urllib2.Request(url=self.url, data=data)
                res = urllib2.urlopen(req)
            except urllib2.HTTPError, e:
                raise e.reason
            py_data = json.loads(res.read())
            res.close()
            item['first'] = 'false'
            item['pn'] = item['pn'] + 1
            success = py_data['success']
            if success:
                print 'Get success...'
            else:
                print 'Get fail....'
            print 'pn is : %s' % item['pn']
            result = py_data['content']['result']
            if len(result) != 0:
                self.queue.put(item)
            print 'now queue size is: %d' % self.queue.qsize()
            self.out_queue.put(py_data['content']['result'])
            self.queue.task_done()

    def _data_post(self, item):
        pn = item['pn']
        first = 'false'
        if pn == 1:
            first = 'true'
        return 'first=' + first + '&pn=' + str(pn) + '&kd=' + item['kd']

    def _item_queue(self):
        pass


class ThreadWrite(threading.Thread):

    def __init__(self, queue, lock, f):
        threading.Thread.__init__(self)
        self.queue = queue
        self.lock = lock
        self.f = f

    def run(self):
        while True:
            item = self.queue.get()
            self._parse_data(item)
            self.queue.task_done()

    def _parse_data(self, item):
        for i in item:
            l = self._item_to_str(i)
            with self.lock:
                print 'write %s' % l
                self.f.write(l)

    def _item_to_str(self, item):
        positionName = item['positionName']
        positionType = item['positionType']
        workYear = item['workYear']
        education = item['education']
        jobNature = item['jobNature']
        companyName = item['companyName']
        companyLogo = item['companyLogo']
        industryField = item['industryField']
        financeStage = item['financeStage']
        companyShortName = item['companyShortName']
        city = item['city']
        salary = item['salary']
        positionFirstType = item['positionFirstType']
        createTime = item['createTime']
        positionId = item['positionId']
        return positionName + ' ' + positionType + ' ' + workYear + ' ' + education + ' ' + \
            jobNature + ' ' + companyLogo + ' ' + industryField + ' ' + financeStage + ' ' + \
            companyShortName + ' ' + city + ' ' + salary + ' ' + positionFirstType + ' ' + \
            createTime + ' ' + str(positionId) + '\n'


def main():
    for i in range(4):
        t = ThreadCrawl(
            'http://www.lagou.com/jobs/positionAjax.json', urls_queue, data_queue)
        t.setDaemon(True)
        t.start()
    datas = [
        {'first': 'true', 'pn': 1, 'kd': 'Java'}
        #{'first': 'true', 'pn': 1, 'kd': 'Python'}
    ]
    for d in datas:
        urls_queue.put(d)
    for i in range(4):
        t = ThreadWrite(data_queue, lock, f)
        t.setDaemon(True)
        t.start()

    urls_queue.join()
    data_queue.join()

    with lock:
        f.close()
    print 'data_queue siez: %d' % data_queue.qsize()
main()