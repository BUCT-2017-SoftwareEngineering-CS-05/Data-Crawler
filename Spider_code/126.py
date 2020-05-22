#-*- codeing = utf-8 -*-
#@Time : 2020/5/18 15:47
#@Author : 张文天
#@File : 8.py
#@Software: PyCharm
#-*- codeing = utf-8 -*-
#@Time : 2020/5/18 13:41
#@Author : 张文天
#@File : 7.py
#@Software: PyCharm
#-*- codeing = utf-8 -*-
#@Time : 2020/5/18 12:35
#@Author : 张文天
#@File : 3.py
#@Software: PyCharm
#-*- codeing = utf-8 -*-
#@Time : 2020/5/17 21:53
#@Author : 张文天
#@File : 2.py
#@Software: PyCharm
#-*- codeing = utf-8 -*-
#@Time : 2020/5/16 20:57
#@Author : 张文天
#@File : liaoningshengmuseum.py
#@Software: PyCharm
#-*- codeing = utf-8 -*-
#@Time : 2020/4/24 19:46
#@Author : 张文天
#@File : suzhoumuseum.py
#@Software: PyCharm


from bs4 import BeautifulSoup
import re
import urllib.request,urllib.error
import pymysql
from lxml import etree




def main():
    baseurl = "http://www.bmnh.org.cn/zljs/jbcl/1/zljs/index.shtml"

    datadict = getData(baseurl)
    print(datadict)

def savedata(datadict):
    conn = pymysql.connect(
        host='cdb-3lehih0k.cd.tencentcdb.com',
        port= 10090,
        user='CS1705museum',
        passwd='CS1705museum',
        db='museum',
        charset='utf8'
    )
    cursor = conn.cursor()
    sql = 'insert into Exhibition(midex,ename,eintro) values (%s,%s,%s)'
    data = (datadict['midex'], datadict['ename'], datadict['eintro'])
    cursor.execute(sql,data)
    conn.commit()
    cursor.close()
    conn.close()


replaceTag = re.compile(r'<.*?>')
findIntro = re.compile(r'<div class="p">(.*?)</div>')
findSrc = re.compile(r'<a href="(.*?)">')
findName = re.compile(r'<h1>\s+(.*)\s+</h1>')

def getSrc(url):
    urllist = []
    baseurl_ = 'https://www.nxbwg.com'
    html = askUrl(url)

    html = html.replace('<br />', ' ').replace('<br>', ' ')
    soup = BeautifulSoup(html, "html.parser")
    for item in soup.find_all('div',class_='article-list'):
        # print(item)
        src = re.findall(findSrc,str(item))
        # print(src)
        for item in src:
            urllist.append(baseurl_+str(item).replace('amp;','').replace(';','&'))
    urllist = sorted(set(urllist),key=urllist.index)
    # print(urllist)
    return urllist

def getData(baseurl):
    datadict = {}
    urllist = []
    # for i in range(1,5):
    urllist = ['http://www.qhmuseum.cn/#/exhibitioninfoDetials/thematicDetials?id=7&t=%25E3%2580%258A%25E5%25A6%2599%25E5%25A2%2583%25E7%25A5%259E%25E9%259F%25B5%25E2%2580%2594%25E2%2580%2594%25E8%2597%258F%25E4%25BC%25A0%25E4%25BD%259B%25E6%2595%2599%25E5%2594%2590%25E5%258D%25A1%25E8%2589%25BA%25E6%259C%25AF%25E5%25B1%2595%25E3%2580%258B','http://www.qhmuseum.cn/#/exhibitioninfoDetials/thematicDetials?id=6&t=%25E3%2580%258A%25E5%25A6%2599%25E7%259B%25B8%25E5%25BA%2584%25E4%25B8%25A5%25E2%2580%2594%25E2%2580%2594%25E8%2597%258F%25E4%25BC%25A0%25E4%25BD%259B%25E6%2595%2599%25E9%2587%2591%25E9%2593%259C%25E9%2580%25A0%25E5%2583%258F%25E8%2589%25BA%25E6%259C%25AF%25E5%25B1%2595%25E3%2580%258B']
    # print(urllist)
    for url in urllist:
        # print(url)
        html = askUrl(url)
        if html == -1:
            continue
        html = html.replace('<br />',' ').replace('<br>',' ')
        soup = BeautifulSoup(html,"html.parser")
        # print(soup)
        datadict['midex'] = '126'
        i = 0
        for item in soup.find_all('div',style="text-align: center; font-size: 20px; font-weight: bold; line-height: 3.125rem;"):
            print(item)
            datadict['ename'] = str(item.text).replace('\r','').replace('\n','').strip()
            datadict['ename'] = datadict['ename'].replace('名称：','').strip()
            print(datadict['ename'])
            intro = soup.find_all('div',style="position: relative; display: block;")[i]
            datadict['eintro'] = str(intro.text).replace('\n','').replace('\xa0','').replace('\u3000','').replace('\r','').replace('\t','')
            datadict['eintro'] = datadict['eintro'].replace(datadict['ename'],'').replace('是','').strip()
            print(datadict['eintro'])
            # i = i+1
            # savedata(datadict)
    return datadict


def askUrl(url):
    head = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36"}
    request = urllib.request.Request(url,headers=head)
    try:
        response = urllib.request.urlopen(request)
        html = response.read().decode('utf-8')

        # print(html)

    except Exception as e:
        return -1
        if hasattr(e,"code"):
            print(e.code)
        if hasattr(e,"reason"):
            print(e.reason)

    return html




if __name__ == "__main__":
    main()












