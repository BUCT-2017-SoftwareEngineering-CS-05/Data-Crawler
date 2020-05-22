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
    name = 'info73'

    def start_requests(self):
        baseurl = 'http://www.wfsbwg.com/content/?'
        start = 400
        end = 424
        for i in range(start, end):
            url = baseurl + str(i) + '.html'
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        if response.status == '404':
            return
        html = response.body.decode('utf-8')
        # print(html)
        soup = BeautifulSoup(html, 'html.parser')
        baseurl = 'http://www.wfsbwg.com'
        item = TutorialItem()
        item['midx'] = '73'
        item['name'] = response.xpath('/html/body/div[7]/div[2]/div[2]/h1/text()').get()
        item['text'] = '无'
        if len(soup.find_all('a', id='MagicZoom')) == 0:
            return
        s = str(soup.find_all('a', id='MagicZoom')[0])
        item['pic'] = baseurl + re.findall(r'href="(.*?)"', s)[0]
        print(item['name'])
        print(item['text'])
        print(item['pic'])
        yield item
