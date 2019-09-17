# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class CoinItem(scrapy.Item):

    name = scrapy.Field()
    symbol = scrapy.Field()
    market_cap = scrapy.Field()
    price = scrapy.Field()
    circulation_supply = scrapy.Field()
    volume = scrapy.Field()
    
    pass
