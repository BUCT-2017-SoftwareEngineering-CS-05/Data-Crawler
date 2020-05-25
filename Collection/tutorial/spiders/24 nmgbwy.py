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
    name = 'info24'

    def start_requests(self):
        urllist = ['http://www.nmgbwy.com/lsww/index.jhtml?contentId=190',
                   'http://www.nmgbwy.com/mzww/index.jhtml?contentId=191',
                   'http://www.nmgbwy.com/gswhs/index.jhtml?contentId=192']
        for url in urllist:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        if response.status == '404':
            return
        # print(response.body.decode('utf-8'))
        baseurl = 'http://www.nmgbwy.com'
        for i in response.xpath('/html/body/div[2]/div[2]/div[3]/div/div/div[2]/div'):
            url = i.xpath('div[1]/a/@href').get()
            img = baseurl + i.xpath('div[1]/img/@src').get()
            yield scrapy.Request(url=url, meta={'img': img}, callback=self.parse_detail)

    def parse_detail(self, response):
        item = TutorialItem()
        # print(response.body.decode('utf-8'))
        item['midx'] = '24'
        item['name'] = response.xpath('/html/body/div[2]/div[2]/div[3]/div/div/div[2]/div[2]/div/div[1]/span/text()').get()
        t = ''
        for i in response.xpath('/html/body/div[2]/div[2]/div[3]/div/div/div[2]/div[2]/div/div[2]/p'):
            if i.xpath('text()').get() != None:
                t = t + i.xpath('text()').get().strip()
        item['text'] = t
        item['pic'] = response.meta['img']
        print(item['name'])
        print(item['text'])
        print(item['pic'])
        yield item

