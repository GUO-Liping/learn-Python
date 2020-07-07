#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
tutorial_04.py
purpose: 百度搜索关键词提取返回结果关键词
'''

import requests

if __name__ == '__main__':
	url = 'https://www.baidu.com/s'
	try:
		kv1 = {'user-agent':'Mozilla/5.0'}
		kv2 = {'wd':'Python'}
		r = requests.get(url, headers=kv1, params = kv2)
		print(r.request.url)
		r.raise_for_status()
		r.encoding = r.apparent_encoding
		print(len(r.text))
	except:
		print("爬取失败")


