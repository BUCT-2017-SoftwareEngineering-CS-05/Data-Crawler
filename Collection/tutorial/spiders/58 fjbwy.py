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
    name = 'info58'

    def start_requests(self):
        url = 'http://museum.fjsen.com/node_167182.htm'
        yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        if response.status == '404':
            return
        html = response.body.decode('utf-8')
        suop = BeautifulSoup(html, 'html.parser')
        for i in suop.find_all('ul', class_="list_page"):
            urllist = re.findall(r'<a href="(.*?)" target="_blank">', str(i))
            namelist = re.findall(r'target="_blank">(.*?)</a>', str(i))
            if len(urllist) != 0:
                for i in range(5):
                    yield scrapy.Request(url=urllist[i], meta={'name': namelist[i]}, callback=self.parse_detail)

    def parse_detail(self, response):
        item = TutorialItem()
        item['midx'] = '58'
        html = response.body.decode('utf-8')
        suop = BeautifulSoup(html, 'html.parser')
        item['name'] = response.meta['name']
        t = ''
        for i in response.xpath('//*[@id="new_message_id"]/p'):
            if i.xpath('text()').get() != None:
                t = t + i.xpath('text()').get().strip()
        item['text'] = t
        s = str(suop.find_all('td', id="new_message_id")[0])
        item['pic'] = re.findall(r'src="(.*?)"', s)[0]
        print(item['name'])
        print(item['text'])
        print(item['pic'])
        yield item
