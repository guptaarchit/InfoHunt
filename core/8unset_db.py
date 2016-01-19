from pymongo import MongoClient
client = MongoClient()
db = client.infohunt
count=0
cursor1=db.repositories.find()
db_tag=[]
for document in cursor1:
	# db.repositories.update({'_id':document['_id']},{'$set':{'db_tag':db_tag}})
	db.repositories.update({'db_tag':'null'}, { '$unset' : {'db_tag' : 1} });
	count+=1
	del db_tag[:]
	print 'pop %d'%count
