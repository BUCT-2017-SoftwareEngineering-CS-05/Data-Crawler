# -*- coding: utf-8 -*-
import scrapy
from tutorial.items import eduItem
from lxml import html


class EduSpider(scrapy.Spider):
    name = 'capEducation'
    # allowed_domains = ['www.dpm.org.cn']
    # start_urls = ['https://www.dpm.org.cn/activity/educations/p/1.html']
    def start_requests(self):
        for page in range(2,7):
            URL = 'http://www.capitalmuseum.org.cn/xsyj/wljt.htm'
            # print(URL)
            yield scrapy.Request(url=URL,callback=self.parse,dont_filter=True)

    def parse(self, response):
        index = 7
        rootUrl = 'http://www.capitalmuseum.org.cn/xsyj/'
        print(response.xpath('/html/body/table[1]/tr[2]/td/table/tr/td/table[1]/tr[1]/td/div/a/span'))
        # for line in response.xpath('/html/body/table[2]/tr/td[2]/table/tr[4]/td/table[@width="85%"]'):  # 教育信息爬取
        #     item = eduItem()
        #     item['mid'] = index
        #     # print(item['mid'])
        #     item['name'] = line.xpath('./tr/td/a/text()').extract()
        #     # print(line.xpath('./a/@href').extract())
        #     item['url'] = rootUrl + line.xpath('./tr/td/a/@href').extract()[0]
        #     yield item