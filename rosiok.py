#coding:utf-8
#www.rosiok.com/shangjia   图片批量下载
import urllib2
import re
import os
from time import sleep
#下载网页
def dwhtml(url):
    try:
        html=urllib2.urlopen(url).read()
    except urllib2.URLError as e:
        print 'Download error:',e.reason
        html=none
    return html.decode('GB2312').encode('utf-8')
#得到组图地址列表
def getimgurl(url,html):
    imgurls=re.findall('<li><a href="/shangjia(.*?)" class="pimg"', html)
    urls=[]
    hm=[]
    for i in imgurls:
        urls.append(url+i)
    for x in urls:
        hm.append(dwhtml(x))
    return hm
#得到所有页
def getnextpage(url,html):
    hms=[]
    while 1:
        hms.extend(getimgurl(url, html))
        list=re.findall("<a href='(.*?)'>下一页</a>", html)
        if len(list):
            html = dwhtml(url + list[0])
        else:
            break
    return hms
#得到文件夹名字
def mkdir(html):
    name=re.findall("<title>(.*?)</title>",html)
    dirname=name[0].decode('utf-8')
    dirpath="E:/rosiok/"+dirname
    if os.path.exists(dirpath):
        os.removedirs(dirpath)
    else:
        os.makedirs(dirpath)
    return dirpath
#创建文件夹
def mkfile(filename,file):

    f=open(filename,'wb')
    f.write(file)
    f.close()
#下载图片
def dwimg(url):
    print 'Downloading ...', url
    try:
            img = urllib2.urlopen(url).read()
    except urllib2.URLError as e:
            print 'Download error:', e.reason
            img = none
    return img
#下载页面中的图片
def getimg(html):
    dirpath=mkdir(html)
    print dirpath
    list=re.findall(' class="a" height="96" src="(http://tu.68flash.com/rosi/.*?.jpg)"',html)
    for index in range(len(list)):
        data=dwimg(list[index])
        sleep(3)
        filepath=dirpath+'/'+str(index)+'.jpg'
        mkfile(filepath,data)
if __name__=='__main__':
    url = 'www.rosiok.com'
    url= 'http://' + url + '/shangjia/'
    html=dwhtml(url)
    hms=getnextpage(url,html)
    for i in hms:
        getimg(i)


