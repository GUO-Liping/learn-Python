#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
tutorial_02.py
purpose: 爬取京东Gopro8商品页面
'''

import requests

if __name__ == '__main__':
	url = "https://www.baidu.com/"
	try:
		r = requests.get(url)
		r.raise_for_status()
		r.encoding = r.apparent_encoding
		print(r.text[:1000])
	except:
		print("爬取失败")


