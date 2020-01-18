# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapyAppItem(scrapy.Item):
    url = scrapy.Field()
    categories = scrapy.Field()
    price = scrapy.Field()
    title = scrapy.Field()
    colours = scrapy.Field()
    sizes = scrapy.Field()
    image_url = scrapy.Field()
    description = scrapy.Field()
