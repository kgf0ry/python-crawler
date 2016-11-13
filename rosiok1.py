#coding:utf-8
import urllib2
import re
def downhtml(url):
    try:
        html=urllib2.urlopen(url).read().decode('GB2312').encode('utf-8')
    except urllib2.URLError as e:
        print 'Download html error:',e.reason
        html=None
    return html
def downimg(imgurl):
    try:
        img=urllib2.urlopen(imgurl).read()
    except urllib2.URLError as e:
        print 'Download img error:',e.reason
        img=None
    return img
def nextpage(html):
    list=re.findall("<a href='(.*?)'>下一页</a>",html)
    if len(list):
        return list[0]
    else:
        list=None

if __name__=='__main__':
    url=raw_input('please input the url you want to download:')
    data=downimg(url)
    print data
