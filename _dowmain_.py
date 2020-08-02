import sys

import you_get


#创建一个下载类
class dowMain():
    #获取用户输入的网址
    def getUrl(self,url):
        self.url=url
    #获取用户输入保存文件
    def getSavePath(self,path):
        self.savePath = path
    #获取视频信息
    def getMoveInfo(self,info):
        if info == True:
            self.indexInfo = '-i'
    #指定下载清晰度
    def getMoveSize(self,size):
        self.movesize = size

    #下载主体
    #视频信息
    def moveIfo(self):
        sys.argv = ['you-get',self.indexInfo,self.url]
        you_get.main()
    #默认下载格式
    def defaDown(self):
        sys.argv = ['you-get','-o',self.savePath,self.url]
        you_get.main()
    #指定下载格式
    def setMovesizeDow(self):
        sys.argv = ['you-get','-o',self.savePath,self.movesize,self.url]
        you_get.main()
