# Python 学习之路

### Python 爬虫  

####[rosiok.py](https://github.com/kgf0ry/python-crawler/blob/master/rosiok.py)

  1.开学在微信公众号 懒人在思考 上看到 [新人上手 Python 另类建议——被和谐了的答案] (https://mp.weixin.qq.com/s?__biz=MzA3NTEzMTUwNA==&mid=2651081156&idx=1&sn=3c2849f3e7753c1359db253da13aa732&chksm=8485d6dbb3f25fcd1380bc2f7d9b988585a4e028df67f866660be82dc2ad0af07e08e69c5328&scene=0&key=cde9f53f8128acbd090bac3e129f84a706eb1c5dedb07f86485387968072ef20bfd8b41dbf3f579ba2e5def1b443a1c1&ascene=7&uin=MTU5MzU2MDEwNw%3D%3D&devicetype=android-21&version=26031933&nettype=cmnet&pass_ticket=55pZ4CZaO5kjidLvomc1T0XvfmHfsEC3viskcaOxDsvYYAmnTjGJuPocU6oiFZgW&wx_header=1)这篇文章，感受颇深，所以就准备自己试试。

  2.由于只会一点点正则表达式，并没有用 Scrapy 。

  3.没有用多线程，所以时间比较久一点。
	
#####下一步工作

  1.运用 Python 面向对象重写代码。

  2.加入多线程，加快图片下载速度。

  3.尽量使代码简洁，减少冗余度。

####对 rosiok.py 的改进[rosiok2.py](rosiok1.py)
    
  １.不再单一的下载 /shangjia/ 这一目录下的图片，包括 /shipin/ , /x/ , /app/ 的所有图片。这才发现，原来 /x/ 目录下东(zi)西(yuan)好多。不过，那么多的图片，下载好慢。
	
  ２.加入线程函数，减少下载过程中的耗时。

  ３.将一部分函数分开，主函数文件更加精炼。
    
######	４.对未来的想法:利用数据库对抓取到的数据进行存储。
