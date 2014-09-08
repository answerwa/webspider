from urllib2 import Request, urlopen, URLError, HTTPError
"""
HTTP Error & URL Error
exception 2
"""

url = 'http://www.csdagfdsh.com'
req = Request(url)

try:
    response = urlopen(req)
except URLError, e:
    if hasattr(e, 'code'):
        print 'The server could not fulfill the request.'
        print 'Error code: ', e.code
    elif hasattr(e, 'reason'):
        print 'We failed to reach a server.'
        print 'Reason:', e.reason

else:
    print 'No exception was raised.'
