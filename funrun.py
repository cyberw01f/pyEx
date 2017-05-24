#!/usr/bin/python
# Copyright (c) 2017 Abhineet Dubey. All rights reserved.
# Use of this source code is governed by the GPLv3 license that can be
# found in the LICENSE file.
lon=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
#sum=0

def foradd(args):
    lsum=0
    for item in args:
        lsum=lsum+item
    print lsum

def whileadd(args):
    lsum=0
    i=0
#    argsLength=len(args)
    while i!=len(args):
        value=args[i]
        lsum+=value
        i += 1
    print lsum

print "from for loop"
foradd(lon)
print "from while loop"
whileadd(lon)
