#!/usr/bin/python
# Copyright (c) 2017 Abhineet Dubey. All rights reserved.
# Use of this source code is governed by the GPLv3 license that can be
# found in the LICENSE file.

# this is a test code for copying downloaded files to their respective directory according to their extensions

import os

videoCollection = ['mkv','mp4','avi','MP4','MKV','AVI']

for (dir, _, files) in os.walk("/home/abhi/Downloads"):
	for f in files:
     		if f[-3:] in videoCollection:
           	 oldpath=os.path.join(dir,f)
             	 newpath=os.path.join('/home/abhi/Videos/',f)
               	 os.rename(oldpath, newpath)
                 print "Moved file : ",f,"to",newpath
