#!/usr/bin/env python
# -*- coding:utf-8 -*-
from scrapy_djangoitem import DjangoItem
from webapp import models


class JobsNewsItem(DjangoItem):
    django_model = models.JobsNewsItem
