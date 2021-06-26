
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    功能：电脑端微信用户图片DAT格式转化为图片
    环境：python3.7
    日期：2019/12/31 22:28
    作者：指尖魔法师
    版本：1.0
"""
import os

#https://blog.csdn.net/veray/article/details/103796327

def main():
    indir = r'G:\wx\2019-06'
    outdir = r'G:\wx\out2019-06'
    
    indir = r'D:\wx'
    outdir = r'D:\wx_out'
 
    # 获取文件夹下所有文件
    infiles = os.listdir(indir)
 
    # 计数成功的文件个数
    count = 0
 
    # 循环每个文件进行判断、转换
    for infile in infiles:
        # 获取文件名
        filename = infile[0:infile.find('.')]
 
        # 二进制读取文件
        f1 = open(os.path.join(indir, infile), 'rb')
        infilebytes = f1.read()
        newfile = []
 
        # 判断图片类型JPG，通过异或判定
        if (infilebytes[0] ^ 0xFF) == (infilebytes[1] ^ 0xD8):
            y1 = infilebytes[0] ^ 0xFF
            print('%s,文件是JPG图片，每个字节是根据0x%X异或进行加密' % (infile, y1))
 
            # 字节进行异或转换，组合成新的文件
            for i in infilebytes:
                newbyte = i ^ y1
                newfile.append(newbyte)
            newfile2 = bytes(newfile)
 
            # 写入新文件
            f2 = open(os.path.join(outdir, filename+'.jpg'), 'wb')
            f2.write(newfile2)
            count += 1
 
        # 判断图片类型PNG，通过异或判定
        elif (infilebytes[0] ^ 0x89) == (infilebytes[1] ^ 0x50):
            y1 = infilebytes[0] ^ 0x89
            print('%s,文件是PNG图片，每个字节是根据0x%X异或进行加密' % (infile, y1))
            for i in infilebytes:
                newbyte = i ^ y1
                newfile.append(newbyte)
            newfile2 = bytes(newfile)
            f2 = open(os.path.join(outdir, filename+'.png'), 'wb')
            f2.write(newfile2)
            count += 1
 
        # 判断图片类型GIF，通过异或判定
        elif (infilebytes[0] ^ 0x47) == (infilebytes[1] ^ 0x49):
            y1 = infilebytes[0] ^ 0x47
            print('%s,文件是GIF图片，每个字节是根据0x%X异或进行加密' % (infile, y1))
            for i in infilebytes:
                newbyte = i ^ y1
                newfile.append(newbyte)
            newfile2 = bytes(newfile)
            f2 = open(os.path.join(outdir, filename+'.gif'), 'wb')
            f2.write(newfile2)
            count += 1
        else:
            print('%s无法识别的类型！' % infile)
    print('识别出图片%d张' % count)
 
 
if __name__ == '__main__':
    main()

