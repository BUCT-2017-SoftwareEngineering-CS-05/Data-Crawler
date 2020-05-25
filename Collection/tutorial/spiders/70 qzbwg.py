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
    name = 'info70'

    def start_requests(self):
        baseurl = 'http://bowuguan.qingzhou.gov.cn/cp/'
        urllist = ['tq/', 'cq/', 'sh/', 'yq/', 'qtq/', 'sk/', 'lxs/', 'qt/']
        for i in urllist:
            url = baseurl + i
            yield scrapy.Request(url=url, meta={'baseurl': url[:-1]}, callback=self.parse)

    def parse(self, response):
        if response.status == '404':
            return
        baseurl = response.meta['baseurl']
        # print(response.body.decode('utf-8'))
        for i in response.xpath('/html/body/div[3]/table/tbody/tr/td/table/tbody//td'):
            if len(i.xpath('table/tbody/tr[1]/td/table/tbody/tr/td/div/a/@href').extract()) != 0:
                url = baseurl + i.xpath('table/tbody/tr[1]/td/table/tbody/tr/td/div/a/@href').get()[1:]
                pic = baseurl + i.xpath('table/tbody/tr[1]/td/table/tbody/tr/td/div/a/img/@src').get()[1:]
                yield scrapy.Request(url=url, meta={'pic': pic}, callback=self.parse_detail)

    def parse_detail(self, response):
        html = response.body.decode('utf-8')
        soup = BeautifulSoup(html, 'html.parser')
        item = TutorialItem()
        item['midx'] = '70'
        item['name'] = response.xpath('/html/body/div[2]/table/tbody/tr[3]/td/text()').get()
        item['pic'] = response.meta['pic']
        item['text'] = soup.find_all('div', class_="TRS_Editor")[0].text.strip().replace('\n', '').replace('\r', '').replace('\t', '')
        print(item['name'])
        print(item['text'])
        print(item['pic'])
        yield item
