from urllib2 import Request, urlopen, URLError, HTTPError
"""
geturl
"""

url = 'http://rrurl.cn/b1UZuP'
req = Request(url)

response = urlopen(url)

print 'Old url:' + url
print 'Real url:' + response.geturl()
