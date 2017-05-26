#!/usr/bin/python3
# Copyright (c) 2017 Abhineet Dubey. All rights reserved.
# Use of this source code is governed by the GPLv3 license that can be
# found in the LICENSE file.

#under construction
import os
import math
from termcolor import colored

videoFiles = ['mkv','mp4','avi','MP4','MKV','AVI','ogv','OGV']
audioFiles = ['mp3','aac','m4a','flac','ogg','MP3','AAC','M4A','FLAC','OGG']
documentFiles = ['pdf','PDF','doc','xls','odt','odp','rtf','txt']
fileLoc=""

def getFileSize(fileName): #function made for future use
    fileSize=os.path.getsize(fileName)
    return fileSize

def GetHumanReadable(size,precision=2):
    suffixes=['B','KB','MB','GB','TB']
    suffixIndex = 0
    while size > 1024 and suffixIndex < 4:
        suffixIndex += 1 #increment the index of the suffix
        size = size/1024.0 #apply the division
    return "%.*f%s"%(precision,size,suffixes[suffixIndex])

def counter(fileLoc):
    vfiles=afiles=dfiles=vSize=aSize=dSize=totalFiles=totalSize=0
    vtotal=atotal=dtotal=0
    for (dir, _, files) in os.walk(fileLoc):
        for f in files:
            if f[-3:] in videoFiles:
                vfiles=vfiles+1
                vSize=getFileSize(os.path.join(dir, f))
                vtotal=vtotal+vSize
            elif f[-3:] in audioFiles:
                afiles=afiles+1
                aSize=getFileSize(os.path.join(dir, f))
                atotal=atotal+aSize
            elif f[-3:] in documentFiles:
                dfiles=dfiles+1
                dSize=getFileSize(os.path.join(dir, f))
                dtotal=dtotal+dSize
    totalFiles=vfiles+afiles+dfiles
    if totalFiles==0:
        totalFiles=1
    print("There are Video Files : {v} of total size : {s}".format(v=vfiles,s=GetHumanReadable(vtotal,2)))
    print("There are Audio Files : {v} of total size : {s}".format(v=afiles,s=GetHumanReadable(atotal,2)))
    print("There are Documents : {v} of total size : {s}".format(v=dfiles,s=GetHumanReadable(dtotal,2)))
    vBar = colored('>>','red')
    aBar = colored('>>','green')
    dBar = colored('>>','blue')
    print (vBar * math.ceil(vfiles*10/totalFiles))
    print (aBar * math.ceil(afiles*10/totalFiles))
    print (dBar * math.ceil(dfiles*10/totalFiles))
    return



while 1:
    fileLoc=input("Enter location to search [exit to quit]\n>>")
    if fileLoc=='exit':
        break
    else:
        counter(fileLoc)
