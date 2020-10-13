import os
import time
from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk


class Elastic_Create:
    def __init__(self, index_name, index_type, ip='127.0.0.1'):
        self.index_name = index_name
        self.index_type = index_type
        self.es = Elasticsearch([{'host': ip, 'post': 9200}])

    def create_Index(self):
        # 用来存储所有的商品数据
        _index_mapping = {
            'mappings': {
                'properties': {
                    'upid': {
                        'type': 'integer',  # 这个号应该与sql表中的主键号相同
                    },
                    'name': {
                        'type': 'text',
                        "analyzer": "ik_max_word",  # 配置中文分词器
                        "search_analyzer": "ik_smart"
                    },
                    'date': {
                        'type': 'text',
                    },
                    'price': {
                        'type': 'long'
                    },
                    'visitors': {
                        'type': 'long'
                    }
                }
            }
        }
        if self.es.indices.exists(index=self.index_name) is not True:
            res = self.es.indices.create(index=self.index_name, body=_index_mapping)
            print(res)

    def Insert_Data_To_Index(self):
        # pass
        test_data = [
            {
                'upid': 102, 'name': '洗衣奶', 'date': '2020-10-1',
                'price': 100, 'visitors': 1001
            }
            # {
            #     'up_id': '102', 'name': '洗衣粉', 'date': '2020-10-1',
            #     'price': '100', 'visitors': '1001'
            # }
        ]
        # 一个index下面只有一个type,真是惊人
        for item in test_data:
            res = self.es.index(index=self.index_name, body=item)
            print(res)

    def Search(self):
        request = {'query': {
            'term': {'name': '洗衣'}
        }
        }
        res = self.es.search(index=self.index_name, body=request)
        print(type(res))
        print(res)
        # print(res['_source'])




if __name__ == '__main__':
    # test = Elastic_Create('huaqi_goods', 'test_CB1')
    # # test.create_Index()
    # # test.Insert_Data_To_Index()
    # test.Search()


    t = {'took': 2, 'timed_out': False, '_shards': {'total': 1, 'successful': 1, 'skipped': 0, 'failed': 0},
         'hits':
             {'total': {'value': 3, 'relation': 'eq'}, 'max_score': 0.14874382, 'hits': [
             {'_index': 'huaqi_goods', '_type': '_doc', '_id': 'BX-AInUBbuQctGVb8biC', '_score': 0.14874382,
              '_source': {'upid': 102, 'name': '洗衣奶', 'date': '2020-10-1', 'price': 100, 'visitors': 1001}},
             {'_index': 'huaqi_goods', '_type': '_doc', '_id': 'A3-AInUBbuQctGVbTbg5', '_score': 0.12703526,
              '_source': {'upid': 101, 'name': '洗衣机', 'date': '2020-10-1', 'price': 100, 'visitors': 1001}},
             {'_index': 'huaqi_goods', '_type': '_doc', '_id': 'BH-AInUBbuQctGVbkbj-', '_score': 0.12703526,
              '_source': {'upid': 101, 'name': '洗衣机', 'date': '2020-10-1', 'price': 100, 'visitors': 1001}}]}}
    for item in t['hits']['hits']:
        print(item)
    # print(t['hits']['hits'])