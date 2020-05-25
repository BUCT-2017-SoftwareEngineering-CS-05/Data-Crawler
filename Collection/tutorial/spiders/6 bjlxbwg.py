# 76 - 119
# -*- coding: utf-8 -*-
import scrapy
from tutorial.items import TutorialItem


class InfoSpider(scrapy.Spider):
    name = 'info6'

    def start_requests(self):
        start_page = 1179
        end_page = 1186
        base_url = "http://www.luxunmuseum.com.cn/html/201509/a"
        count = 0
        for i in range(start_page, end_page):
            if i == 1185:
                url = base_url[:-3] + '7/a' + str(i) + '.htm'
            else:
                url = base_url + str(i) + '.htm'
            count += 1
            yield scrapy.Request(url=url, callback=self.parse, meta={'id': count})

    def parse(self, response):
        if response.status == '404':
            return
        Items = TutorialItem()
        Items['midx'] = '6'
        Items['id'] = response.meta['id']
        Items['name'] = response.css('.content_title::text').extract()
        print(Items['name'])
        s = ''
        for i in response.css('#zoom > p:nth-child(2) > span:nth-child(2)::text').extract():
            s = s + str(i).strip() + ' '
        Items['text'] = s
        print(Items['text'])
        picurl = "http://www.luxunmuseum.com.cn"
        p = str(response.css('#zoom > p:nth-child(1) > img:nth-child(1)::attr(src)').extract())
        Items['pic'] = picurl + p
        print(Items['pic'])
        yield Items