import urllib2
"""
info application
"""

# create password manager
password_mgr = urllib2.HTTPPasswordMgrWithDefaultRealm()

# add user and password
top_level_url = 'http://example.com/foo/'
password_mgr.add_password(None, top_level_url, 'why', '1223')

# create a new handler
handler = urllib2.HTTPBasicAuthHandler(password_mgr)

# create opener (OpenerDirector object)
opener = urllib2.build_opener(handler)

a_url = 'http://www.baidu.com'

# get a url by opener
opener.open(a_url)

# install opener
# now the urllib2.urlopen will use this opener
urllib2.install_opener(opener)
