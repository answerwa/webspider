import urllib2
"""
HTTP Error
"""

url = 'http://bbs.csdn.net/callmewhy'

req = urllib2.Request(url)
try: urllib2.urlopen(req)
except urllib2.HTTPError, e:
    print e.code
