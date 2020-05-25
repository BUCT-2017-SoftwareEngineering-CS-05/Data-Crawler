# -*- coding: utf-8 -*-
import scrapy
from tutorial.items import TutorialItem
from urllib import parse
from tutorial.requests import SeleniumRequest
from tutorial.Spider import SeleniumSpider
from tutorial.tools import waitForXpath
from bs4 import BeautifulSoup


class InfoSpider(SeleniumSpider):
    name = 'info36'

    def start_requests(self):
        url = 'http://www.hljmuseum.com/cpgz/cpxs/zgzb/'
        yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        if response.status == '404':
            return
        # print(response.body.decode('utf-8'))
        baseurl = 'http://www.hljmuseum.com'
        for i in response.xpath('/html/body/div[2]/div[3]/div[1]/div[1]/ul/div'):
            if i.xpath('li/a/@href').get() == None:
                continue
            url = baseurl + i.xpath('li/a/@href').get()
            pic = i.xpath('li/a/img/@src').get()
            name = i.xpath('li/a/span/text()').get()
            yield SeleniumRequest(url=url, meta={'pic': pic, 'name': name}, callback=self.parse_detail)

    def parse_detail(self, response):
        item = TutorialItem()
        item['midx'] = '36'
        item['name'] = response.meta['name']
        item['pic'] = response.meta['pic']
        html = response.body.decode('utf-8')
        suop = BeautifulSoup(html, 'html.parser')
        t = ''
        for i in suop.find_all('div', class_='duanluo'):
            t = t + i.get_text().strip()
        # for i in response.xpath('/html/body/div[2]/div[3]/div[1]/div[1]/div[2]/div[1]/div'):
        #     t = t + i.xpath('')
        item['text'] = t
        print(item['name'])
        print(item['text'])
        print(item['pic'])
        yield item

