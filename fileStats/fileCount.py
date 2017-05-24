#!/usr/bin/python
# Copyright (c) 2017 Abhineet Dubey. All rights reserved.
# Use of this source code is governed by the GPLv3 license that can be
# found in the LICENSE file.

#under construction

import os

videoFiles = ['mkv','mp4','avi','MP4','MKV','AVI','ogv','OGV']
audioFiles = ['mp3','aac','m4a','flac','ogg','MP3','AAC','M4A','FLAC','OGG']

while(fileLoc!='exit'):
    fileLoc=raw_input("Enter location to search[exit to terminate]: ")
    if fileLoc=='exit':
        return 0
    else:
        for (dir, _, files) in os.walk(fileLoc):
            for f in files:
                if f[-3:] in videoFiles:
                    vfiles=vfiles+1
                elif f[-3:] in audioFiles:
                    afiles=afiles+1

print "Number of Video File = ",vfiles,"Number of Audio Files = ",afiles
