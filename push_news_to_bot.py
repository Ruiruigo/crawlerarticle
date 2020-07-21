# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests
import datetime

data_dits = {}
data_lits = []
data_json = {
    "code": 0,
    "count": 1000,
    "msg": "",
    "data": data_lits
    }
id = 1

def get_time():
    return datetime.datetime.now().strftime('%Y-%m-%d')

# 获取昨天时间 格式：2020-05-24 09:00:00
def yesterday():
    yesterday = str(datetime.date.today() + datetime.timedelta(-1)) + " 09:00:00"
    return yesterday


# 获取昨天简写月份时间 格式：24 May 2020 09:00:00
def yesterday1():
    yesterday = datetime.datetime.now() + datetime.timedelta(-1)
    yesterday = str(yesterday.strftime("%d %b %Y")) + " 09:00:00"
    return yesterday


#封装请求函数
def req(url):
    return BeautifulSoup(requests.get(url).text, 'xml')


# 获取安全客文章标题及链接
def anquanke_data():
    global data_dits, id
    url = "https://api.anquanke.com/data/v1/rss"
    txt = req(url).find_all('item')

    for i in range(len(txt)):
        if txt[i].pubDate.get_text() >= yesterday():
            data_dits['id'] = 'bx' + str(id)
            data_dits['time'] = get_time()
            data_dits['name'] = '安全客'
            data_dits['title'] = txt[i].title.get_text()
            data_dits['url'] = txt[i].guid.get_text()
            data_lits.append(data_dits)
            data_dits = {}
            id += 1


# 获取FreeBuf文章标题及链接
def freebuf_data():
    global data_dits, id
    url = "https://www.freebuf.com/feed"
    txt = req(url).find_all('item')

    for i in range(len(txt)):
        if txt[i].pubDate.get_text()[5:25] >= yesterday1():
            data_dits['id'] = 'bx' + str(id)
            data_dits['time'] = get_time()
            data_dits['name'] = 'FreeBuf'
            data_dits['title'] = txt[i].title.get_text()
            data_dits['url'] = txt[i].link.get_text()
            data_lits.append(data_dits)
            data_dits = {}
            id += 1


# 获取SeeBug文章标题及链接
def seebug_data():
    global data_dits, id
    url = "https://paper.seebug.org/rss/"
    txt = req(url).find_all('item')

    for i in range(len(txt)):
        if txt[i].pubDate.get_text()[5:25] >= yesterday1():
            data_dits['id'] = 'bx' + str(id)
            data_dits['time'] = get_time()
            data_dits['name'] = 'SeeBug'
            data_dits['title'] = txt[i].title.get_text()
            data_dits['url'] = txt[i].link.get_text()
            data_lits.append(data_dits)
            data_dits = {}
            id += 1

# 获取嘶吼文章标题及链接
def sihou_data():
    global data_dits, id
    url = "https://www.4hou.com/feed"
    txt = req(url).find_all('item')

    for i in range(len(txt)):
        if txt[i].pubDate.get_text()[5:25] >= yesterday1():
            data_dits['id'] = 'bx' + str(id)
            data_dits['time'] = get_time()
            data_dits['name'] = '嘶吼'
            data_dits['title'] = txt[i].title.get_text()
            data_dits['url'] = txt[i].link.get_text()
            data_lits.append(data_dits)
            data_dits = {}
            id += 1


def start_go():
    anquanke_data()
    seebug_data()
    sihou_data()
    freebuf_data()


def dell():
    global data_lits
    data_lits = []


if __name__=="__main__":
    start_go()
    print(data_json)

