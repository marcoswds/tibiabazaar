# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class TibiabazzarItem(scrapy.Item):

    name = scrapy.Field()
    server =  scrapy.Field()
    lvl = scrapy.Field()
    vocation = scrapy.Field()
    sex = scrapy.Field()
    item1 = scrapy.Field()
    item2 = scrapy.Field()
    item3 = scrapy.Field()
    item4 = scrapy.Field()
    start = scrapy.Field()
    end = scrapy.Field()
    status_auction = scrapy.Field()
    tc = scrapy.Field()
    special_features1 = scrapy.Field()
    special_features2 = scrapy.Field()
    special_features3 = scrapy.Field()
    special_features4 = scrapy.Field()
    special_features5 = scrapy.Field()

