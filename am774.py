#!/usr/bin/env python
#-*-coding=utf-8-*-
import sys,urllib2
import sgmllib
import string
import optparse
'''    SGMLParser  '''

tagstack = []

class ShowStructure(sgmllib.SGMLParser):
    def unknown_starttag(self,tag,attrs):
#        print 'start tag:<'+tag+'>'
	if tag == "param":
		for key,value in attrs:
			print "%s=%s"%(key,value)
			if key == "value":
				wma_url=value
				print wma_url
				print value
				tagstack.append(value)

def download_file(url,filename):
	process = 0
	req = urllib2.Request(url)
	try:
		fd = urllib2.urlopen(req)
	except urllib2.URLError,e:
		print "Error recieving data",e
		sys.exit(1)
	print "Retrieved", fd.geturl()
	info = fd.info()
	for key,value in info.items():
		print "%s=%s"%(key,value)

	file1=open(filename,"w")
	if not file1:
		print "wma file failed to open"
		sys.exit(1)

	while 1:
		data = fd.read(10240)
		if not len(data):
			break
		process = process + 1
		print "downloading",process
		file1.write(data)
	print "work done"

# get url wma in parsing html
def get_url_wma(url):	
	req = urllib2.Request(url)
	try:
		fd = urllib2.urlopen(req)
	except urllib2.URLError,e:
		print "Error retrieving data:",e
		sys.exit(1)
	print "Retrieved", fd.geturl()
	info = fd.info()#http head info
	for key,value in info.items():
		print "%s=%s"%(key,value)
		data=fd.read()
		#print data
		ShowStructure().feed(data)

	print tagstack[0]
	return tagstack[0]

def getopts():
	parser = optparse.OptionParser()
	parser.add_option("-u","--url",dest="url", help="url needing parse",metavar="URL")
	(options,args) = parser.parse_args()
	if options.url is None:
		parser.error("url")
	return (options.url)
''' am774 -u http://t.am774.com/Apps/Live/?s=/Program/programReview_gy/pid/166/cid/30816'''
def main():
	url = getopts()
	print "getopts url:",url
	g_wma_url = get_url_wma(url)
	g_filename = g_wma_url.split("/")[-1]
	print "start download:",g_filename
	download_file(g_wma_url, g_filename)
	print "finished parser"
	sys.exit(0)
if __name__ == '__main__':main()
