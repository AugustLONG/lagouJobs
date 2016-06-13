from __future__ import absolute_import

#import os
import subprocess
from celery import task


@task()
def crawl():
    # os.environ['SCRAPY_SETTINGS_MODULE'] = 'crawler.jobsnews.settings'
    return subprocess.call(['scrapy', 'crawl', 'lagoujobs'])
