import json
import urllib2
import pprint
from pymongo import MongoClient
client = MongoClient()
db = client.test
host='https://api.github.com/organizations'
oath='client_id=adad980c28260d504dd2&client_secret=a110928a9d11b56ac38ef2f3cd5d79a98c7e11e7'
para = raw_input('Enter GET to fetched: ')
if len(para)<1: para="errfree"
url= host +'/'+ para+'/repos'+'?'+oath
print "Receving...",url
repos=[]
visitedLink=[]
count=0
while True:
	visitedLink.append(url)
	req_json = urllib2.urlopen(url)
	# print 'Feached data is of type',type(req_json)
	data=req_json.read()
	# print 'loading feached data'
	json_obj=json.loads(data)
	# print len(json_obj)
	# print pprint.pprint(json_obj)
	# print '&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&'
	for repo in json_obj:
		print pprint.pprint(repo)
		db.users.insert(repo)
		print '@@@@@@@@@@@@@@@@@@@@@@@@@@@@@'
	print 'X-RateLimit-Limit: ',req_json.info().getheader('X-RateLimit-Limit')
	print 'X-RateLimit-Limit: ',req_json.info().getheader('X-RateLimit-Remaining')
	try:
		next_link=req_json.headers.getheader('Link').split(';')[0].strip('<>')
		url=next_link
		print "Next Link is: ", next_link
	except:
		next_link=None
		print "Next link Not Found"
	if next_link is None:
		print "Exit!..Exit!..Exit!..Exit!.."
		break
	if url in visitedLink:
		print "url already visited"
		break
fp=open("repo.txt","w+")

for r in repos:
	t=str(r)+'\n'
	fp.write(t)
print len(repos)
print 'Total repos: %d'%count
del repos[:]
del visitedLink[:]