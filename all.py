from bs4 import BeautifulSoup
import urllib.request,urllib.error


def askURL(url):
    head = {"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36'}
    request = urllib.request.Request(url, headers=head)
    html = ""
    try:
        response = urllib.request.urlopen(request, timeout=3)
        html = response.read().decode("utf-8")
    except urllib.error.URLError as e:
        return askURL(url)
    return html


def main():
    html = askURL('https://baike.baidu.com/item/%E5%9B%BD%E5%AE%B6%E4%B8%80%E7%BA%A7%E5%8D%9A%E7%89%A9%E9%A6%86')
    soup = BeautifulSoup(html, 'html.parser')
    table = soup.find_all('table')[0]
    data = table.find_all('a', target='_blank')
    n = 1
    for i in data:
        print(n, i.text)
        n = n + 1


if __name__ == '__main__':
    # main()
    l = [32725, 32769, 32811, 32774, 32972, 32877, 33090, 32978, 32876, 32729]
    l.sort()
    print(l)