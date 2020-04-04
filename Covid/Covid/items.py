# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class CovidItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # pais = scrapy.Field()
    # muertos = scrapy.Field()
    # infectados = scrapy.Field()
    # curados = scrapy.Field()
    pregunta = scrapy.Field()
    id = scrapy.Field()