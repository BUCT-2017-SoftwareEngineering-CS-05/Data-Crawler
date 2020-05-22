#-*- codeing = utf-8 -*-
#@Time : 2020/4/24 19:46
#@Author : 张文天
#@File : suzhoumuseum.py
#@Software: PyCharm


from bs4 import BeautifulSoup
import re
import urllib.request,urllib.error
import pymysql




def main():
    baseurl = "http://www.hebeimuseum.org.cn/channels/13.html"

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
findSrc = re.compile(r'<img src=(.*)>')

def getData(baseurl):
    datadict = {}
    html = askUrl(baseurl)
    html = html.replace('<br />',' ').replace('<br>',' ')
    soup = BeautifulSoup(html,"html.parser")
    # print(soup)
    datadict['midex'] = '18'
    i = 0
    soup = soup.find_all('div',class_="list")
    soup = BeautifulSoup(str(soup),"html.parser")
    for item in soup.find_all('a',target="_blank"):
        # print(item)
        if item.text == '[详细]':
            continue
        if item.text == '':
            continue
        datadict['ename'] = str(item.text).replace('\n','').strip()
        print(datadict['ename'])
        intro = soup.find_all('div',class_="text")[i]
        datadict['eintro'] = str(intro.text).replace('\n','').replace('\xa0','').replace('\u3000','').replace('\r','').strip()
        print(datadict['eintro'])
        i = i+1
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












