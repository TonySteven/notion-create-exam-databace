#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 7/13/22 15:25
# @Author  : StevenL
# @Email   : stevenl365404@gmail.com
# @File    : redis_bloom_test.py

from redisbloom.client import Client

# 创建redis_client
redis_client = Client(host='localhost', port=6379, db=0)

# 把id写入redis布隆过滤器
redis_client.bfAdd('id', 'ecv0akors4dewt8tmn66jw')

print(redis_client.bfExists('id', 'ecv0akors12312dewt8tmn66jw'))  # out: 0
print(redis_client.bfExists('id', 'ecv0akors4dewt8tmn66jw'))  # out: 1
print(redis_client.bfExists('id', 'ecv0akors12312dewt8tmn65jw'))  # out: 0
