# -*- coding: utf-8 -*-
import scrapy
from tutorial.items import eduItem
from lxml import html


class EduSpider(scrapy.Spider):
    name = 'dmpEducation'
    # allowed_domains = ['www.dpm.org.cn']
    # start_urls = ['https://www.dpm.org.cn/activity/educations/p/1.html']
    def start_requests(self):
        for page in range(1,11):
            URL = 'https://www.dpm.org.cn/activity/educations/p/{}.html'.format(page)
            # print(URL)
            yield scrapy.Request(url=URL,callback=self.parse)

    def parse(self, response):
        index = 1
        rootUrl = 'https://www.dpm.org.cn'
        for line in response.xpath('//table/tr/td[@width="660"]'):  # 教育信息爬取
            item = eduItem()
            item['mid'] = index
            # print(item['mid'])
            item['name'] = line.xpath('./a/text()').extract()
            # print(line.xpath('./a/@href').extract())
            item['url'] = rootUrl + line.xpath('./a/@href').extract()[0]
            yield item