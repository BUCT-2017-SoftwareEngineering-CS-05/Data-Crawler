#-*- codeing = utf-8 -*-
#@Time : 2020/5/17 8:31
#@Author : 张文天
#@File : spider.py
#@Software: PyCharm
import bs4
import re
import urllib.request,urllib.error
import xlwt
import sqlite3
import sys,urllib
findlink=re.compile(r'<a href="(.*?)">')
findImgSrc=re.compile(r'<img.*src="(.*?)"',re.S)
findTitle =re.compile(r'<span class="title">(.*)</span>')
findreting = re.compile(r'<span class="rating_num" property="v:average">(.*)</span>')
findJudge =re.compile(r'<span>(\d*)人评价</span>')
findinq = re.compile(r'<span class="inq">(.*)</span>')
findBD = re.compile(r'<p class="">(.*?)</p>',re.S)
findMuseum=re.compile(r'<a target="_blank" href="(.*?)>(.*?)</a>')

def main():
    baseurl="https://baike.baidu.com/item/"
    museumList=[]
    museumList=getAllmuseum(baseurl)
    for item in museumList:
        s=item
        item=urllib.parse.quote(item.encode('utf-8').decode(sys.stdin.encoding).encode('utf-8'))
        url=baseurl+item
        getdata(url,s)
    # datalist=getdata(baseurl)
    # path="豆瓣电影top250.xls"
    # savadata(datalist,path)
def getAllmuseum(baseurl):
    datalist=[]
    s='国家一级博物馆'
    s=urllib.parse.quote(s.encode('utf-8').decode(sys.stdin.encoding).encode('utf-8'))
    url=baseurl+s
    # print(url)
    html=askurl(url)
    soup=bs4.BeautifulSoup(html,"html.parser")
    table=soup.find_all('table')[0]
    for item in table.find_all('a',target='_blank'):
        s=str(item.string)
        datalist.append(s)
    return datalist
def getdata(baseurl,s):
    datadict={}
    # print(baseurl)
    html=askurl(baseurl)
    soup=bs4.BeautifulSoup(html,"html.parser").decode('utf-8')
    re_start = re.compile(r'<div class="anchor-list">\n[\s]*<a class="lemma-anchor para-title" name="[\d]*?"',re.S)
    start=re_start.finditer(soup)
    startList=[]
    for i in start:
        startList.append(i.span(0)[0])
    for i in range(len(startList)-1):
        content_data_node = soup[startList[i]:startList[i+1]]
        s0=bs4.BeautifulSoup(content_data_node,"html.parser")
        s1=""
        for item in s0.find_all('h2',class_='title-text'):
            s1=str(item.text)
            s1=s1.replace(' ',"").replace('\n',"")
            data=re.split(s,s1)
            if(len(data)==2):
                s1=data[1]
            elif len(data)==1:
                s1=data[0]
        s3=""
        for item in s0.find_all('div',class_='para'):
            s2=item.text
            s2 = s2.replace(' ', "").replace('\n', "")
            s3+=s2
        datadict={s1:s3}
        print(datadict)
    # info=soup.find_all('div',class_="para")
    # for item in info:
    #     print(item.text)
    return datadict

def askurl(url):
    head={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36"}
    request=urllib.request.Request(url,headers=head)
    html=""
    try:
        response=urllib.request.urlopen(request)
        html=response.read().decode("utf-8")
    except urllib.error.URLError as e:
        if hasattr(e,"code"):
            print(e.code)
        if hasattr(e,"error"):
            print(e.reason)
    return html
def savadata(datalist,path):
    print("save....")

if __name__=="__main__":
    main()
'''
1 故宫博物院(异步)
2 中国科学技术馆
3 中国地质博物馆
4 中国人民革命军事博物馆
5 中国航空博物馆(无官网)
6 北京鲁迅博物馆
7 首都博物馆
8 北京自然博物馆
9 中国人民抗日战争纪念馆(异步)
10 周口店猿人遗址博物馆
11 中国国家博物馆
12 中国农业博物馆
13 北京天文馆
14 文化部恭王府博物馆
15 天津博物馆
16 天津自然博物馆
17 周恩来邓颖超纪念馆(无官网)
18 河北博物院
19 西柏坡纪念馆
20 邯郸市博物馆(爬不出来)
21 山西博物院
22 中国煤炭博物馆
23 八路军太行纪念馆
24 内蒙古博物院
25 鄂尔多斯博物馆(打不开)
26 辽宁省博物馆(爬不出来)
27 “九·一八”历史博物馆
28 旅顺博物馆
29 沈阳故宫博物院
30 吉林省自然博物馆
31 吉林省博物院
32 伪满皇宫博物院
33 东北烈士纪念馆(无官网)
34 铁人王进喜纪念馆(打不开)
35 爱辉历史陈列馆(爬不出来)
36 黑龙江省博物馆
37 大庆博物馆(爬不出来)
38 上海博物馆(异步)
39 上海鲁迅纪念馆
40 中共一大会址纪念馆(异步)
41 上海科技馆(异步）
42 陈云纪念馆(无临展)
43 南京博物院(异步)
44 侵华日军南京大屠杀遇难同胞纪念馆
45 南通博物苑
46 苏州博物馆
47 扬州博物馆(异步)
48 常州博物馆
49 南京市博物总馆
50 浙江省博物馆(爬不出来)
51 浙江自然博物馆(异步)
52 中国丝绸博物馆
53 宁波博物馆
54 杭州博物馆
55 温州博物馆
56 安徽省博物馆
57 安徽中国徽州文化博物馆
58 福建博物院
59 古田会议纪念馆(无展览)
60 泉州海外交通史博物馆
61 中国闽台缘博物馆
62 中央苏区（闽西）历史博物馆(异步)
63 井冈山革命博物馆(无临展)
64 江西省博物馆
65 瑞金中央革命根据地纪念馆(异步)
66 南昌八一起义纪念馆
67 安源路矿工人运动纪念馆(无展览)
68 青岛市博物馆
69 中国甲午战争博物馆(无展览)
70 青州博物馆
71 山东博物馆
72 烟台市博物馆
73 潍坊市博物馆
74 河南博物院(没爬出来)
75 郑州博物馆
76 洛阳博物馆(异步)
77 南阳汉画馆
78 开封市博物馆(异步)
79 鄂豫皖苏区首府革命博物馆
80 湖北省博物馆(异步)
81 荆州博物馆
82 武汉博物馆(异步)
83 辛亥革命武昌起义纪念馆
84 湖南省博物馆
85 韶山毛泽东故居纪念馆（无官网）
86 刘少奇故居纪念馆(异步)
87 长沙简牍博物馆
88 广东省博物馆
89 西汉南越王博物馆
90 孙中山故居纪念馆
91 深圳博物馆
92 广州博物馆(无展览)
93 广东民间工艺博物馆
94 广西壮族自治区博物馆
95 广西民族博物馆
96 海南省博物馆
97 自贡恐龙博物馆
98 三星堆博物馆(异步)
99 成都武侯祠博物馆(异步)
100 邓小平故居陈列馆(无官网)
101 成都杜甫草堂博物馆(打不开)
102 四川博物院
103 成都金沙遗址博物馆
104 自贡市盐业历史博物馆
105 遵义会议纪念馆(无临展)
106 云南省博物馆
107 云南民族博物馆
108 重庆中国三峡博物馆(异步)
109 重庆红岩革命历史博物馆（异步）
110 重庆自然博物馆
111 西藏博物馆(异步)
112 陕西历史博物馆
113 秦始皇兵马俑博物馆(图片)
114 延安革命纪念馆(无临展)
115 汉阳陵博物馆
116 西安碑林博物馆(异步)
117 西安半坡博物馆
118 西安博物院(异步)
119 宝鸡青铜器博物院
120 西安大唐西市博物馆
121 甘肃省博物馆
122 天水市博物馆(异步)
123 敦煌研究院
124 固原博物馆
125 宁夏博物馆
126 青海省博物馆(异步)
127 新疆维吾尔自治区博物馆(无官网)
128 吐鲁番博物馆(无官网)
'''