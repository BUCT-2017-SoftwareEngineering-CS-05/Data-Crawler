#-*- codeing = utf-8 -*-
#@Time : 2020/5/18 12:57
#@Author : 张文天
#@File : 4.py
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
    baseurl = "http://www.jb.mil.cn/zlcl/jbcl/"

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
findName = re.compile(r'<h3>(.*)</h3>')
findIntro = re.compile(r'<p>(.*)</p>')
findSrc = re.compile(r'<img src=(.*)>')

def getData(baseurl):
    datadict = {}
    html = askUrl(baseurl)
    html = html.replace('<br />',' ').replace('<br>',' ')
    soup = BeautifulSoup(html,"html.parser")
    # print(soup)
    datadict['midex'] = '4'
    i = 2
    for item in re.findall(findName,str(soup)):
        # print(item)
        datadict['ename'] = str(item)
        # print(datadict['ename'])
        datadict['eintro'] = str(re.findall(findIntro,str(soup))[i]).replace('\n','').replace('\xa0','').replace('\u3000','').replace('\r','')
        # print(datadict['eintro'])
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












