#encoding=utf-8

import time
from escpos import printer
#from PIL import Image



def printLine(record,flag,deltatime=0):
    p = printer.Usb(0x6868,0x0200,0,in_ep=0x81,out_ep=0x02)
    p.set(align='left')
    p._raw(record[1])  #time
    p._raw('\n')
    p._raw(record[3].encode('gbk'))  #username
    p._raw('\n')
    if flag == 0:
        p._raw(('用'+str(deltatime)+'天读完: ' ).encode('gbk'))
        p._raw('\n')
    if flag == 1:
        p._raw('正在读: '.encode('gbk'))
    p._raw(record[5].encode('gbk'))  #bookname
    p._raw('\n')
    p._raw(('作者: ' + record[7]).encode('gbk'))  #author
    p._raw('\n')
    p._raw(('推荐来源: ' + record[8]).encode('gbk'))  #referral
    p._raw('\n')
    p._raw('\n')
    p._raw('. . . . . . . . . . . . . .')
    p._raw('\n')
    p._raw('\n')
    p._raw('\n')
    #p.cut('PART')
    
# p.text(time.asctime( time.localtime(time.time()) )+'\n')
# s = '造旅馆的人'
#s = s.decode('GB2312')
#print(s)
# name = 'Y.X'
# p.text(name)
# p.text('\n')
#p._raw(s.encode('gbk'))
#p.text('\n')
#im = Image.open('math.jpg')
#im.thumbnail((400,800))
#im.save('./mathn.png')
#p.set(align='left')
#p.image('mathn.png')
