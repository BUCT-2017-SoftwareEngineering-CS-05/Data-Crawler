# 76 - 119
# -*- coding: utf-8 -*-
import scrapy
from tutorial.items import TutorialItem
from urllib import parse
from tutorial.requests import SeleniumRequest
from tutorial.Spider import SeleniumSpider
from tutorial.tools import waitForXpath
from bs4 import BeautifulSoup


class InfoSpider(scrapy.Spider):
    name = 'info50'

    def start_requests(self):
        start = 1
        end = 120
        base_url = "https://www.zjmuex.com/Collection/Details/TSGC?nid="
        for i in range(start, end):
            url = base_url + str(i)
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        if response.status == '404':
            return
        # print(response.body.decode('utf-8'))
        item = TutorialItem()
        item['midx'] = '50'
        item['name'] = response.xpath('/html/body/div[2]/div[2]/div[2]/div[3]/h3/text()').get().strip()
        t = ''
        for i in response.xpath('/html/body/div[2]/div[2]/div[3]/div/p'):
            if i.xpath('text()').get() != None:
                t = t + i.xpath('text()').get().strip()
        item['text'] = t
        item['pic'] = response.xpath('/html/body/div[2]/div[2]/div[2]/div[2]/div/a[1]/div/img/@src').get()
        print(item['name'])
        print(item['text'])
        print(item['pic'])
        yield item
