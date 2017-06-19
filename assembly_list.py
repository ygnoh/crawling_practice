# Crawling from:
# http://www.assembly.go.kr/assm/memact/congressman/memCond/memCond.do

import re
import requests
from bs4 import BeautifulSoup as bs

url = 'http://www.assembly.go.kr/assm/memact/congressman/memCond/memCondListAjax.do?currentPage=1&rowPerPage=1000'

html = requests.get(url).text
soup = bs(html, 'html5lib')

for member_tag in soup.select('.memberna_list dl dt a'):
	name = member_tag.text
	link = member_tag['href']

	matched = re.search(r'\d+', link)
	if matched:
		member_id = matched.group(0)
	else:
		member_id = None

	print(name, member_id)

