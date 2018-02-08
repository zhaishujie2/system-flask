# -*- coding:UTF-8 -*-
import py2neo
import urllib
import json
graph = py2neo.Graph(
    "http://192.168.3.21:7474",
    username="neo4j",
    password="123456"
    # "http://localhost:7474",
    # username="neo4j",
    # password="lichen"
)

#获得集群中所有的节点数量,关系数量
def getNodeID_RelationshipID():
    IDdic = {}
    Ncql = "MATCH (n) RETURN count(n)"
    result = graph.run(Ncql)
    nodelist = []
    for i in result:
        nodelist.append(i)
    nid = nodelist[0]['count(n)']
    IDdic['NodeID']=nid
    Rcql = "MATCH ()-->() RETURN count(*)"
    result = graph.run(Rcql)
    relalist = []
    for i in result:
        relalist.append(i)
    rid = relalist[0]['count(*)']
    IDdic['RelationshipID']=rid
    return IDdic

#获得neo4j集群中的具体的关系，返回一个list
def getRelationshipName():
    cql = "MATCH ()-[r]->() RETURN DISTINCT type(r)"
    result = graph.run(cql)
    list = []
    for item in result:
        list.append(((str)(item['type(r)'])).split("u'")[0])
    return list
#获得neo4j集群中的具体的Label，返回一个list
def getLabelsName():
    cql = "MATCH (a) RETURN DISTINCT labels(a)"
    result = graph.run(cql)
    list = []
    for item in result:
        if item['labels(a)'] != []:
            list.append(((str(item).split("[u'"))[1].split("']")[0]))
    return list

def get_all():
    IDdic = {}
    IDdic['RelationshipTypes']=getRelationshipName()
    IDdic['NodeLabels']=getLabelsName()
    return IDdic
