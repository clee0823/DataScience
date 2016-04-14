import urllib
from BeautifulSoup import *
import re
url = 'http://python-data.dr-chuck.net/comments_190370.html '
#url = 'http://corporate.pchome.com.tw/'
#url = raw_input("Enter file name: ")
html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)
tags = soup('span')
lst = list()
count = 0
for tag in tags:
 print 'Contents:',tag.contents[0]
 for line in tag:
  x = re.findall('([0-9]+)', line)
  if len(x)<1 : continue
  for word in x:
   #if word in lst : continue
   lst.append(word)
   count = count +1
y = map(int,lst)
t = sum(y)
print count
print y,t



