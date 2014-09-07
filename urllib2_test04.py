import urllib
import urllib2
"""
data Get send
"""
data = {}

url = 'http://www.imooc.com'

data['name'] = 'WHY'
data['lacation'] = 'SDU'
data['language'] = 'Python'


url_values = urllib.urlencode(data)
print url_values

full_url = url + '?' +url_values

response = urllib2.urlopen(full_url)
print response.read()
