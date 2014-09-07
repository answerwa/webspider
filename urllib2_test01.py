import urllib2
response = urllib2.urlopen('http://www.imooc.com/')
html = response.read()
print html
