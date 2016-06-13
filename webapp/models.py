#!/usr/bin/env python
# -*- coding:utf-8 -*-
from django.db import models

class JobsNewsItemSet(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return unicode(self.timestamp)


class JobsNewsItem(models.Model):
    item_set = models.ForeignKey('JobsNewsItemSet', null=True)

    idnumber = models.IntegerField(null=True, blank=True)
    positionname = models.CharField(null=True, blank=True, max_length=400)
    salary = models.CharField(null=True, blank=True, max_length=400)
    companyname = models.CharField(null=True, blank=True, max_length=400)
    positionid = models.URLField(null=True, blank=True, max_length=400)
    createtime = models.CharField(null=True, blank=True, max_length=400)

    class Meta:
        ordering = ['-createtime']

