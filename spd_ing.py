# -*- coding:UTF-8 -*-
import requests,sys
from bs4 import BeautifulSoup

'''未完成'''
'''
 类说明：全书网下载《总裁的新鲜小妻子》
 Modify:
 2019-01-04
'''
class downloader(object):

    def __init__(self):
        self.server = 'http://www.quanshuwang.com/'     # 网站地址
        self.target = 'http://www.quanshuwang.com/book/16/16860'        #小说地址
        self.name = []      # 存放章节名称
        self.urls = []      #存放章节链接
        self.nums = 0       # 章节数

    '''
        函数说明：获取下载链接
        Parameter:
        无
        Return:
        无
        Modify:
        2019-01-04
        '''

    def get_chapter_download_url(self):
        req = requests.get(url=self.target)
        html = req.content.decode('gbk')
        menu_bf = BeautifulSoup(html, 'html5lib')
        menu_div = menu_bf.findAll('div', class_='clearfix dirconone')
        a_bf = BeautifulSoup(str(menu_div[0]), 'html5lib')
        a = a_bf.findAll('a')
        self.nums = len(a[0:])

        for each in a[0:]:
            self.name.append(each.string)
            self.urls.append(self.server+each.get('href'))

    '''
    函数说明：获取章节内容
    Parameter:
        target -  小说下载链接（string）
    Return:
        texts - 章节内容（string）
    Modify:
        2019-01-04
    '''

    def get_novel_contents(self, target):
        req = requests.get(url=target)
        html = req.content.decode('gbk')
        bf = BeautifulSoup(html, 'html5lib')
        div_texts = contents_bf.findAll('div', class_='mainContenr')
        texts = div_texts[0].text.replace('\xa0', '\n')
        return texts



    '''
    函数说明：将爬取的文章内容写入文件
    Parameter:
        target -  小说下载链接（string）
    Return:
        texts - 章节内容（string）
    Modify:
        2019-01-04
    '''

    def writer(self, name, path, text):
        write_flag = True

        with open(path, 'a', encoding='utf-8')as f:
            f.write(name + '\n')
            f.writelines(text)
            f.write('\n\n')

if __name__ == '__main__':
    dl = downloader()
    dl.get_chapter_download_url
    print('总裁的新鲜小妻子开始下载：')

    for i in range(dl.nums):
        dl.writer(dl.name[i], '总裁的新鲜小妻子.txt', dl.get_novel_contents(dl.get_chapter_download_url[i]))
        sys.stdout.write("  已下载:%.3f%%" % float(i / dl.nums) + '\r')
        sys.stdout.flush()
    print('《总裁的新鲜小妻子》下载完成')










'''  格式化打印第一章内容
if __name__ == '__main__':
    target = 'http://www.quanshuwang.com/book/16/16860/6264619.html'
    req = requests.get(url=target)
    content = req.content.decode('gbk')
    bf = BeautifulSoup(content, 'html5lib')

    texts = bf.find_all('div', class_="mainContenr")
    print(texts[0].text.replace('\xa0', '\n'))
    
if __name__ == '__main__':
    server = 'http://www.quanshuwang.com/book/16/16860'
    req = requests.get(url=server)
    contentmenu = req.content.decode('gbk')
    menu_bf = BeautifulSoup(contentmenu, 'html5lib')
    menu_div = menu_bf.findAll('div', class_='clearfix dirconone')
    a_bf = BeautifulSoup(str(menu_div[0]), 'html5lib')
    a = a_bf.findAll('a')
    for each in a:
        print(each.string, each.get('href'))
        '''






