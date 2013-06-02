#!/usr/bin/env python

import sys,urllib2

wma_url = "http://res.audio.rbc.cn/wygb/qwqcyy/qwqcyy2013060206305572.wma"

req = urllib2.Request(wma_url)
try:
	fd = urllib2.urlopen(req)
except urllib2.URLError,e:
	print "Error recieving data",e
	sys.exit(1)
print "Retrieved", fd.geturl()
info = fd.info()
for key,value in info.items():
	print "%s=%s"%(key,value)

file1=open("earnmoney.wma","w")
if not file1:
	print "wma file failed to open"
	sys.exit(1)

while 1:
	data = fd.read(1024)
	if not len(data):
		break
	print "downloading"
	file1.write(data)
print "work done"	
