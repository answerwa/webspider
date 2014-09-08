import urllib2
"""
timeout setting
"""
#before python 2.6
urllib2.socket.setdefaulttimeout(10)

#after python 2.6
response = urllib2.urlopen('http://www.baidu.com', timeout=10)
