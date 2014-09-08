import urllib2
import urllib
"""
table
"""
postdata=urllib.urlencode({
    'username':'wxg',
    'password':'why888',
    'continueURI':'http://www.verycd.com/',
    'fk':'',
    'login_submit':'login'
})
req = urllib2.Request(
    url = 'http://secure.verycd.com/signin',
    data = postdata
)
result = urllib2.urlopen(req)
print result.read() 


