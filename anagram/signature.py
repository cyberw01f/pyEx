#!/usr/bin/python

# Copyright (c) 2017 Abhineet Dubey. All rights reserved.
# Use of this source code is governed by the GPLv3 license that can be
# found in the LICENSE file.

# this script creats a signature,word file from a list of words
with open("wordlist.txt", "r") as source, open("worddb.txt", "a") as target:
    for line in source:
	l=line.rstrip()
	s=''.join(sorted(l))
	#print "%s,%s"%(s,l)
	addline=s+','+l
 	#target = open('db.txt', 'a')
  	target.write(addline+'\n')
