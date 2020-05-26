# -*- coding: utf-8 -*-
import scrapy
from tutorial.items import eduItem
from tutorial.selenium.myscrapy import SeleniumRequest
from tutorial.selenium.myscrapy import SeleniumSpider

from lxml import html


class EduSpider(scrapy.Spider):
    name = 'jgs'
    # allowed_domains = ['www.dpm.org.cn']
    # start_urls = ['https://www.dpm.org.cn/activity/educations/p/1.html']

    def start_requests(self):
        for page in range(1,4):
            URL = 'http://www.jgsgmbwg.com/news.php?cid=72&page={}'.format(page)
        # print(URL)
            yield SeleniumRequest(url=URL, callback=self.parse, dont_filter=True)
    def parse(self, response):
        index = 63
        # / html / body / div[5] / div / div[2] / div[2] / ul / li[1]
        # print(response.xpath('/html/body/div/div/div[2]/div[2]/ul[1]/li[2]/div/a/h3'))
       # ' / html / body / div / div / div[2] / div[2] / ul[1] / li[2] / div / a / h3 / strong'
       #  print(response.xpath('/html/body/form/div[3]/table/tr/td/table/tr[3]/td/table/tr[3]/td/table/tr/td[3]/div/span[2]/div/table[1]/tr[1]'))
        for line in response.xpath('/html/body/div[1]/div[5]/div[2]/div/ul/li'):  # 教育信息爬取
            # print(1)
            item = eduItem()
            item['mid'] = index
            # print(item['mid'])
            #                             '/html/body/div[3]/div/div/ul/li[17]/a'
            # '/html/body/div[3]/div/div[3]/div[1]/ul/li[1]/div[3]/a[1]/h3'
            # '/td/table/tbody/tr/td[1]/a'
            item['name'] = line.xpath('./span[3]/a/text()').extract()[0]
            print(item['name'])
            # print(line.xpath('./h2/a/@href').extract())
            item['url'] = "http://www.jgsgmbwg.com/"+line.xpath('./span[3]/a/@href').extract()[0]
            print(item['url'])
            # item['details'] = line.xpath('./span/text()').extract()[0].strip()
            yield item

