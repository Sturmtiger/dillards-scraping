# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

from dillards_app.tasks import save_products_to_db


class ScrapyAppPipeline(object):
    def __init__(self, crawler):
        self.crawler = crawler
        self.items = list()

    def process_item(self, item, spider):
        self.items.append(item._values)
        if len(self.items) >= 200:
            save_products_to_db.delay(self.items)
            self.items.clear()
        return item

    def close_spider(self, spider):
        if self.items:
            save_products_to_db.delay(self.items)
