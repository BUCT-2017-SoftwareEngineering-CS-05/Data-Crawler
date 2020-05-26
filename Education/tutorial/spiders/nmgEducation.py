# -*- coding: utf-8 -*-
import scrapy
from tutorial.items import eduItem
from tutorial.selenium.myscrapy import SeleniumRequest
from tutorial.selenium.myscrapy import SeleniumSpider

from lxml import html


class EduSpider(SeleniumSpider):
    name = 'nmg'
    # allowed_domains = ['www.dpm.org.cn']
    # start_urls = ['https://www.dpm.org.cn/activity/educations/p/1.html']

    def start_requests(self):
        for page in range(1,4):
            URL = 'http://www.nmgbwy.com/byjt/index_{}.jhtml?contentId=176'.format(page)
            # print(URL)
            yield SeleniumRequest(url=URL,callback=self.parse)

    def parse(self, response):
        index = 24
        # / html / body / div[5] / div / div[2] / div[2] / ul / li[1]
        # print(response.xpath('/html/body/div/div/div[2]/div[2]/ul[1]/li[2]/div/a/h3'))
       # ' / html / body / div / div / div[2] / div[2] / ul[1] / li[2] / div / a / h3 / strong'
        for i in range(1,4,2):
            for line in response.xpath('/html/body/div[2]/div[2]/div[3]/div[3]/div[{}]'.format(i)):  # 教育信息爬取
                # print(1)
                #                         '/html/body/div[2]/div[2]/div[3]/div[3]/div[1]'
                #                         '/html/body/div[2]/div[2]/div[3]/div[3]/div[1]'
                #                         '/html/body/div[2]/div[2]/div[3]/div[3]/div[2]'
                #                         '/html/body/div[2]/div[2]/div[3]/div[3]/div[1]'
                #                         '/html/body/div[2]/div[2]/div[3]/div[3]/div[1]/div[2]'
                #                         '/html/body/div[2]/div[2]/div[3]/div[3]/div[2]'
                #                         '/html/body/div[2]/div[2]/div[3]/div[3]/div[1]'
                mid = index
                # print(item['mid'])
                name = line.xpath('./div[2]/div[1]/a/text()').extract()[0]
                print(name)
                # print(line.xpath('./h2/a/@href').extract())
                # '/ html / body / div[2] / div[2] / div[3] / div[3] / div[1] / div[2] / div[1]'
                url = line.xpath('./div[2]/div[1]/a/@href').extract()[0]
                print(url)
                yield SeleniumRequest(url=url,meta={'mid':mid,'name':name,'url':url}, callback=self.parse_details)
    def parse_details(self,response):
        item = eduItem()
        item['mid']= response.meta['mid']
        item['name'] = response.meta['name']
        item['url'] = response.meta['url']
        item['details'] = response.xpath('/html/body/div[2]/div[2]/div[4]/div/div/p[1]/text()').extract()[0]
        yield item

