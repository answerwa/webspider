# -*- coding: utf-8 -*-
#---------------------------------------
#   程序：百度贴吧爬虫
#   版本：0.1
#   作者：answerwa
#   日期：2014-09-08
#   语言：Python 2.7
#   操作：输入带分页的地址，去掉最后面的数字，设置一下起始页数和终点页数。
#   功能：下载对应页码内的所有页面并存储为html文件。
#---------------------------------------
 
import urllib2
from string import zfill
 
#定义百度函数
def baidu_tieba(url,begin_page,end_page):
    filepath = 'Download/'
    for i in xrange(begin_page, end_page+1):
        sName = zfill(i,5) + '.html'#自动填充成六位的文件名
        print '正在下载第' + str(i) + '个网页，并将其存储为' + sName + '......'
        f = open(filepath + sName,'w+')
        m = urllib2.urlopen(url + str(i)).read()
        f.write(m)
        f.close()
 
 
#-------- 在这里输入参数 ------------------
bdurl = str(raw_input(u'请输入贴吧的地址，去掉pn=后面的数字：\n'))
begin_page = int(raw_input(u'请输入开始的页数：\n'))
end_page = int(raw_input(u'请输入终点的页数：\n'))
#-------- 在这里输入参数 ------------------
 

#调用
baidu_tieba(bdurl,begin_page,end_page)
