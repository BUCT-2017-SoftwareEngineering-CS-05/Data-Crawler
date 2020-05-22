# 76 - 119
# -*- coding: utf-8 -*-
import scrapy
from tutorial.items import TutorialItem


class InfoSpider(scrapy.Spider):
    name = 'info77'

    def start_requests(self):
        start_page = 141
        end_page = 165
        base_url = "http://nyhhg.com/a/xy/"
        count = 0
        for i in range(start_page, end_page):
            url = base_url + str(i) + '.html'
            count += 1
            yield scrapy.Request(url=url, callback=self.parse, meta={'id': count})

    def parse(self, response):
        Items = TutorialItem()
        Items['midx'] = '77'
        Items['id'] = response.meta['id']
        Items['name'] = response.xpath('/html/body/div[4]/div[2]/div[2]/div[1]/text()').get()
        if Items['name'] == '阳乌':
            Items['text'] = response.xpath('/html/body/div[4]/div[2]/div[2]/div[3]/span/span/text()').get()
            print(Items['text'])
        else:
            Items['text'] = response.xpath('/html/body/div[4]/div[2]/div[2]/div[4]/span/span/text()').get()
        picurl = "http://nyhhg.com"
        Items['pic'] = picurl+str(response.css('html body div.main div.main_right div.content div img::attr(src)').extract()[0])
        yield Items


