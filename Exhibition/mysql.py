#-*- codeing = utf-8 -*-
#@Time : 2020/4/17 20:13
#@Author : 张文天
#@File : mysql.py
#@Software: PyCharm
# import pymysql
# pymysql.install_as_MySQLdb()
# connect = pymysql.connect(
#     host='127.0.0.1',
#     port=3306,
#     user='root',
#     passwd='a19990721',
#     db='test',
#     charset='utf8'
# )
# cursor = conn.cursor()


from bs4 import BeautifulSoup
import re
import urllib.request,urllib.error
import xlwt
import sqlite3

findinfo = re.compile(r'<.*?>')

def main():
    baseurl = "http://www.qhmuseum.cn/#/exhibitioninfoDetials/thematicDetials?id=7&t=%25E3%2580%258A%25E5%25A6%2599%25E5%25A2%2583%25E7%25A5%259E%25E9%259F%25B5%25E2%2580%2594%25E2%2580%2594%25E8%2597%258F%25E4%25BC%25A0%25E4%25BD%259B%25E6%2595%2599%25E5%2594%2590%25E5%258D%25A1%25E8%2589%25BA%25E6%259C%25AF%25E5%25B1%2595%25E3%2580%258B"
    html = askUrl(baseurl)
    print(html)
    # html = (html.replace('<br />', ' ')).replace('<br>', ' ')

    data = []
    # soup = BeautifulSoup(html,"html.parser")

    # info = soup.find_all('div',class_="l")[0]
    # info = str(info).replace('\n', '').replace('\r', '')
    # info = BeautifulSoup(info, "html.parser")
    # openTime1 = info.find_all('div',class_="x-tit")[0]
    # openTime1 = str(openTime1)
    # openTime2 = info.find_all('div',class_="padd")[1]
    # openTime2 = str(openTime2)
    # ticket = info.find_all('div',class_="padd")[0]
    # ticket = str(ticket)
    # openTime = openTime1+openTime2
    # openTime = re.sub(findinfo, '', openTime)
    # ticket = re.sub(findinfo, '', ticket)
    # data.extend(['山西博物馆'])
    # data.append(openTime)
    # data.append(ticket)
    # print(data)

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






