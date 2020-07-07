#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
tutorial_06.py
purpose: 爬取一个IP地址对应的地理位置信息
'''

import requests

url = "https://m.ip138.com/iplookup.asp?ip="

try:
	r = requests.get(url+'221.237.179.253')
	r.raise_for_status()
	r.encoding = r.apparent_encoding
	print(r.text[-500:])

except:
	print('爬取失败')

