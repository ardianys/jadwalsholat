# -*- coding: utf-8 -*-
import scrapy

from adzan.items import AdzanItem

class JadwalshalatSpider(scrapy.Spider):
    name            = "jadwalsholat"
    allowed_domains = ["http://jadwalsholat.pkpu.or.id/monthly.php?id=267"]
    start_urls      = ('http://jadwalsholat.pkpu.or.id/monthly.php?id=267',)

    def parse(self, response):
        date   = []
        jadwal = []
    	
        for i in response.xpath("//tr/td").re(r'<b>(\d{2})</b>'):
            date.append(i)

        for i in response.xpath("//tr/td").re(r'(\d{2}:\d{2})'):
            jadwal.append(i)

        for i in xrange(0, len(date)):
            item = AdzanItem()
            item['c'] = 267
            item['d'] = i+1
            item['s'] = jadwal[i+0+i*5]
            item['t'] = jadwal[i+1+i*5]
            item['z'] = jadwal[i+2+i*5]
            item['a'] = jadwal[i+3+i*5]
            item['m'] = jadwal[i+4+i*5]
            item['i'] = jadwal[i+5+i*5]
            yield item