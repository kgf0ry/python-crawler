#! usr/bin/env python
#coding:utf-8
import re
import rosiok1
import time
import threading
class rosiok:
    def __init__(self):
        self.url='http://www.rosiok.com'
        self.ulist=['/shipin/','/x/','/app/','/shangjia/']
        self.htmls=[]
        self.imgurls=[]
        self.imglist=[]
    def gethtmls(self):
        i=self.ulist.pop()
        html=rosiok1.downhtml(self.url+i)
        while 1:
            self.htmls.append(html)
            
            if rosiok1.nextpage(html):
                html=rosiok1.downhtml(self.url+i+rosiok1.nextpage(html))
                time.sleep(3)
                print (i+'-------------------->ok')
            else:
                print ('over.....')
                break

    def geturls(self):
        while len(self.htmls):
            imgurl=re.findall('<li><a href="(.*?)" class="pimg"',self.htmls.pop())
            self.imgurls.extend(imgurl) 
    def thread(self,fun):
        for i in range(len(self.ulist)):
            t=threading.Thread(target=fun)
            t.start()
    def getimg(self):
        while len(self.imgurls):
            url=self.url+self.imgurls.pop()
            html=rosiok1.downhtml(url)
            imglist=re.findall(' class="a" height="96" src="(http://tu.68flash.com/.*?.jpg)"',html)
            self.imglist.extend(imglist)
    def mkfile(self,filename,file):
        f=open(fliename,'wb')
        f.write(file)
        f.close
    def downimg(self):
        i=0
        while len(self.imglist):
            data=rosiok1.downimg(self.imglist.pop())
            time.sleep(3)
            i=i+1
            self.mkfile('rosiok/{}.ipg'.format(i),data)



if __name__=="__main__":
    R=rosiok()
    #R.thread(R.gethtmls)
 #   R.gethtmls()
    R.gethtmls()
    print (len(R.htmls))
    R.thread(R.geturls())
    R.thread(R.getimg())
    print len(R.imglist)
  #  print R.imglist[:10]
    R.thread(R.downimg())

