#-*- codeing = utf-8 -*-
#@Time : 2020/5/18 16:59
#@Author : 张文天
#@File : 15.py
#@Software: PyCharm
#-*- codeing = utf-8 -*-
#@Time : 2020/5/18 16:23
#@Author : 张文天
#@File : 12.py
#@Software: PyCharm
#-*- codeing = utf-8 -*-
#@Time : 2020/5/18 16:05
#@Author : 张文天
#@File : 10.py
#@Software: PyCharm
#-*- codeing = utf-8 -*-
#@Time : 2020/5/18 15:58
#@Author : 张文天
#@File : 9.py
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




def main():
    baseurl = "https://www.tjbwg.com/cn/ExhibitionList.aspx?TypeId=10939"

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
findName = re.compile(r'<h3>\s+(.*)</h3>')

def getData(baseurl):
    datadict = {}
    html = askUrl(baseurl)
    html = html.replace('<br />',' ').replace('<br>',' ')
    soup = BeautifulSoup(html,"html.parser")
    # print(soup)
    datadict['midex'] = '15'
    i = 0
    for item in soup.find_all('div',class_="text"):
        # print(item)
        datadict['ename'] = str(re.findall(findName,str(item))[0]).replace('\n','').strip()
        print(datadict['ename'])
        intro = soup.find_all('div',class_="sum")[i]
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












