#!/usr/bin/env python
# -*- coding:utf-8 -*-
import os
import sys

sys.path.append(os.path.abspath('../../'))
os.environ['DJANGO_SETTINGS_MODULE'] = 'jobs_clone.settings'

BOT_NAME = 'jobsnews'
USER_AGENT = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/47.0.2526.73 Chrome/47.0.2526.73 Safari/537.36'
SPIDER_MODULES = ['jobsnews.spiders']
NEWSPIDER_MODULE = 'jobsnews.spiders'

ITEM_PIPELINES = {
    'jobsnews.pipelines.JobsnewsDbStorePipeline': 300,
}

DOWNLOAD_DELAY = 0.5
