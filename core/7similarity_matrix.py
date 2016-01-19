import json
import urllib2
from pymongo import MongoClient
# from bson import json_util, ObjectId
def mat():
	client = MongoClient()
	db = client.infohunt
	i=0
	k=0
	flag=0
	cursor=db.repositories.find({},{'db_tag':1}).skip(500	)
	for ytags in cursor:
		similarity=dict()
		tag_y=ytags["db_tag"]
		ykey=ytags['_id']
		cursor1=db.repositories.find({'_id':{'$ne':ytags['_id']}},{'db_tag':1})
		similarity['id_A']=ykey
		distance={}
		i=i+1;
		print "In y ",i
		for xtag in cursor1:
			tag_x=xtag['db_tag']
			common_tag=set(tag_y) & set(tag_x)
			weight_common_tag=len(common_tag)
			if weight_common_tag<=1:
				continue
			xkey=str(xtag['_id'])
			distance[xkey]=weight_common_tag
			print "common tag's : ",common_tag,weight_common_tag
			k=k+1
			print "In %d y:%d "%(i,k)
		similarity['distance']=distance
		# db.sim_matrix.insert(similarity)
		print "Marix Created and inserted for ",i
		# print similarity
mat()
