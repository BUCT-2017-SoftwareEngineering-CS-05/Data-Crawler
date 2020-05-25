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
    name = 'info22'

    def start_requests(self):
        start_page = 1556
        end_page = 1562
        base_url = "http://www.coalmus.org.cn/html/list_"
        for i in range(start_page, end_page):
            url = base_url + str(i) + '.html'
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        if response.status == '404':
            return
        # print(response.body.decode('utf-8'))
        for i in response.xpath('/html/body/div[5]/div[2]/div[2]/ul/li'):
            url = i.xpath('div[1]/a/@href').get()
            yield SeleniumRequest(url=url, callback=self.parse_detail)

    def parse_detail(self, response):
        item = TutorialItem()
        # print(response.body.decode('utf-8'))
        item['midx'] = '22'
        item['name'] = response.xpath('/html/body/div[5]/div[2]/div[1]/text()').get()
        t = ''
        for i in response.xpath('/html/body/div[5]/div[2]/div[5]/div[3]/p'):
            if i.xpath('text()').get() != None:
                t = t + i.xpath('text()').get().strip()
        item['text'] = t
        item['pic'] = response.xpath('/html/body/div[5]/div[2]/div[5]/div[1]/div/div/img/@src').get()
        print(item['name'])
        print(item['text'])
        print(item['pic'])
        yield item

