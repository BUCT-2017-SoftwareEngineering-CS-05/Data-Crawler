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
    name = 'info61'

    def start_requests(self):
        baseurl = 'http://www.mtybwg.org.cn/cangpin/show/'
        start = 600
        end = 701
        for i in range(start, end):
            url = baseurl + str(i) + '.aspx'
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        if response.status == '404':
            return
        # html = response.body.decode('utf-8')
        # suop = BeautifulSoup(html, 'html.parser')
        item = TutorialItem()
        item['midx'] = '61'
        html = response.body.decode('utf-8')
        suop = BeautifulSoup(html, 'html.parser')
        item['name'] = response.xpath('/html/body/div[2]/div[2]/ul/div[2]/h1/text()').get().strip()
        item['text'] = suop.find_all('ul', class_='con')[0].text.strip().replace('\n', '').replace('\r', '').replace('\t', '')
        baseurl = 'http://www.mtybwg.org.cn'
        item['pic'] = baseurl + response.xpath('/html/body/div[2]/div[2]/ul/div[1]/div[1]/li/a/img/@src').get()
        print(item['name'])
        print(item['text'])
        print(item['pic'])
        yield item
