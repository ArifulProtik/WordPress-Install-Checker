# -*- coding: utf-8 -*-
#Author:http://github.com/ArifulProtik
#mail:mdarifulislam.protik@gmail.com
#Follow Me For More If You Like It Give It A Star
import requests 
from bs4 import BeautifulSoup
def FindAll():
	headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
	f=open('list.txt', 'r').read().split('\n')
	o = ["/wordpress/wp-admin/install.php", "/wp-admin/install.php"] 
	with open('result.txt', 'w') as result:
		for line in f:
			if line == "":
				continue;
			newline=line.split('/')
			parent_url=newline[2]
			for line in o:
				if line == "":
					continue;
				final_url='http://' + parent_url + line 
				try:
					r = requests.get(final_url,headers=headers)
					r.raise_for_status()
				except requests.exceptions.HTTPError:
					print('[Error-Http]'+final_url)
					continue;
				except requests.exceptions.ConnectionError:
					print('[WrongURL]'+final_url)
					continue;
				else:
					html = r.text
					soup = BeautifulSoup(html,'html.parser')
					title = '<title>WordPress › Setup Configuration File</title>'
					resultT = str(soup.title)
					if resultT == title:
						print('[Okay]'+final_url)
						result.write(final_url+"\n")
					else:
						print('[Nope]'+final_url)
print('Just Started  Please Wait')

FindAll()
print("Program Finished, See The result.txt File For Ur Result")
