#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
tutorial_01.py
purpose: download a picture from 'https://cn.bing.com/
'''

import requests

def downloadFigure(source_url, target_location):
	try:
		r = requests.get(source_url)
		r.raise_for_status()  # 若状态码不为200则抛出异常信息
		r.encoding = r.apparent_encoding
		source_fig = r.content
		writeToFile(source_fig, target_location)
	except Exception as result:
		return result

def writeToFile(source_fig, target_location):
	with open(target_location + '\\flexible-Barrier-04.jpg', 'wb') as f:
			f.write(source_fig)

if __name__ == '__main__':
	source_url = "http://img.co188.com/ivp/images/product/367/427/266/48684328.jpg"
	target_location = 'D:\\Program Files\\GitHub\\learn-Python\\learn-Requests'
	downloadFigure(source_url, target_location)

