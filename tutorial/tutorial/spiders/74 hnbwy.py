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
    name = 'info74'

    def start_requests(self):
        baseurl = 'http://www.chnmus.net/sitesources/hnsbwy/page_pc/dzjp/zpjc/'
        urllist = ['qtq', 'tq', 'yq', 'cq', 'sk', 'qt']
        for i in urllist:
            url = baseurl + i + '/list1.html'
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        if response.status == '404':
            return
        baseurl = 'http://www.chnmus.net'
        html = response.body.decode('utf-8')
        suop = BeautifulSoup(html, 'html.parser')
        for i in suop.find_all('li', class_="colRightOne" ):
            s = str(i)
            url = baseurl + re.findall(r'href="(.*?)"', s)[0]
            pic = baseurl + re.findall(r'src="(.*?)"', s)[0]
            yield scrapy.Request(url=url, meta={'pic': pic}, callback=self.parse_detail)

    def parse_detail(self, response):
        html = response.body.decode('utf-8')
        soup = BeautifulSoup(html, 'html.parser')
        item = TutorialItem()
        item['midx'] = '74'
        item['name'] = soup.find_all('div', class_="cms-article-tit")[0].text.strip()
        item['pic'] = response.meta['pic']
        t = ''
        for i in soup.find_all('p', style="text-align: justify;"):
            t = t + i.text.strip()
        item['text'] = t
        print(item['name'])
        print(item['text'])
        print(item['pic'])
        yield item
