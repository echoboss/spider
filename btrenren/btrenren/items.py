# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class BtrenrenItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    alias = scrapy.Field()
    tags = scrapy.Field()
    locality = scrapy.Field()
    year = scrapy.Field()
    director = scrapy.Field()
    screenwriter = scrapy.Field()
    star = scrapy.Field()
    imdb = scrapy.Field()
    info = scrapy.Field()
    bt_url = scrapy.Field()
    context = scrapy.Field()
    img_url = scrapy.Field()
    source_url = scrapy.Field()