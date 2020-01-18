# -*- coding: utf-8 -*-
import scrapy


class DillardsSpider(scrapy.Spider):
    name = 'dillards'
    allowed_domains = ['dillards.com']
    start_urls = ['http://dillards.com/']

    def parse(self, response):
        pass
