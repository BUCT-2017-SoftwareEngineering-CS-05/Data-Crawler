# -*- coding: utf-8 -*-
import scrapy
from tutorial.items import eduItem
from tutorial.selenium.myscrapy import SeleniumRequest
from tutorial.selenium.myscrapy import SeleniumSpider

from lxml import html


class EduSpider(SeleniumSpider):
    name = 'coal'
    # allowed_domains = ['www.dpm.org.cn']
    # start_urls = ['https://www.dpm.org.cn/activity/educations/p/1.html']
    def start_requests(self):
            URL = 'http://www.coalmus.org.cn/html/list_1657.html'
            # print(URL)
            yield SeleniumRequest(url=URL,callback=self.parse)
    def parse(self, response):
        index = 22
        rootUrl = 'http://www.luxunmuseum.com.cn/'
        # / html / body / div[5] / div / div[2] / div[2] / ul / li[1]
        for line in response.xpath('/html/body/div[5]/div/div[2]/div[2]/ul/li'):  # 教育信息爬取
            print(1)
            item = eduItem()
            item['mid'] = index
            # print(item['mid'])
            item['name'] = line.xpath('./h2/a/text()').extract()
            # print(line.xpath('./h2/a/@href').extract())
            item['url'] = line.xpath('./h2/a/@href').extract()[0]
            yield item