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
    name = 'info45'

    def start_requests(self):
        start = 1
        end = 45
        base_url = "http://www.ntmuseum.com/colunm2/col1/list_17_"
        for i in range(start, end):
            url = base_url + str(i) + '.html'
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        if response.status == '404':
            return
        # print(response.body.decode('utf-8'))
        for i in response.xpath('/html/body/section[2]/div[3]/div[1]/ul/li'):
            url = i.xpath('a/@href').get()
            pic = i.xpath('a/img/@src').get()
            yield scrapy.Request(url=url, meta={'pic': pic}, callback=self.parse_detail)

    def parse_detail(self, response):
        baseurl = 'http://www.19371213.com.cn/collection/zdwwjs/201811'
        item = TutorialItem()
        item['midx'] = '45'
        item['name'] = response.xpath('/html/body/section[2]/div[3]/div/div/ul/li[1]/text()').get().strip()
        item['pic'] = response.meta['pic']
        html = response.body.decode('utf-8')
        suop = BeautifulSoup(html, 'html.parser')
        item['text'] = suop.find_all('li', class_="list_all")[0].text.strip().replace('\n', '').replace('\xa0', '')
        print(item['name'])
        print(item['text'])
        print(item['pic'])
        yield item

