import json
import urllib2
from pymongo import MongoClient
client = MongoClient()
db = client.infohunt

host='https://api.github.com'
para = raw_input('Enter GET to fetched: ')
if len(para)<1: para="/organizations"
oath='client_id=adad980c28260d504dd2&client_secret=a110928a9d11b56ac38ef2f3cd5d79a98c7e11e7'
url= host + para+'?'+oath+'&since=860682'
errr=open('org_log_error.txt','a+')
url_hit=open('url_hit.txt','w+')

while True:
	print "Receving...",url
	req_json = urllib2.urlopen(url)
	print 'Feached data is of type',type(req_json)
	data=req_json.read()
	print 'loading feached data'
	json_obj=json.loads(data)
	for org in json_obj:
		try:
			# db.organizations_log.insert(org)
			print 'Organisation Log Inserted sucessfully'
			try:
				org_url=org['url']+'?'+oath
				print "Receving Organisation...",org_url
				org_req_json = urllib2.urlopen(org_url)
				org_data=org_req_json.read()
				org_json_obj=json.loads(org_data)
				# db.organizations.insert(org_json_obj)
				uhit=org_url+'\n'
				url_hit.write(uhit)
			except Exception, e:
				org_err='org_err'+'::'+org['login']+'::'+str(org['id'])+'\n'
				errr.write(org_err)
				print "Error occure"
		except Exception, e:
			log_err='log_err'+'::'+org['login']+'::'+str(org['id'])+'\n'
			errr.write(log_err)
			print "Error occure"
	next_link=req_json.info().getheader('Link').split(';')[0].strip('<>')
	print 'X-RateLimit-Limit: ',req_json.info().getheader('X-RateLimit-Limit')
	print 'X-RateLimit-Limit: ',req_json.info().getheader('X-RateLimit-Remaining')
	print 'next_link:-',next_link
	ulhit=next_link+'\n'
	url_hit.write(ulhit)	
	url=next_link






