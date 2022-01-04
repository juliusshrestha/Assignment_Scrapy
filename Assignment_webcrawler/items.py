# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class AssignmentWebcrawlerItem(scrapy.Item):
    # define the fields for your item here like:
    item_name = scrapy.Field()
    price = scrapy.Field()
    
