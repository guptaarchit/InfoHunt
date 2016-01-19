import json
import urllib2
from pymongo import MongoClient
client = MongoClient()
db = client.infohunt
host='https://api.github.com/organizations'
oath='client_id=adad980c28260d504dd2&client_secret=a110928a9d11b56ac38ef2f3cd5d79a98c7e11e7'
# para = raw_input('Enter GET to fetched: ')
# if len(para)<1: para="mozilla"
fp=open("repo.txt","a")
cursor=db.organizations.find({"id":{'$gt':115120}},{"login":1,"id":1})
# cursor=db.organizations.find({},{"login":1,"id":1})
visitedLink=[]
while cursor.next:
	for document in cursor:
		para=document['id']
		print para
		count=0
		url= host +'/'+ str(para)+'/repos'+'?'+oath+'&page=1'
		print "Receving...",url
		while True:
			visitedLink.append(url)
			try:
				req_json = urllib2.urlopen(url)
			except urllib2.URLError, e:
				if e.code==404:
					print "404 Error "
					break
			if req_json.getcode:
				pass


			data=req_json.read()
			# print 'loading feached data'
			json_obj=json.loads(data)
			for repo in json_obj:
				try:
					# db.repositories.insert(repo)
					count+=1
					print 'Repository Inserted Sucessfully'
				except Exception, e:
					print "Error while inserting Repository %s"%e
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
				print "Going to Featching Next Organization Repository"
				break
			if url in visitedLink:
				print "URL already visited"
				break
		print 'Total repos in %s is: %d '% (document['login'],count)
		del visitedLink[:]
		last_fetched_organizations=str(document['_id'])+'::'+document['login']+'::'+str(document['id'])+'::'+str(count)+'\n'
		fp.write(last_fetched_organizations)
	# cursor=cursor.next
	print "Going to Next <Cursor></Cursor>"


# use this option to delete duplicate entery in from db
# db.collection.ensureIndex( { record_id:1 }, { unique:true, dropDups:true } )