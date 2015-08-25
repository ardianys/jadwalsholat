# -*- coding: utf-8 -*-
import scrapy
import csv
import os

from adzan.items import AdzanItem

class JadwalsholatSpider(scrapy.Spider):
    name            = "jadwalsholat"
    allowed_domains = ["http://jadwalsholat.pkpu.or.id/"]
    cities          = {}

    def __init__(self, city_id=83, *args, **kwargs):
        super(JadwalsholatSpider, self).__init__(*args, **kwargs)
        self.start_urls = ['http://jadwalsholat.pkpu.or.id/monthly.php?id=%s' % city_id]
        self.city_id    = city_id
        root_dir = os.path.abspath(os.path.dirname(__file__))
        csv_path = os.path.join(root_dir, '../data/cities.csv')
        with open(csv_path,"rb") as source:
          reader= csv.reader( source )
          for r in reader:
            self.cities[r[0]] = r[1]
        try:
          self.cities[city_id]
        except Exception:
          raise Exception('city_id not available, please check ./data/cities.csv')

    def parse(self, response):
        date   = []
        jadwal = []
    	
        for i in response.xpath("//tr/td").re(r'<b>(\d{2})</b>'):
            date.append(i)

        for i in response.xpath("//tr/td").re(r'(\d{2}:\d{2})'):
            jadwal.append(i)

        for i in xrange(0, len(date)):
            item = AdzanItem()
            item['c'] = self.city_id
            item['d'] = i+1
            item['s'] = jadwal[i+0+i*5]
            item['t'] = jadwal[i+1+i*5]
            item['z'] = jadwal[i+2+i*5]
            item['a'] = jadwal[i+3+i*5]
            item['m'] = jadwal[i+4+i*5]
            item['i'] = jadwal[i+5+i*5]
            yield item