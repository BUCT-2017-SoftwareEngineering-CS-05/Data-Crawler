# -*- coding: utf-8 -*-
import scrapy
from tutorial.items import eduItem
from lxml import html


class EduSpider(scrapy.Spider):
    name = 'hd'
    # allowed_domains = ['www.dpm.org.cn']
    # start_urls = ['https://www.dpm.org.cn/activity/educations/p/1.html']
    def start_requests(self):
        for page in (1,3):
            URL = 'http://www.hdmuseum.org/newslist.asp?cd=51&page={}'.format(page)
            # print(URL)
            yield scrapy.Request(url=URL,callback=self.parse)

    def parse(self, response):
        index = 20
        rootUrl = 'http://www.luxunmuseum.com.cn/'
        for i in range(1,12,2):
            for line in response.xpath('/html/body/table[4]/tr/td[3]/table/tr/td/table[2]/tr/td/table/tr/td/table/tr/td/table[1]/tr[1]/td{}'.format(i)):  # 教育信息爬取
                item = eduItem()
                item['mid'] = index
                # print(item['mid'])
                item['name'] = line.xpath('./a/@title').extract()
                # print(line.xpath('./a/@href').extract())
                item['url'] = rootUrl + line.xpath('./div[2]/a/@href').extract()[0]
                yield item