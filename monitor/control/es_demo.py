# -*- coding:utf-8 -*-
from elasticsearch import Elasticsearch
import json
import time
from system_message import get_all_system
es = Elasticsearch("192.168.3.21:9200", timeout=600)

def es_index(lis):
    lis = json.loads(lis)
    for item in lis:
        node = item["hostname"]
        es.index(index="system_monitor",doc_type=node,id=itime,body=item)


def get_data(node, page_num, page_size):
    page_num=(int(page_num)-1)*int(page_size)
    query_body = {
        'query': {
            'bool': {
            }
        },
        'sort': [
            {'time': 'desc'}
        ],
        'size': page_size,
        'from': page_num
    }
    result = es.search(index="system_monitor", doc_type=node, body=query_body)['hits']['hits']
    return result


# 一共返回多少条数据
def get_number(node):
    query_body = {
        'query': {
            'bool': {
            }
        },
        'sort': [
            {'time': 'desc'}
        ],
        'size': 200
    }
    result = es.search(index="system_monitor", doc_type=node, body=query_body)['hits']['hits']
    return len(result)


def get_condition_data(node, page_num, page_size, keys):
    page_num=(int(page_num)-1)*int(page_size)
    query_body = {
        'query': {
            'bool': {
                "must": [
                    {
                        "query_string": {
                            "default_field": "_all",
                            "query": keys
                        }
                    }
                ],
                "must_not": [],
                "should": []
            }
        },
        'sort': [
            {'time': 'desc'}
        ],
        'size': page_size,
        'from': page_num
    }
    result = es.search(index="system_monitor", doc_type=node, body=query_body)['hits']['hits']
    return result


# 一共返回多少条数据
def get_condition_number(node, keys):
    query_body = {
        'query': {
            'bool': {
                "must": [
                    {
                        "query_string": {
                            "default_field": "_all",
                            "query": keys
                        }
                    }
                ],
                "must_not": [],
                "should": []
            }
        },
        'sort': [
            {'time': 'desc'}
        ],
        'size': 200
    }
    result = es.search(index="system_monitor", doc_type=node, body=query_body)['hits']['hits']
    return len(result)
