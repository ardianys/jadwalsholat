# -*- coding: utf-8 -*-
import scrapy

from adzan.items import AdzanItem

class JadwaltodaySpider(scrapy.Spider):
    name            = "jadwaltoday"
    allowed_domains = ["http://jadwalsholat.pkpu.or.id/"]

    def __init__(self, city_id=83, *args, **kwargs):
        super(JadwaltodaySpider, self).__init__(*args, **kwargs)
        self.start_urls = ['http://jadwalsholat.pkpu.or.id/monthly.php?id=%s' % city_id]
        self.city_id    = city_id

    def parse(self, response):
        jadwal = []
    	
        date = response.xpath("//tr[contains(@class, 'table_highlight')]/td").re(r'<b>(\d{2})</b>')[0]

        for i in response.xpath("//tr[contains(@class, 'table_highlight')]/td").re(r'(\d{2}:\d{2})'):
            jadwal.append(i)

        item = AdzanItem()
        item['c'] = self.city_id
        item['d'] = date
        item['s'] = jadwal[0]
        item['t'] = jadwal[1]
        item['z'] = jadwal[2]
        item['a'] = jadwal[3]
        item['m'] = jadwal[4]
        item['i'] = jadwal[5]
        yield item