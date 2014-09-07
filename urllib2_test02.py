import urllib2
req = urllib2.Request('http://www.imooc.com/')
response = urllib2.urlopen(req)
the_page = response.read()
print the_page
