import sys

import you_get
import os
import _dowmain_
from sys import argv

def download(url):
    sys.argv = ['you-get', '-i', url]
    you_get.main()

def downInfo():
    os.system('you-get https://www.bilibili.com/video/BV1DC4y1b7GP?spm_id_from=333.851.b_7265706f7274466972737431.8' )

if __name__ == '__main__':
    # 视频网站的地址
    for i in range(1,500):
        url = 'https://www.bilibili.com/video/BV1DC4y1b7GP?spm_id_from=333.851.b_7265706f7274466972737431.8'
    # 视频输出的位置
        path = 'E:/bilibili'
    downInfo()

