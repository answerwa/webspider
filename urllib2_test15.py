import urllib2
"""
HTTP Request Header
"""
request = urllib2.Request('http://www.imooc.com')
request.add_header('User-Agent', 'fake-client')
response = urllib2.urlopen(request)
print response.read()
