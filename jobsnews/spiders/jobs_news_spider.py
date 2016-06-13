#!/usr/bin/env python
# -*- coding:utf-8 -*-
from scrapy.contrib.spiders import CrawlSpider
from jobsnews.items import JobsNewsItem
from webapp.models import JobsNewsItemSet
import json
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


class Position:
    def __init__(self, positionName, salary, companyName, positionId, createTime):
        self.positionName = positionName
        self.salary = salary
        self.companyName = companyName
        self.positionId = positionId
        self.createTime = createTime


class JobsNewsSpider(CrawlSpider):
    name = "lagoujobs"
    start_urls = ['http://www.lagou.com/jobs/positionAjax.json?kd=python&px=new&gx=%E5%85%A8%E8%81%8C&city=%E4%B8%8A%E6%B5%B7']

    def parse(self, response):
        #url = 'http://www.lagou.com/jobs/positionAjax.json?kd=python&px=new&gx=%E5%85%A8%E8%81%8C&city=%E4%B8%8A%E6%B5%B7'
        # rcv = urllib2.urlopen(response.body_as_unicode()).read()
        # data = json.loads(rcv)
        #rcv = urllib2.urlopen(response.body_as_unicode()).read()

        item_set = JobsNewsItemSet()
        item_set.save()
        data = json.loads(response.body_as_unicode())
        p, number = [], 10

        for j in range(0, number):
            p.append(Position(data['content']['result'][j]['positionName'], data['content']['result'][j]['salary'], data['content']['result'][j]['companyName'], data['content']['result'][j]['positionId'], data['content']['result'][j]['createTime']))
            # print "No.%-8s\t%-24s\t%-8s\t%-8s\thttp://www.lagou.com/jobs/%-6s.html\t%-8s" % (
            #     j + 1, p[-1].positionName, p[-1].salary, p[-1].companyName, p[-1].positionId, p[-1].createTime)
            news_item = JobsNewsItem()
            news_item['item_set'] = item_set
            news_item['idnumber'] = p[-1].positionId
            news_item['positionname'] = p[-1].positionName
            news_item['salary'] = p[-1].salary
            news_item['companyname'] = p[-1].companyName
            news_item['positionid'] = 'http://www.lagou.com/jobs/'+ str(p[-1].positionId)+'.html'
            news_item['createtime'] = p[-1].createTime
            yield news_item  # nice



