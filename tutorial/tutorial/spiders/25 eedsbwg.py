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
    name = 'info25'

    def start_requests(self):
        baseurl = 'http://ordosbwg.org.cn/wwdz_121925/'
        urllist = ['sq/', 'tq/', 'cq/', 'tq_121792/', 'tq_121793/', 'jyq/', 'mzww/', 'gmww/', 'qt/']
        for i in urllist:
            url = baseurl + i
            yield scrapy.Request(url=url, meta={'baseurl': url}, callback=self.parse)

    def parse(self, response):
        if response.status == '404':
            return
        # print(response.body.decode('utf-8'))
        baseurl = response.meta['baseurl']
        for i in response.xpath('/html/body/div[2]/div/div[2]/ul/li'):
            url = baseurl + i.xpath('a/p/a/@href').get()[1:]
            img = baseurl + i.xpath('a/img/@src').get()[1:]
            yield scrapy.Request(url=url, meta={'img': img}, callback=self.parse_detail)

    def parse_detail(self, response):
        item = TutorialItem()
        # print(response.body.decode('utf-8'))
        item['midx'] = '25'
        item['name'] = response.xpath('/html/body/div[2]/div/h1/text()').get()
        item['text'] = ''
        item['pic'] = response.meta['img']
        print(item['name'])
        # print(item['text'])
        print(item['pic'])
        yield item

