#!/usr/bin/python

# Copyright (c) 2017 Abhineet Dubey. All rights reserved.
# Use of this source code is governed by the GPLv3 license that can be
# found in the LICENSE file.

# this script compares a user inputted word with the signature of words generated by signature script
outputs=[]
with open("worddb.txt", "r") as database:
	gotInput=raw_input("Enter your word : ")
 	userWord=gotInput.rstrip()
	signature=''.join(sorted(userWord))
 	for line in database:
      		key = line.split(',')[0]
      		word = line.split(',')[1]
#      		print key,word
      		if signature==key:
            		clean=word.rstrip()
            		outputs.append(clean)
#            		print word
print 'Your anagram/s: '+', '.join(outputs)
