# -*- coding: utf-8 -*-
import scrapy
from tutorial.items import eduItem
from tutorial.selenium.myscrapy import SeleniumRequest
from tutorial.selenium.myscrapy import SeleniumSpider

from lxml import html


class EduSpider(SeleniumSpider):
    name = 'sh'
    # allowed_domains = ['www.dpm.org.cn']
    # start_urls = ['https://www.dpm.org.cn/activity/educations/p/1.html']

    def start_requests(self):
        URL = 'https://www.shanghaimuseum.net/education/show/show.action'
        # print(URL)
        yield SeleniumRequest(url=URL, callback=self.parse, dont_filter=True)


    def parse(self, response):
        index = 38
        # / html / body / div[5] / div / div[2] / div[2] / ul / li[1]
        # print(response.xpath('/html/body/div/div/div[2]/div[2]/ul[1]/li[2]/div/a/h3'))
       # ' / html / body / div / div / div[2] / div[2] / ul[1] / li[2] / div / a / h3 / strong'
        for line in response.xpath('/html/body/div[6]/div[2]/div[1]/ul/li'):  # 教育信息爬取
            # print(1)
            item = eduItem()
            item['mid'] = index
            # print(item['mid'])
            #                             '/html/body/div[3]/div/div/ul/li[17]/a'
            item['name'] = line.xpath('./div[2]/div[1]/dl/dt/text()').extract()[0]
            print(item['name'])
            # print(line.xpath('./h2/a/@href').extract())
            item['url'] = "https://www.shanghaimuseum.net/education/" + line.xpath('./div[1]/div[2]/a/@href').extract()[0]
            print(item['url'])
            item['details'] = line.xpath('./div[2]/div[1]/dl/dd[1]/p/text()').extract()[0].strip()
            yield item

