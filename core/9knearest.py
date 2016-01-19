#!/usr/bin/python -
import json
import urllib2
from pymongo import MongoClient
from operator import itemgetter
from bson.objectid import ObjectId
import operator 
from collections import OrderedDict
import operator
import time
def getNeighbors(trainingSet, k,searched_tag,db):
	distances = trainingSet
	print distances['566bd61728cab63a34ddc1cd']
	#
	neighbors=[]
	#
	#
	sorted_x = sorted(distances.items(), key=operator.itemgetter(1))
	sorted_x.reverse()
	#print sorted_x[0][1]
	#print sorted_x
	p=0
	for i in sorted_x:
		#if(i[0])
		#print i[0]
		p=p+1
		cursor=db.repositories.find({'_id':ObjectId(i[0])})
		for doc in cursor:
			for tag in searched_tag:
				for j in doc["db_tag"]:
					if((tag!="") and (j)):
		 				if(tag==j):		
		 					l=i[0][1]
		 					li=list(i)
		 					li[1]=li[1]+2
		 					i=tuple(li)
		 					sorted_x[p]=i
		 					p=0
		 					break 
	#for
	sorted_xx = sorted(distances.items(), key=operator.itemgetter(1))
	sorted_xx.reverse() 
	#print sorted_xx	
	neighbors_ret=[] 					
	for x in sorted_xx:
	 	neighbors.append(x[0])
	for x in range(k):
		neighbors_ret.append(neighbors[x]) 	
	return neighbors_ret

def datapass(db,k,searched_tag,search_id):
	trainingSet={}
	neighbors={}
	cursor=db.sim_matrix.find({'id_A':search_id})	
	#while cursor.next:
	for document in cursor:
		trainingSet=(document["distance"])
	neighbors=getNeighbors(trainingSet,k,searched_tag,db)
	#print neighbors
	urls(neighbors,db)
def urls(neighbors,db):
	neighbors_url=[]
	for x in neighbors:
		#print x
		cursor=db.repositories.find({'_id':ObjectId(x)})
		for url in cursor:
			#print url	
			neighbors_url.append(url["url"])
			print url["db_tag"]		
	print neighbors_url

def main():
	client = MongoClient()
	db = client.infohunt
	k=20
	time1=time.time()
	searched_tag=['cloud','python']
	search_id=ObjectId("566ae49e28cab649c9a26a69")
	datapass(db,k,searched_tag,search_id)
	time2=time.time()
	print "Total item %s" %(str(time2-time1))
main()


	