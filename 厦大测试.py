import requests

def spider(url):
	try:
		headers={
		"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36",
		"Host": "ceas.xmu.edu.cn",
		# "Referer": "http://ceas.xmu.edu.cn/site/xmsearch?p=3&F_Name=&F_ItemNo=&F_ProjectStart=&F_ProjectEnd=&F_BXDW=",
		"X-Requested-With": "XMLHttpRequest"

		}
		r=requests.get(url,headers=headers)
		r.raise_for_status()
		r.encoding=r.apparent_encoding
		return r.text
	except Exception as e:
		raise e


# u='http://ceas.xmu.edu.cn/Site/GetProjects?p=2'

# res=spider(u)
# print(res)

import re
pat=r'0([12][0-9]|[3-9][0-9][0-9])\d{7,8}'

s='012356703456211'
res=re.search(pat,s)
print(res)
#　change