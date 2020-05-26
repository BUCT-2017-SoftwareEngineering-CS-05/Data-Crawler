# -*- coding: utf-8 -*-
import scrapy
from tutorial.items import eduItem
from lxml import html


class EduSpider(scrapy.Spider):
    name = 'gmcEducation'
    def start_requests(self):
        for page in range(1,3):
            URL = 'http://www.gmc.org.cn/knowledge/p/{}.html'.format(page)
            # print(URL)
            yield scrapy.Request(url=URL,callback=self.parse)

    def parse(self, response):
        index = 3
        rootUrl = 'http://www.gmc.org.cn'
        for line in response.xpath('/html/body/div[4]/div/div/div[3]/div[1]/div'):  # 教育信息爬取
            item = eduItem()
            item['mid'] = index
            # print(item['mid'])
            item['name'] = line.xpath('./a/div[1]/div[1]/text()').extract()
            # print(line.xpath('./a/div[1]/div[1]/text()').extract())
            # print(line.xpath('./a/@href').extract())
            item['url'] = rootUrl + line.xpath('./a/@href').extract()[0]
            yield item