#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
tutorial_03.py
purpose: 修改请求头，爬取有爬虫限制的网页
'''

import requests

if __name__ == '__main__':
	url = 'https://www.amazon.cn/'
	try:
		kv = {'user-agent':'Mozilla/5.0'}
		r = requests.get(url, headers=kv)
		r.raise_for_status()
		r.encoding = r.apparent_encoding
		print(r.text[1000:2000])
	except:
		print("爬取失败")


