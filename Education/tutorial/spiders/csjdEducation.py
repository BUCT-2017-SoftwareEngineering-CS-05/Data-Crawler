# -*- coding: utf-8 -*-
import scrapy
from tutorial.items import eduItem
from tutorial.selenium.myscrapy import SeleniumRequest
from tutorial.selenium.myscrapy import SeleniumSpider

from lxml import html


class EduSpider(SeleniumSpider):
    name = 'csjd'
    # allowed_domains = ['www.dpm.org.cn']
    # start_urls = ['https://www.dpm.org.cn/activity/educations/p/1.html']

    def start_requests(self):
        for page in range(1, 7):
            URL = 'http://www.chinajiandu.cn/News/List/whjt?page={}'.format(page)
        # print(URL)
            yield SeleniumRequest(url=URL, callback=self.parse, dont_filter=True)
    def parse(self, response):
        index = 87
        # / html / body / div[5] / div / div[2] / div[2] / ul / li[1]
        # print(response.xpath('/html/body/div/div/div[2]/div[2]/ul[1]/li[2]/div/a/h3'))
       # ' / html / body / div / div / div[2] / div[2] / ul[1] / li[2] / div / a / h3 / strong'
       #  print(response.xpath('/html/body/form/div[3]/table/tr/td/table/tr[3]/td/table/tr[3]/td/table/tr/td[3]/div/span[2]/div/table[1]/tr[1]'))

        # '/html/body/div[2]/table/tbody/tr[4]/td/table/tbody/tr[1]/td[1]/a/span'
        for i in range(1,2):
            if i == 8 :continue
            # print(response.xpath('/html/body/div[4]/div/div/ul/li'))
            for line in response.xpath('/html/body/div[2]/div/ul/li'):  # 教育信息爬取
                print(1)
                # print(1)
                item = eduItem()
                item['mid'] = index
                # print(item['mid'])
                #                             '/html/body/div[3]/div/div/ul/li[17]/a'
                # '/html/body/div[3]/div/div[3]/div[1]/ul/li[1]/div[3]/a[1]/h3'
                # '/td/table/tbody/tr/td[1]/a'
                # '/html/body/div[1]/div[8]/div/div/div[2]/div[2]/div[2]/table/tbody/tr/td[2]/div[1]/div[2]/div[3]/div[2]/div/div[1]/div[1]/table/tbody/tr/td/a'
                # '/html/body/div[1]/div[8]/div/div/div[2]/div[2]/div[2]/table/tbody/tr/td[2]/div[1]/div[2]/div[3]/div[2]/div/div[1]/div[1]/table/tbody/tr/td/a/text()'
                item['name'] = line.xpath('./a/div[1]/h3/text()').extract()[0].strip()
                # '/html/body/div[6]/div[4]/div[1]/div[9]/div/table/tbody/tr[1]/td/table[9]/tbody/tr[1]/td[2]/a/b'
                print(item['name'])
                # print(line.xpath('./h2/a/@href').extract())
                # '/html/body/div[2]/table/tbody/tr[4]/td/table/tbody/tr[1]/td[1]/a/span'
                item['url'] = "http://www.chinajiandu.cn"+line.xpath('./a/@href').extract()[0]
                print(item['url'])
                # item['details'] = line.xpath('./span/text()').extract()[0].strip()
                yield item


