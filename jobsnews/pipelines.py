#!/usr/bin/env python
# -*- coding:utf-8 -*-
# http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.exceptions import DropItem


class JobsnewsDbStorePipeline(object):
    def process_item(self, item, spider):
        try:
            item.save()  # nice # calling DjangoItem.save() stores the item in the database
        except:
            raise DropItem('Unable to save the job: %s' % item.positionname)
        return item

# from scrapy.exceptions import DropItem
#
#
# class JobsnewsDbStorePipeline(object):
# # Duplicates filter
#     def __init__(self):
#         self.ids_seen = set()
#
#     def process_item(self, item, spider):
#         if item['ID'] in self.ids_seen:
#             raise DropItem("Duplicate item found: %s" % item)
#         else:
#             self.ids_seen.add(item['ID'])
#             return item

# from scrapy.exceptions import DropItem
# class FilterWordsPipeline(object):
# """A pipeline for filtering out items which contain certain words in their     description"""
#  # put all words in lowercase
# words_to_filter = ['politics', 'religion']
# def process_item(self, item, spider):
#     for word in self.words_to_filter:
#     if word in unicode(item['description']).lower():
#         raise DropItem("Contains forbidden word: %s" % word)
#     else:
#    return item