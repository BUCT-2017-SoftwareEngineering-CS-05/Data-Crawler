# 76 - 119
# -*- coding: utf-8 -*-
import scrapy
from tutorial.items import TutorialItem


class InfoSpider(scrapy.Spider):
    name = 'info4'

    def start_requests(self):
        start_page = 32725
        end_page = 33091
        base_url = "http://www.jb.mil.cn/gcww/wwjs_new/gjdww/201707/t20170704_"
        count = 0
        for i in range(start_page, end_page):
            url = base_url + str(i) + '.html'
            count += 1
            yield scrapy.Request(url=url, callback=self.parse, meta={'id': count})

    def parse(self, response):
        if response.status == '404':
            return
        Items = TutorialItem()
        Items['midx'] = '4'
        Items['id'] = response.meta['id']
        Items['name'] = response.css('.interContext > h2:nth-child(1)::text').extract()[0]
        s = str(response.css('.TRS_Editor > p:nth-child(3)::text').extract()[0]).strip()
        Items['text'] = s
        picurl = "http://www.gmc.org.cn/"
        p = ''
        l = ['兽面纹铙', '背剑带釉俑', '“薛师”铭文戟', '双耳兽面纹簋']
        if Items['name'] in l:
            for i in response.css('.TRS_Editor > p:nth-child(1) > a:nth-child(1) > img:nth-child(1)::attr(oldsrc)').extract():
                p = p + str(i)
        else:
            for i in response.css('.TRS_Editor > p:nth-child(1) > img:nth-child(1)::attr(oldsrc)').extract():
                p = p + str(i)
        Items['pic'] = picurl + p
        yield Items
