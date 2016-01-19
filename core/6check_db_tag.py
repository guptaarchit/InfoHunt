from pymongo import MongoClient
client = MongoClient()
db = client.infohunt
fh=open("tag.txt",'r')
tags=fh.read()
tags=tags.split('\n')

db_tag=[]
cursor=db.repositories.find({},{'description':1,'full_name':1,'db_tag':1})
count =0
cnt=0
for document in cursor:
	if 'db_tag' not in document.keys():
		print document['_id']
		count=count+1
		print count
	else:
		print document['db_tag']
		cnt=cnt+1
		print "fdsfsdfsdf",cnt
print "Done!"
print cnt
print count
# count=0
# cursor1=db.users.find()
# for document in cursor1:
# 	# document.pop('db_tag',0)
# 	# print document
# 	db.users.update({ '_id': document['_id'] }, { '$unset' : {'db_tag' : 1} });
# 	count+=1
# 	# break
# print 'pop %d'%count