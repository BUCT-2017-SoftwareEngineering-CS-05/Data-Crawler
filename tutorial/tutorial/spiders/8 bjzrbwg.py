# 76 - 119
# -*- coding: utf-8 -*-
import scrapy
from tutorial.items import TutorialItem


class InfoSpider(scrapy.Spider):
    name = 'info8'

    def start_requests(self):
        start_page = 1
        end_page = 16
        base_url = "http://www.bmnh.org.cn/gzxx/gzbb/"
        count = 0
        for i in range(start_page, end_page):
            url = base_url + str(i) + '/list.shtml'
            count += 1
            yield scrapy.Request(url=url, callback=self.parse, meta={'id': count})

    def parse(self, response):
        if response.status == '404':
            return
        Items = TutorialItem()
        Items['midx'] = '8'
        Items['id'] = response.meta['id']
        name = []
        pic = []
        picurl = "http://www.bmnh.org.cn/"
        for i in response.xpath('/html/body/div[3]/div[3]/div[2]/div[1]/div'):
            p = picurl+i.xpath('/a/img@src')
            n = i.xpath('/div/div/a/h3/text()')
            pic.append(p)
            name.append(n)
        Items['name'] = name
        Items['text'] = ''
        Items['pic'] = pic
        yield Items
