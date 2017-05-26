#!/usr/bin/python3
# Copyright (c) 2017 Abhineet Dubey. All rights reserved.
# Use of this source code is governed by the GPLv3 license that can be
# found in the LICENSE file.

import json

def getHex(str):
    with open('data.json') as json_data:
        d = json.load(json_data)
        for i in range(len(d)):
            if str in d[i]["name"].lower():
                print("{hex} is the hex code for color {col}".format(hex=d[i]["hexString"],col=d[i]["name"]))


def getRGB(str):
    with open('data.json') as json_data:
        d = json.load(json_data)
        for i in range(len(d)):
            if str in d[i]["name"].lower():
                print("{rgb} are the rgb values for color {col}".format(rgb=d[i]["rgb"],col=d[i]["name"]))


def getHLS(str):
    with open('data.json') as json_data:
        d = json.load(json_data)
        for i in range(len(d)):
            if str in d[i]["name"].lower():
                print("{hls} are the hls values for color {col}".format(hls=d[i]["hsl"],col=d[i]["name"]))

while 1:
    colorName=input("input color name for hex value, type exit to quit\n>>")
    if colorName=='exit':
        break
    else:
        task=input("what you want for this?[rgb:1,hex:2,hls:3]\n>>")
        colorName=colorName.lower()
        if task=='1':
            getRGB(colorName)
        elif task=='2':
            getHex(colorName)
        elif task=='3':
            getHLS(colorName)
        elif task=='exit':
            break
