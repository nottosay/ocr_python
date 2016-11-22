#!~/python2.5.2/bin/python
# -*- coding: utf-8 -*-
import StringIO
import os
import random

import Image
import ImageEnhance
import pygame


def changeBrightness(img, brightnessValue):
    tmp = ImageEnhance.Brightness(img)
    img = tmp.enhance(brightnessValue)
    return img

def paste(word, index):
    pygame.init()
    font = pygame.font.Font(os.path.join("fonts", "hwxh.ttf"), 33)
    path = "D:/workspace_other/python_space/chinese/" + word
    imgName = "D:/workspace_other/python_space/chinese/" + word + "/" + str(index) + ".jpg"
    if not (os.path.exists(path)):
        os.makedirs(path)
    img = Image.new("RGB", (32, 32), (255, 255, 255))
    rtext = font.render(word, True, (0, 0, 0), (255, 255, 255))
    sio = StringIO.StringIO()
    pygame.image.save(rtext, sio)
    sio.seek(0)
    line = Image.open(sio)
    img.paste(line, (random.randint(-5, 5), random.randint(-15, -5)))
    img.save(imgName)


fp = open("chinese.txt", "r")
for eachline in fp:
    ls = list(eachline.decode('utf-8'))
    for each in ls:
        print each
        for z in xrange(0, 1001):
            paste(each, z)
fp.close()
