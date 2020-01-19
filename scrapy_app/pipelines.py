# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy import signals
from dillards_app.tasks import save_products_to_db


class ScrapyAppPipeline(object):
    def __init__(self):
        self.items = list()

    def process_item(self, item, spider):
        self.items.append(item._values)
        if len(self.items) >= 300:
            save_products_to_db.delay(self.items)
            self.items.clear()
        return item

    def open_spider(self, spider):
        spider.crawler.signals.connect(
            self.save_remaining_products,
            signal=signals.spider_idle,
        )

    def save_remaining_products(self):
        if self.items:
            save_products_to_db.delay(self.items)
            self.items.clear()
