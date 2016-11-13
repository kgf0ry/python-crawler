#! usr/bin/env python
#coding:utf-8
import rosiok1
import time
import threading
class rosiok:
    def __init__(self):
        self.url='http://www.rosiok.com'
        self.ulist=['/shipin/','/app/','/x/','/shangjia/']
        self.htmls=[]
        self.imgurls=[]
    def gethtmls(self):
        i=self.ulist
        i=i.pop()
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
    def getimgs(self):
        pass
    def thread(self,fun):
        for i in range(len(self.ulist)):
            t=threading.Thread(target=fun)
            t.start()



if __name__=="__main__":
    R=rosiok()
    R.thread(R.gethtmls)
    print R.ulist

    print ('over') 
