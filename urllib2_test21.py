import urllib2
import urllib
"""
user-agent
can not be used

referer
"""
postdata=urllib.urlencode({
    'username':'wxg',
    'password':'why888',
    'continueURI':'http://www.verycd.com/',
    'fk':'',
    'login_submit':'login'
})
header = {
    'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'
}
headers = {
    'Referer':'http://www.cnbeta.com/articles'
}
req = urllib2.Request(
    url = 'http://secure.verycd.com/signin/*/http://www.verycd.com/',
    data = postdata,
    headers = headers
)

