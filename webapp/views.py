#!/usr/bin/env python
# -*- coding:utf-8 -*-
from django.shortcuts import render
from webapp.models import JobsNewsItem, JobsNewsItemSet
#from django.db import connection
#from django.db import connection, transaction

def home(request):
    latest_item_set = JobsNewsItemSet.objects.last()
    list = JobsNewsItem.objects.filter(item_set=latest_item_set)
    #top10 = list(set(list))[:8]  __lte
    return render(request, 'main.html', {
            'items': list,
            'timestamp': latest_item_set and latest_item_set.timestamp
    })



# topdata = []
# for top in list(set(JobsNewsItem.objects.order_by("-createtime").iterator())):
#     topdata.append(top)
#
# top10 = list(set(topdata))[:8]
# 数据库小写
#     raw_sql = 'select * from webapp_jobsnewsitem order by createtime desc'
#     table = JobsNewsItem.objects.raw(raw_sql)  # xx.objects.raw()执行原始sql
#
#     top10 = list(set(table))[:10]
#     raw_sql = 'select * from webapp_jobsnewsitem order by createtime desc'
#     cursor = connection.cursor()  # 获得一个游标(cursor)对象
#
#     # 更新操作
#     cursor.execute(raw_sql)  # 执行sql语句
#     transaction.commit_unless_managed()  # 提交到数据库
#
#     table = cursor.fetchone()
#     top10 = list(set(table))[:12]
    # table = cursor.fetchall()  # 返回的结果集是个元组
    # top10 = list(set(table))[:12]
    # raw_sql = 'select * from webapp_jobsnewsitem order by createtime desc'
    #
    # cursor = connection.cursor()  # 获得一个游标(cursor)对象
    # cursor.execute(raw_sql)
    # table = cursor.fetchall()  # 返回的结果集是个元组
    # top10 = list(set(table))[:12]
    # raw_sql = 'select * from webapp_jobsnewsitem order by createtime desc'
    # try:
    #     table = JobsNewsItem.objects.raw(raw_sql).delete  # xx.objects.raw()执行原始sql
    #     table10 = list(set(table))[:10]
    #     print  table10
    # except:
    #     tablelist = JobsNewsItem.objects.raw(raw_sql)
    #     top10 = list(set(tablelist))[:10]



    #select * from webapp_jobsnewsitem order by createTime desc;
    #
    #JobsNewsItem.objects.order_by("-createTime").delete()

    #tablelist = JobsNewsItem.objects.all()
    #tablelist = JobsNewsItem.objects.order_by("positionName")
    #tablelist = JobsNewsItem.objects.last()

    # ID = models.IntegerField(null=True, blank=True)
    # positionName = models.CharField(null=True, blank=True, max_length=400)
    # salary = models.CharField(null=True, blank=True, max_length=400)
    # companyName = models.CharField(null=True, blank=True, max_length=400)
    # positionId = models.URLField(null=True, blank=True, max_length=400)
    # createTime = models.CharField(null=True, blank=True, max_length=400)



    # topdata = []
    # for top in JobsNewsItem.objects.all().iterator():
    #     topdata.append(top)
    #     #top = list(set(topdata))
    # top10 = list(set(sorted(topdata, key=lambda topdata: topdata.createTime, reverse=True)))[:9]

    #top10 =list(set(sorted(top)))[:6]
    #sorted(top10, key=lambda top10: top10.createTime, reverse=True)
    #top = list(set(topdata))[:5]
    #if top.ID
    # data = JobsNewsItem.objects.filter(createTime__gt="2016-03-10 09:46:49")
    # top10 = list(set(data))[:9]


#top10 = list(set(tablelist))[:5]
# for i in range(n):
#     for top in topdata.iterator():
#         top10.append(top)


#     tablelist = list(set(JobsNewsItem.objects.order_by("-createTime")))
#     #tablelist = JobsNewsItem.objects.order_by("-createTime")
#     #tablelist = JobsNewsItem.objects.all().order_by("-createTime")
#     top_10 = tablelist[:10]
#
#     timestandard = top_10[9].createTime
#     JobsNewsItem.objects.filter(createTime__lt=timestandard).delete()
#     return render(request, 'main.html', {
#         'items': top_10
#     })

# from django.shortcuts import render
# from webapp.models import JobsNewsItem
# import time

#
# def home(request):
#
#     tablelist = JobsNewsItem.objects.all()
#     top_10 = sorted(tablelist, key=lambda x: x[5], cmp=comparetime, reverse=True)[:10]
#
#     return render(request, 'main.html', {
#         'items': top_10
#     })

#
# def comparetime(time1, time2):
#     t1 = time.strptime(time1, '%Y-%m-%d %H:%M:%S')
#     t2 = time.strptime(time2, '%Y-%m-%d %H:%M:%S')
#     if t1.tm_year > t2.tm_year or t1.tm_year < t2.tm_year:
#         return t1.tm_year - t2.tm_year
#     else:
#         if t1.tm_mon > t2.tm_mon or t1.tm_mon < t2.tm_mon:
#             return t1.tm_mon - t2.tm_mon
#         else:
#             if t1.tm_mday > t2.tm_mday or t1.tm_mday < t2.tm_mday:
#                 return t1.tm_mday - t2.tm_mday
#             else:
#                 if t1.tm_hour > t2.tm_hour or t1.tm_hour < t2.tm_hour:
#                     return t1.tm_hour - t2.tm_hour
#                 else:
#                     if t1.tm_min > t2.tm_min or t1.tm_min < t2.tm_min:
#                         return t1.tm_min - t2.tm_min
#                     else:
#                         if t1.tm_sec > t2.tm_sec or t1.tm_sec <= t2.tm_sec:
#                             return t1.tm_sec - t2.tm_sec




