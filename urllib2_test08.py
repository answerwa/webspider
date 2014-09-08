from urllib2 import Request, urlopen, URLError, HTTPError
"""
HTTP Error & URL Error
"""

url = 'http://www.baidu.com'
req = Request(url)

try:
    response = urlopen(req)
except HTTPError, e:
    print 'The server could not fulfill the request.'
    print 'Error code: ', e.code
except URLError, e:
    print 'We failed to reach a server.'
    print 'Reason:', e.reason

else:
    print 'No exception was raised.'
