# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class eduItem(scrapy.Item):
    # define the fields for your item here like:
    mid = scrapy.Field()
    name = scrapy.Field()
    url = scrapy.Field()
    details = scrapy.Field()
    pass


class visitItem(scrapy.Item):
    season = scrapy.Field()
    time = scrapy.Field()
    pass


class academyItem(scrapy.Item):
    mid = scrapy.Field()
    name = scrapy.Field()
    url = scrapy.Field()
    pass