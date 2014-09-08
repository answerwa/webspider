from urllib2 import Request, urlopen, URLError, HTTPError
"""
info
"""

url = 'http://www.baidu.com'
req = Request(url)

response = urlopen(url)

print 'Info():'
print response.info()
