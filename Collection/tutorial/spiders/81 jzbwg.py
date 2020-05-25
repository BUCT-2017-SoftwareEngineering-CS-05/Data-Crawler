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
    name = 'info81'

    def start_requests(self):
        baseurl = 'http://www.jzmsm.org/yk/cangpin/index'
        urllist = ['', '_2', '_3']
        for i in urllist:
            url = baseurl + i + '.html'
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        if response.status == '404':
            return
        baseurl = 'http://www.jzmsm.org'
        # print(response.body.decode('utf-8'))
        for i in response.xpath('/html/body/div[3]/div[1]/ul/div/ul/li'):
            url = baseurl + i.xpath('a/@href').get()
            yield scrapy.Request(url=url, callback=self.parse_detail)

    def parse_detail(self, response):
        html = response.body.decode('utf-8')
        soup = BeautifulSoup(html, 'html.parser')
        item = TutorialItem()
        # print(html)
        baseurl = 'http://www.jzmsm.org'
        item['midx'] = '81'
        item['name'] = response.xpath('/html/body/div[6]/div/div[1]/center/h1/text()').get()
        if response.xpath('/html/body/div[6]/div/div[3]/p[3]/img/@src').get() == None:
            return
        item['pic'] = baseurl + response.xpath('/html/body/div[6]/div/div[3]/p[3]/img/@src').get()
        if len(soup.find_all('p', class_="MsoNormal")) == 0:
            return
        item['text'] = soup.find_all('p', class_="MsoNormal")[0].text.strip()
        print(item['name'])
        print(item['text'])
        print(item['pic'])
        yield item
