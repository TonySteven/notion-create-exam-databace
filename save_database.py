#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 7/13/22 13:05
# @Author  : StevenL
# @Email   : stevenl365404@gmail.com
# @File    : save_database.py

from notion_client import Client

# 创建 API 客户端
# notion = Client(auth=os.environ['NOTION_TOKEN'])
notion = Client(auth='secret_zjmsB5oeXEGw25ndV7JVN1j2C8EwE9jMbaUpGvVtZ6I')

# 写入数据库
notion.pages.create(
    **{
        'parent': {'database_id': 'f406642b43ba49ff99844e621608f8d3'},
        'properties': {
            'Id': {
                'title': [
                    {
                        'text': {
                            'content': 'ecv0akors4dewt8tmn66jw'
                        }
                    }
                ]
            },
            'Title': {
                'rich_text': [{
                    'text': {
                        'content': '下列不属于毛泽东思想成熟时期的著作是(  )',
                        'link': None
                    }
                }]
            },
            'Answer': {
                'rich_text': [{
                    'text': {
                        'content': '1',
                        'link': None
                    },
                }]
            },
            'Options': {
                'multi_select': [{'name': '0 人民政协'}, {'name': '1 党代表大会'}, {'name': '2 人民代表大会'}, {'name': '3 人大常委会'}],
            },
            'QuestionType': {
                'number': 1,
            },
            'Subject': {
                'select': {
                    'name': '毛概'
                },
            }
        }
    }
)
