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

def counter(fileLoc):
    vfiles=0
    afiles=0
    dfiles=0
    total=1
    for (dir, _, files) in os.walk(fileLoc):
        for f in files:
            if f[-3:] in videoFiles:
                vfiles=vfiles+1
            elif f[-3:] in audioFiles:
                afiles=afiles+1
            elif f[-3:] in documentFiles:
                dfiles=dfiles+1
    total=vfiles+afiles+dfiles
    print ("Number of Video File =",vfiles,"\nNumber of Audio Files = ",afiles,"\nNumber of documents = ",dfiles,"\nTotal number of files = ",total)
    vBar = colored('|','red')
    aBar = colored('|','green')
    dBar = colored('|','blue')
    print (vBar * math.ceil(vfiles*10/total))
    print (aBar * math.ceil(afiles*10/total))
    print (dBar * math.ceil(dfiles*10/total))
    return

while 1:
    fileLoc=input("Enter location to search [exit to quit]\n>>")
    if fileLoc=='exit':
        break
    else:
        counter(fileLoc)
