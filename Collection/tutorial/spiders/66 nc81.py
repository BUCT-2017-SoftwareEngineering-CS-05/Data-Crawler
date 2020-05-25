# 76 - 119
# -*- coding: utf-8 -*-
import scrapy
from tutorial.items import TutorialItem
from urllib import parse
from tutorial.requests import SeleniumRequest
from tutorial.Spider import SeleniumSpider
from tutorial.tools import waitForXpath
from bs4 import BeautifulSoup
import re


class InfoSpider(scrapy.Spider):
    name = 'info66'

    def start_requests(self):
        baseurl = 'http://www.81-china.com/collect/60/'
        start = 15
        end = 19
        for i in range(start, end):
            url = baseurl + str(i) + '.html'
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        if response.status == '404':
            return
        html = response.body.decode('utf-8')
        # print(html)
        soup = BeautifulSoup(html, 'html.parser')
        item = TutorialItem()
        item['midx'] = '66'
        baseurl = 'http://www.81-china.com'
        for i in response.xpath('/html/body/div/div[5]/div[3]/div[2]/ul/li'):
            item['name'] = i.xpath('div[2]/h3/a/text()').get()
            item['text'] = i.xpath('div[2]/p/text()').extract()[1].strip()
            s = str(soup.find_all('img')[0])
            item['pic'] = baseurl + i.xpath('div[1]/a/img/@src').get()
            print(item['name'])
            print(item['text'])
            print(item['pic'])
            yield item
