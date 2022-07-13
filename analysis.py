#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 7/13/22 10:57
# @Author  : StevenL
# @Email   : stevenl365404@gmail.com
# @File    : analysis.py


import json

from notion_client import Client as NotionClient
from redisbloom.client import Client as RedisBloomClient

from utils.utils import stu_question2options

# 加载文件
file_name = '毛概_1'
subject = file_name.split('_', 1)[0]
path = r"/Users/steven/PycharmProjects/notion-create-exam-databace/origin_json_data/" + file_name + ".json"
file = open(path, 'r', encoding='utf-8')

# 创建 API 客户端
# notion = Client(auth=os.environ['NOTION_TOKEN'])
notion = NotionClient(auth='secret_zjmsB5oeXEGw25ndV7JVN1j2C8EwE9jMbaUpGvVtZ6I')

# 创建redis_client
redis_client = RedisBloomClient(host='localhost', port=6379, db=0)

# 解析数据
list_data = json.load(file)

for data in list_data:
    stuQuestions = data["stuQuestions"]
    index = 1
    for stuQuestion in stuQuestions:
        print('执行第' + str(index) + '遍')
        stuQuestion_id = stuQuestion["id"]
        stuQuestion_title = stuQuestion["title"]
        stuQuestion_answer = stuQuestion["answer"]
        stuQuestion_type = stuQuestion["questionType"]
        stuQuestion_options = stuQuestion["options"]
        stuQuestion_options_done = stu_question2options(stuQuestion_options)

        if redis_client.bfExists('id', stuQuestion_id):
            print('已存在的id:', stuQuestion_id)
            index += 1
            continue

        # 写入数据库
        notion.pages.create(
            **{
                'parent': {'database_id': 'f406642b43ba49ff99844e621608f8d3'},
                'properties': {
                    'Id': {
                        'title': [
                            {
                                'text': {
                                    'content': stuQuestion_id
                                }
                            }
                        ]
                    },
                    'Title': {
                        'rich_text': [{
                            'text': {
                                'content': stuQuestion_title,
                                'link': None
                            }
                        }]
                    },
                    'Answer': {
                        'rich_text': [{
                            'text': {
                                'content': stuQuestion_answer,
                                'link': None
                            },
                        }]
                    },
                    'Options': {
                        'multi_select': stuQuestion_options_done,
                    },
                    'QuestionType': {
                        'number': stuQuestion_type,
                    },
                    'Subject': {
                        'select': {
                            'name': subject
                        },
                    }
                }
            }
        )
        index += 1

        # 把id写入redis布隆过滤器
        redis_client.bfAdd('id', stuQuestion_id)
