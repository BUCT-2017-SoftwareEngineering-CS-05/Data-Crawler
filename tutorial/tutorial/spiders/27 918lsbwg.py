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
    name = 'info27'

    def start_requests(self):
        baseurl = 'http://www.918museum.org.cn/index.php/article/listarticle/pid/126/rel/thumb/sidebar/sidebar?currentPage='
        start = 1
        end = 17
        for i in range(start, end):
            url = baseurl + str(i)
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        if response.status == '404':
            return
        # print(response.body.decode('utf-8'))
        baseurl = 'http://www.918museum.org.cn'
        for i in response.xpath('/html/body/div[3]/div/div/div[1]/div/div[2]/div[1]/div'):
            url = baseurl + i.xpath('a/@href').get()
            # print(url)
            yield SeleniumRequest(url=url, callback=self.parse_detail)

    def parse_detail(self, response):
        item = TutorialItem()
        # print(response.body.decode('utf-8'))
        # print(response.body.decode('utf-8'))
        baseurl = 'http://www.918museum.org.cn'
        item['midx'] = '27'
        item['name'] = response.xpath('/html/body/div[3]/div/div/div[1]/div/div[2]/div/div[1]/text()').get().strip()
        item['text'] = response.xpath('/html/body/div[3]/div/div/div[1]/div/div[2]/div/div[3]/div[2]/p/text()').get()
        item['pic'] = ''
        if response.xpath('/html/body/div[3]/div/div/div[1]/div/div[2]/div/div[3]/div[1]/div/div/div[1]/ul/li[2]/a/img/@src').get() != None:
            item['pic'] = baseurl + response.xpath('/html/body/div[3]/div/div/div[1]/div/div[2]/div/div[3]/div[1]/div/div/div[1]/ul/li[2]/a/img/@src').get()
        elif response.xpath('/html/body/div[3]/div/div/div[1]/div/div[2]/div/div[3]/div[1]/div/div/div[1]/ul/li/a/@href').get() != None:
            item['pic'] = baseurl + response.xpath('/html/body/div[3]/div/div/div[1]/div/div[2]/div/div[3]/div[1]/div/div/div[1]/ul/li/a/@href').get()
        if item['pic'] == None or item['name'] == None or item['text'] == None:
            return
        print(item['name'])
        print(item['text'])
        print(item['pic'])
        yield item

