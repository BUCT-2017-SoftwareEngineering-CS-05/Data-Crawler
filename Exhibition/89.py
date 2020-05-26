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
findSrc = re.compile(r'<a href="(.*?)" title=".*?">')
findName = re.compile(r'<h2>(.*)</h2>')

def getSrc(url):
    urllist = []
    baseurl_ = 'https://www.gznywmuseum.org'
    html = askUrl(url)

    html = html.replace('<br />', ' ').replace('<br>', ' ')
    soup = BeautifulSoup(html, "html.parser")
    for item in soup.find_all('div',class_='gg-list-content'):
        src = re.findall(findSrc,str(item))
        # print(src)
        for item in src:
            urllist.append(baseurl_+str(item))
    urllist = sorted(set(urllist),key=urllist.index)
    # print(urllist)
    return urllist

def getData(baseurl):
    datadict = {}
    urllist = []
    for i in range(1,4):
        urllist = getSrc("https://www.gznywmuseum.org/zlgg/index_%d.jhtml"%i)
        # print(urllist)
        for url in urllist:
            # print(url)
            html = askUrl(url)
            if html == -1:
                continue
            html = html.replace('<br />',' ').replace('<br>',' ')
            soup = BeautifulSoup(html,"html.parser")
            # print(soup)
            datadict['midex'] = '89'
            i = 0
            for item in soup.find_all('p',class_="nbsp-sp-detail-title"):
                # print(item)
                datadict['ename'] = str(item.text).replace('\r','').replace('\n','').strip()
                datadict['ename'] = datadict['ename'].replace('名称：','').replace('返回','').strip()
                print(datadict['ename'])
                intro = soup.find_all('div',class_="nbsp-sp-detail-view-middle")[i]
                datadict['eintro'] = str(intro.text).replace('\n','').replace('\xa0','').replace('\u3000','').replace('\r','').replace('\t','')
                datadict['eintro'] = datadict['eintro'].replace(datadict['ename'],'')
                print(datadict['eintro'])
                # i = i+1
                savedata(datadict)
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












