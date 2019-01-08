# -*- coding:utf-8 -*-
import requests
import time
import random
from bs4 import BeautifulSoup
from urllib import error

'''
第一版：没有任何修饰，无反爬应对
'''

if __name__ == '__main__':
    file = open('总裁的新鲜小妻子.txt', 'w', encoding='utf-8')      #创建txt 文件 当前目录
    menu_url = 'http://www.quanshuwang.com/book/16/16860'
    req = requests.get(url=menu_url)
    content_menu = req.content.decode('gbk')
    menu_bf = BeautifulSoup(content_menu, 'html5lib')
    menu_div = menu_bf.findAll('div', class_='clearfix dirconone')
    a_bf = BeautifulSoup(str(menu_div[0]), 'html5lib')
    a = a_bf.findAll('a')
    for each in a:
        chapter_name = each.string      #章节名称
        chapter_url = each.get('href')     #章节链接

        file.write('\n'+chapter_name+'\n')
        chapter_req = requests.get(url=chapter_url, timeout=30)
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
        time.sleep(random.random()*3)
    file.close()


