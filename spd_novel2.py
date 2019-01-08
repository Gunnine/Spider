# -*- coding:utf-8 -*-
import requests
import time
import random
from bs4 import BeautifulSoup
from urllib import error
from urllib import request

if __name__ == '__main__':
    file = open('总裁的新鲜小妻子2.txt', 'w', encoding='utf-8')      #创建txt 文件 当前目录
    headers = {
        'User-Agent': 'Mozilla/5.0 (Android; Mobile; rv:14.0) Gecko/14.0 Firefox/14.0'
    }
    menu_url = 'http://www.quanshuwang.com/book/16/16860'
    req = requests.get(url=menu_url, headers=headers)
    content_menu = req.content.decode('gbk')
    menu_bf = BeautifulSoup(content_menu, 'html5lib')
    menu_div = menu_bf.findAll('div', class_='clearfix dirconone')
    a_bf = BeautifulSoup(str(menu_div[0]), 'html5lib')
    a = a_bf.findAll('a')
    for each in a:
        chapter_name = each.string      #章节名称
        chapter_url = each.get('href')     #章节链接

        file.write('\n'+chapter_name+'\n')

        proxy = {'http': ''}

        proxy_list = [
            {"http": '115.203.99.9'},
            {"http": '119.101.116.253'},
            {"http": '119.101.116.50'},
            {"http": '119.101.113.13'}
        ]
        proxy = random.choice(proxy_list)
        proxy_support = request.ProxyHandler(proxy)
        opener = request.build_opener(proxy_support)
        request.install_opener(opener)

        chapter_req = requests.get(url=chapter_url, headers=headers, timeout=30)
        try:
            chapter_content = chapter_req.content.decode('gbk')
        except error.Httperror as e:
            print(e.code)
        except error.URLError as e:
            print(e.reason)

        chapter_bf = BeautifulSoup(str(chapter_content), 'html5lib')
        chapter_tag = chapter_bf.findAll('div', class_='mainContenr')
        chapter_text = chapter_tag[0].text.replace('\xa0', '\n')
        file.write(chapter_text)
        file.write('\n')
        time.sleep(random.random()*4)
    file.close()


