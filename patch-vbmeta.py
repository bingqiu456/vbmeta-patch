#!/usr/bin/env python

import os
import ttkbootstrap
from ttkbootstrap.constants import INFO,PRIMARY


def create():

    # Magic for the vbmeta image header
    AVB_MAGIC = b"AVB0"
    AVB_MAGIC_LEN = 4

    # Information about the verification flags
    FLAGS_OFFSET = 123
    FLAGS_TO_SET = b'\x03'

    try:
        fd = os.open("vbmeta.img", os.O_RDWR)
    except OSError:
        return "当前目录下没有vbmeta.img"

    # making sure it's a vbmeta image by reading the magic bytes at the start of the file
    magic = os.read(fd, AVB_MAGIC_LEN)

    if (magic != AVB_MAGIC):
        fd.close()
        return "错误你提供的不是有效vbmeta.img\n文件未修改"

    # set the disable-verity and disable-verification flags at offset 123
    try:
        os.lseek(fd, FLAGS_OFFSET, os.SEEK_SET)
        os.write(fd, FLAGS_TO_SET)
    except OSError:
        fd.close()
        return "修补vbmeta.img失败"

    # end of program
    os.close(fd)
    return "修补成功"


def Loding():
    a = create()
    ttkbootstrap.Label(mywindows,text=a,bootstyle=INFO,font=("微软雅黑",15)).pack()
    mywindows.mainloop()

global mywindows
mywindows = ttkbootstrap.Window(title="一键去除dm校验",themename="litera",size=(400,200))
ttkbootstrap.Label(mywindows,text="作者:Bingyue\n二改LibXZR作者的项目",bootstyle=INFO,font=("微软雅黑",15)).pack()
ttkbootstrap.Button(mywindows,text="一键去除",bootstyle=(PRIMARY,"outline-toolbutton"),command=Loding).pack()
mywindows.mainloop()


