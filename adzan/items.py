# -*- coding: utf-8 -*-
import scrapy
class AdzanItem(scrapy.Item):
		c = scrapy.Field() # city
		d = scrapy.Field() # day
		s = scrapy.Field() # shubuh
		t = scrapy.Field() # terbit
		z = scrapy.Field() # zuhur
		a = scrapy.Field() # ashr
		m = scrapy.Field() # maghrib
		i = scrapy.Field() # isya