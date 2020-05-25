# 76 - 119
# -*- coding: utf-8 -*-
import scrapy
from tutorial.items import TutorialItem
from urllib import parse
from tutorial.requests import SeleniumRequest
from tutorial.Spider import SeleniumSpider
from tutorial.tools import waitForXpath
from bs4 import BeautifulSoup


class InfoSpider(SeleniumSpider):
    name = 'info31'

    def start_requests(self):
        baseurl = 'http://www.jlmuseum.org/collection/show/'
        start = 1275
        end = 1303
        for i in range(start, end):
            url = baseurl + str(i) + '.html'
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        if response.status == '404':
            return
        item = TutorialItem()
        baseurl = 'http://www.jlmuseum.org'
        item['midx'] = '31'
        item['name'] = response.xpath('/html/body/div[2]/div[2]/div[2]/h1/text()').get().strip()
        if response.xpath('/html/body/div[2]/div[2]/div[2]/div/p[2]/font/text()').get() != None:
            item['text'] = response.xpath('/html/body/div[2]/div[2]/div[2]/div/p[2]/font/text()').get().strip()
        else:
            item['text'] = response.xpath('/html/body/div[2]/div[2]/div[2]/div/p[2]/text()').get().strip()
        if response.xpath('/html/body/div[2]/div[2]/div[2]/div/p[1]/font/img/@src').get() != None:
            item['pic'] = baseurl + response.xpath('/html/body/div[2]/div[2]/div[2]/div/p[1]/font/img/@src').get()
        elif response.xpath('/html/body/div[2]/div[2]/div[2]/div/p[1]/img/@src').get() != None:
            item['pic'] = baseurl + response.xpath('/html/body/div[2]/div[2]/div[2]/div/p[1]/img/@src').get()
        else:
            return
        print(item['name'])
        print(item['text'])
        print(item['pic'])
        yield item



