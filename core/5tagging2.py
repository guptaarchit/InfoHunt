from pymongo import MongoClient

client = MongoClient()
db = client.infohunt
fh=open("tag.txt",'r')
tags=fh.read()
tags=tags.split('\n')

db_tag=[]
cursor=db.repositories.find({},{'language':1,'full_name':1,'db_tag':1})
count =0
for document in cursor:
	# description=document['description']
	if 'db_tag' not in document.keys():
		db_tag=[]
		print "New db_tag created"
	else:
		db_tag=document['db_tag']
	count+=1
	db_tag.append(document['language'])
	# for tag in tags:
	# 	full_name=str(document['full_name'])
	# 	if tag in description:
	# 		db_tag.append(tag)

	# 	if tag in full_name:
	# 		db_tag.append(tag)
	db.repositories.update({'_id':document['_id']},{'$set':{'db_tag':db_tag}})
	print 'Sucessfully Inserted Tag%d'%count
	del db_tag[:]

# count=0
# cursor1=db.users.find()
# for document in cursor1:
# 	# document.pop('db_tag',0)
# 	# print document
# 	db.users.update({ '_id': document['_id'] }, { '$unset' : {'db_tag' : 1} });
# 	count+=1
# 	# break
# print 'pop %d'%count