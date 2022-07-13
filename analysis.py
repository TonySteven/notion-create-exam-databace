#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 7/13/22 10:57
# @Author  : StevenL
# @Email   : stevenl365404@gmail.com
# @File    : analysis.py


import json

from notion_client import Client

from utils.utils import stu_question2options

# 加载文件
file_name = '毛概_1'
subject = file_name.split('_', 1)[0]
path = r"/Users/steven/PycharmProjects/notion-create-exam-databace/origin_json_data" + file_name + ".json"
file = open(path, 'r', encoding='utf-8')

# 创建 API 客户端
# notion = Client(auth=os.environ['NOTION_TOKEN'])
notion = Client(auth='secret_zjmsB5oeXEGw25ndV7JVN1j2C8EwE9jMbaUpGvVtZ6I')

# 解析数据
list_data = json.load(file)

for data in list_data:
    stuQuestions = data["stuQuestions"]
    for stuQuestion in stuQuestions:
        stuQuestion_id = stuQuestion["id"]
        stuQuestion_title = stuQuestion["title"]
        stuQuestion_answer = stuQuestion["answer"]
        stuQuestion_type = stuQuestion["questionType"]
        stuQuestion_options = stuQuestion["options"]
        stuQuestion_options_done = stu_question2options(stuQuestion_options)

        # 写入数据库
        notion.pages.create(
            **{
                'parent': {'database_id': 'f406642b43ba49ff99844e621608f8d3'},
                'properties': {
                    'id': {
                        'title': [
                            {
                                'text': {
                                    'content': stuQuestion_id  # 野菜名を指定
                                }
                            }
                        ]
                    },
                    'title': {
                        'rich_text': [{
                            'plain_text': stuQuestion_title,
                            'text': {
                                'content': stuQuestion_title,
                                'link': None
                            },
                            'type': 'text'
                        }],
                    },
                    'answer': {
                        'rich_text': [{
                            'plain_text': stuQuestion_answer,
                            'text': {
                                'content': stuQuestion_answer,
                                'link': None
                            },
                            'type': 'text'
                        }],
                        'type': 'rich_text'
                    },
                    'options': {
                        'multi_select': stuQuestion_options_done,
                        'type': 'multi_select'
                    },
                    'questionType': {
                        'number': stuQuestion_type,
                        'type': 'number'
                    },
                    'subject': {
                        'select': {
                            'name': subject
                        },
                        'type': 'select'
                    },
                }
            }
        )
