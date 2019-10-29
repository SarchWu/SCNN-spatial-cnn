# -*- coding: utf-8 -*-
# @Time    : 2019/8/23 15:48
# @Author  : user
# @Site    : 
# @File    : tmp.py
# @Software: PyCharm


valid_classes = [7, 8, 11, 12, 13, 17, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 31, 32, 33]
import os
import random
import shutil
oriImg="H:\\tmp\\test_scnn\oriImg"
labelImg="H:\\tmp\\test_scnn\labelImg"
outpath="H:\\tmp\\test_scnn\out"
image_out=os.path.join(outpath,"image")
label=os.path.join(outpath,"label")
def generate_dir(path,split):
    outpath=os.path.join(path,split)
    return outpath
image_out_train=generate_dir(image_out,"train")
image_out_val=generate_dir(image_out,"val")
label_out_train=generate_dir(label,"train")
label_out_val=generate_dir(label,"val")

def mkdir(path):
    if not os.path.exists(path):
        os.mkdir(path)
mkdir(image_out)
mkdir(label)
mkdir(image_out_train)
mkdir(image_out_val)
mkdir(label_out_train)
mkdir(label_out_val)


oriimglist=os.listdir(oriImg)
random.shuffle(oriimglist)
train_imglist=oriimglist[0:int(0.8*len(oriimglist))]
val_imglist=oriimglist[int(0.8*len(oriimglist)):]

def movefile(list,oriImg,labelImg,outImg,outlabel,split):
    for file in list:
        oriimgpath=os.path.join(oriImg,file)
        labelimgpath=os.path.join(labelImg,file)
        outimgpath=os.path.join(outImg,split,file)
        outlabelpath=os.path.join(outlabel,split,file)

        shutil.move(oriimgpath,outimgpath)
        shutil.move(labelimgpath,outlabelpath)

movefile(train_imglist,oriImg,labelImg,image_out,label,"train")
movefile(val_imglist,oriImg,labelImg,image_out,label,"val")




