import urllib
import urllib2
"""
set user-agent
can not be used
"""
values = {'name' : 'WHY',
          'location' : 'SDU',
          'language': 'Python' }
url = 'http://www.imooc.com'
user-agent = 'Mozilla/5.0 (Linux; U; Android 4.0.2; en-us; Galaxy Nexus Build/ICL53F) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30'

headers = { 'User-Agent' : user-agent }
data = urllib.urlencode(values)
req = urllib2.Request(url, data, hearders)
response = urllib2.urlopen(req)
print response.read()
