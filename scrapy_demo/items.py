# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item,Field


class kugouTop500Item(Item):
    # define the fields for your item here like:
    index = Field()
    songname = Field()
    time = Field()
    url = Field()
    pass

class zhuantiItem(Item):
	"""docstring for zhuantiItem"""
	name = Field()
	fans = Field()
	content = Field()
	article = Field()
		