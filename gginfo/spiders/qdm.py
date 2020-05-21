# -*- coding: utf-8 -*-
import scrapy
import bs4
import re
from gginfo import items


class QdmSpider(scrapy.Spider):
    name = 'qdm'
    # allowed_domains = ['http://www.qingdaomuseum.com/collection/detail/100']
    # start_urls = ['http://http://www.qingdaomuseum.com/collection/detail/100/']

    def start_requests(self):
        start_page = 100
        end_page = 250
        base_url = "http://www.qingdaomuseum.com/collection/detail/"
        count = 0
        for i in range(start_page, end_page):
            url = base_url + str(i)
            count += 1
            yield scrapy.Request(url=url, callback=self.parse, meta={'id': count})

    def parse(self, response):
        if (response.status == '404'):
            return
        Items = items.GginfoItem()
        Items['id'] = 68
        name = response.css('body > div.n_dc > div.wccp_n > div > h3::text').extract()
        if (len(name) == 0):
            return
        Items['name'] = str(name[0]).strip()
        pic = response.css('body > div.n_dc > div.wccp_n > div > div.wrapper > div > div.stage > div > ul > li:nth-child(1) > img::attr(src)').extract()
        if (len(pic) == 0):
            return
        base_url = ""
        pic1 = str(pic[0]).strip()
        pic2 = ""
        for i in range(0, len(str(pic[0]).strip())):
            pic2 += pic1[i]
        url = base_url + pic2
        Items['pic'] = url
        text = response.css('body > div.n_dc > div.wccp_n > div > div.dc_nr > div > p::text').extract()
        if (len(text) == 0):
            Items['text'] = ""
        else:
            s = ""
            for item in text:
                s += str(str(item).strip()).replace('\u3000', '')
            Items['text'] = s.replace('\xa0', '')
        if Items['text'] == "":
            return
        yield Items
