#!/usr/bin/env python3
# coding: utf-8
# File: MedicalGraph.py
import os
import json
from py2neo import Graph,Node

class MedicalGraph:
    def __init__(self):
        cur_dir = '/'.join(os.path.abspath(__file__).split('/')[:-1])
        self.data_path = os.path.join(cur_dir, 'data/medical.json')
        # self.g = Graph(
        #     host="127.0.0.1",  # neo4j 搭载服务器的ip地址，ifconfig可获取到
        #     http_port=7687,  # neo4j 服务器监听的端口号
        #     user="neo4j",  # 数据库user name，如果没有更改过，应该是neo4j
        #     password="12345678")
        self.g =  Graph("http://localhost:7474", auth=("neo4j", "12345678"))