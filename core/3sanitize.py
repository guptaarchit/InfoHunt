from pymongo import MongoClient
client = MongoClient()
db = client.infohunt
count=0
cursor1=db.repositories.find({'db_tag':None	},{'db_tag':1})
# cursor1=db.repositories.find(},{'db_tag':1,'language':1})
# print cursor1
def removeDuplicate():
	for document in cursor1:
		print document['db_tag']
		db_tag=list(set(document['db_tag']))
		print 'Tag After sanitize',db_tag
		# db.repositories.update({'_id':document['_id']},{'$set':{'db_tag':db_tag}})
		count+=1
		print 'Tag sanitized %d'%count
def RemoveNoneValues():
	cursor1=db.repositories.find({'db_tag':None	},{'db_tag':1})
	# cursor1=db.repositories.find({'db_tag':[]	},{'db_tag':1,'language':1})
	for document in cursor1:
		print document['db_tag']
		# db_tag=list(set(document['db_tag']))
		db_tag=document['db_tag']
		db_tag.remove(None)
		print 'Tag After None Value',db_tag
		# db.repositories.update({'_id':document['_id']},{'$set':{'db_tag':db_tag}})
		count+=1
		print 'None Value Removed %d'%count
print 'Data Sanitization Done!'