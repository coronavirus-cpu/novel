# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class GhspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field()
    follower = scrapy.Field()
    email = scrapy.Field()
    company = scrapy.Field()
    location = scrapy.Field()
    gh_url = scrapy.Field()
    has_key = scrapy.Field()
    create_at = scrapy.Field()
