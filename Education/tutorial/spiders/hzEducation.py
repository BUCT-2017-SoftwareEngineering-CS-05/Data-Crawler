# -*- coding: utf-8 -*-
import scrapy
from tutorial.items import eduItem
from tutorial.selenium.myscrapy import SeleniumRequest
from tutorial.selenium.myscrapy import SeleniumSpider

from lxml import html


class EduSpider(scrapy.Spider):
    name = 'hz'
    # allowed_domains = ['www.dpm.org.cn']
    # start_urls = ['https://www.dpm.org.cn/activity/educations/p/1.html']

    def start_requests(self):
        data ={'__VIEWSTATE':'nx/w/eOnM+KfVPtVGVAjcTuLc/V307t8Q+KVE5z4z6fHoZFpcDuEdLT5/MakxzqDO1G6oQHoPfGN8t/+KzRyfv20Npq0I4Mx6ugQe7xDURX/kEOJB3Cy8cB321iUSlLbHPNKrVx1hBtsIuESt6vZQ9gINPDs16cSxsOg1xhX9nK52kwlImLCaPhQLbjsZZM26iyDK7X6Dyd/SynHkJBLjniF/0YyOjUQ9asergrziSJP6TnI3ykYi0Lwqep0gDC584u6fbo6xTKVkw7fTKQDj0TODytUU92IXu4RtsqPQ4SkgwONperZ8Lfw8zSFNz2BH7zCNiQYd32AOtGAkAZRKPgVJ/mgUoI/5H0bnUsGe6BIclIu3u4nBvv+HAO1nKx2dzhdHO1qXSmOxebHWwASRux+JUUnjwFsp5mND8eOcUmoDZ/HOe7bEBpvGo1kbGLfAs0dmfLupmyOt41FAVEZL80glMUPN6WOJjyxV7K7U58p8vWNwpERGYBkadcnrJvpE0YOjPmU/Xg7MVK0h+f7ci0D0xL+N/q4hSYHPxgKfJ81jyO+sA4X+azEx53ouSt1Ru3/BMPDSXlnzRShpZ3fxM4JbWlv4xozxiTlUTwrZbm03XRh5zqyssTWn86hd0D7q7TOl/7PVvdvuYQynzevFrErjOZ2LUHVHiW9AX+LfEYQr988BeEe0NREKinFkDcH6glvYt/wLB9XMPIYDXEEvaZgQM8yqGZYCKnxd386GIyL/Swq2ZCn4AdKP4K3kCLt/NQn0r/ayxe/qaQcKF0vh7FsyUGNPepvPmY0MWk1DG1bXiJg8YMBOLudA4+HtJ+vtvRe77zPDxS2aFVrBWtOddBYURC3xSdb+9FktqOPjFEr8jq2LdlDj/WhX0jG20gZxUFh90N1U0OFkZGw81rr9hmhcrCbcvRQw9KVdzUKQrsiVib3gfyIYA68HJkgNUsCjkRxxgeoywitW55BJBt+fzIjZca55Ak3kYyCjQUcuGH8RMW9fa9JCNN48sL9iSOT+6MmPX2/N9/OK3KdEzyfA/FU10NGXSuOH+7a51Nhor4vriUoNv4kIp7IahiYQIeRQ3b9Qg==',
               '__VIEWSTATEGENERATOR':' D45CB6B7',
               '__EVENTTARGET': 'AspNetPager'}
        for page in range(1,2):
            URL = 'http://www.hzmuseum.com/missionlist.aspx?cid=17?__VIEWSTATE={}&__VIEWSTATEGENERATOR={}&__EVENTTARGET={}&__EVENTARGUMENT={}'.format(data['__VIEWSTATE'],data['__VIEWSTATEGENERATOR'],data['__EVENTTARGET'],page)
        # print(URL)
            yield SeleniumRequest(url=URL,method='POST', callback=self.parse, dont_filter=True)


    def parse(self, response):
        index = 54
        # / html / body / div[5] / div / div[2] / div[2] / ul / li[1]
        # print(response.xpath('/html/body/div/div/div[2]/div[2]/ul[1]/li[2]/div/a/h3'))
       # ' / html / body / div / div / div[2] / div[2] / ul[1] / li[2] / div / a / h3 / strong'
       #  print(response.xpath('/html/body/form/div[3]/table/tr/td/table/tr[3]/td/table/tr[3]/td/table/tr/td[3]/div/span[2]/div/table[1]/tr[1]'))
        for line in response.xpath('/html/body/form/div[5]/div[2]/div[2]/div/ul/li'):  # 教育信息爬取
            # print(1)
            item = eduItem()
            item['mid'] = index
            # print(item['mid'])
            #                             '/html/body/div[3]/div/div/ul/li[17]/a'
            item['name'] = line.xpath('./div[2]/p/a/text()').extract()[0]
            print(item['name'])
            # print(line.xpath('./h2/a/@href').extract())
            item['url'] = "http://www.hzmuseum.com/"+line.xpath('./div[2]/p/a/@href').extract()[0]
            print(item['url'])
            # item['details'] = line.xpath('./span/text()').extract()[0].strip()
            yield item

