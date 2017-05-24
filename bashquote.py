#!/usr/bin/python3
# Copyright (c) 2017 Abhineet Dubey. All rights reserved.
# Use of this source code is governed by the GPLv3 license that can be
# found in the LICENSE file.
import urllib.request
from bs4 import BeautifulSoup

page = urllib.request.urlopen('http://bash.org/?random')
soup = BeautifulSoup(page, 'lxml')
quote = soup.select('p.qt')[0]
print(quote.text)
