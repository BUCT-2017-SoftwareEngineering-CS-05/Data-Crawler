# -*- coding: utf-8 -*-
import scrapy
from tutorial.items import eduItem
from tutorial.selenium.myscrapy import SeleniumRequest
from tutorial.selenium.myscrapy import SeleniumSpider

from lxml import html


class EduSpider(SeleniumSpider):
    name = 'blj'
    # allowed_domains = ['www.dpm.org.cn']
    # start_urls = ['https://www.dpm.org.cn/activity/educations/p/1.html']
    def start_requests(self):
        for page in range(1,9):
            URL = 'http://www.balujun.cn/e/action/ListInfo/index.php?page={}&classid=5'.format(page)
            # print(URL)
            yield SeleniumRequest(url=URL,callback=self.parse)

    def parse(self, response):
        index = 23
        # / html / body / div[5] / div / div[2] / div[2] / ul / li[1]
        # print(response.xpath('/html/body/div/div/div[2]/div[2]/ul[1]/li[2]/div/a/h3'))
       # ' / html / body / div / div / div[2] / div[2] / ul[1] / li[2] / div / a / h3 / strong'
        for i in (1,5):
            for line in response.xpath('/html/body/div/div/div[2]/div[2]/ul[{}]/li'.format(i)):  # 教育信息爬取
                # print(1)
                item = eduItem()
                item['mid'] = index
                # print(item['mid'])
                item['name'] = line.xpath('./div/a/h3/strong/text()').extract()
                print(item['name'])
                # print(line.xpath('./h2/a/@href').extract())
                item['url'] = "http://www.balujun.cn"+line.xpath('./div/a/@href').extract()[0]
                print(item['url'])
                yield item