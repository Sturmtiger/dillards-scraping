# -*- coding: utf-8 -*-
import scrapy
from scrapy_redis.spiders import RedisSpider
from ..items import ScrapyAppItem


# class DillardsSpider(scrapy.Spider):
class DillardsSpider(RedisSpider):
    name = 'dillards'
    allowed_domains = ['dillards.com']
    # start_urls = ['https://www.dillards.com/c/men']

    def get_product_detail(self, response):
        """Collects product information."""
        url = response.url
        categories = ', '.join(response.meta['categories'])
        price = ''.join(response.xpath(
            '//div[contains(@class, "price-wrapper")]//div[1]/span[contains(@class, "price")]/text()'
        ).extract())  # ['$', 344]
        title = '{1} (Brand: {0})'.format(*response.xpath(
            '//h1[contains(@class, "product__title")]/descendant::text()'
        ).extract())  # ['brand', 'name']
        colours = ', '.join(response.xpath(
            '//div/select/option[position() > 1]/text() | //div/span[contains(@class, "one-option")]/text()'
        ).extract())  # [multiple]
        sizes = ', '.join(response.xpath(
            '//form[contains(@class, "productDisplay__form")]//div/ul/li/text()'
        ).extract())  # [multiple]
        image_url = response.xpath(
            '//figure[contains(@class, "main-img-wrapper")]/div/img/@src'
        ).extract_first()  # [single_img]
        description = ''.join(response.xpath(
            '//div[contains(@class, "product-description-wrapper")]/div/descendant::text()'
        ).extract())  # ['...', '....', '.....', ...]

        items = ScrapyAppItem()
        items['url'] = url
        items['categories'] = categories
        items['price'] = price
        items['title'] = title
        items['colours'] = colours
        items['sizes'] = sizes
        items['image_url'] = image_url
        items['description'] = description

        yield items

    def get_product_data_from_pages(self, response):
        """Collects a list of product URLs on the page."""
        products = response.xpath(
            '//div/div[contains(@class, "result-tile")]/div[contains(@class, "result-tile-below")]/a/@href'
        ).extract()

        categories = response.xpath(
            '//div[contains(@class, "CategoryNavigation")]/div[contains(@class, "filter-list")]/ul//text()'
        ).extract()

        for url in products:
            url = response.urljoin(url)
            yield scrapy.Request(url=url,
                                 callback=self.get_product_detail,
                                 meta={'categories': categories},
                                 )

        next_page = response.xpath(
            '//div[@id="topPagination"]/div[contains(@class, "pagination__wrapper")]/span[last() - 1]/a/@href'
        ).extract_first()

        if next_page:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(url=next_page, callback=self.get_product_data_from_pages)

    def parse(self, response):
        categories = response.xpath(
            '//div[contains(@class, "CategoryNavigation")]/div/ul/li[position() >= 2 and position() <= 4]/a/@href'
        ).extract()

        for url in categories[:1]:
            yield scrapy.Request(url=response.urljoin(url), callback=self.get_product_data_from_pages)
