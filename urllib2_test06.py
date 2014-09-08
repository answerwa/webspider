import urllib2
"""
URL Error
"""

url = 'http://www.gfdhsakv.com'

req = urllib2.Request(url)
try: response = urllib2.urlopen(req)
except urllib2.URLError, e:
    print e.reason
