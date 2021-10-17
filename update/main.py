from bs4 import BeautifulSoup as bs
import requests
import re

starspage = requests.get('https://github.com/MansiAyer?tab=stars')
soup = bs(starspage.text, 'html.parser')


listitems = []
for x in soup.find_all("div", class_="col-12 d-block width-full py-4 border-bottom color-border-muted"):
		try:
			title = str(x.h3)
		except:
			continue
		try:
			description = str(x.p)
		except:
			continue
		try:
			proglang = str(x.find_all("span", class_="ml-0 mr-3"))
		except:
			continue
		temp = str(title+": <sup>"+proglang+"</sup><span>"+description+"</span>\n<br>\n\n")
		listitems.append(temp)

with open('../src/README.md','r',encoding="utf-8") as file:
	temp = str(file.read());
tootitems = [temp]

tootitems.append("<details><summary><sub>:octocat: Recently Starred Repos :octocat:</sub></summary><hr><i>")
for x in listitems:
		a = x.replace("<h3>","<b>")
		a = a.replace("</h3>","</b>")
		a = a.replace("None","<br>No description provided :/<br>")
		a = a.replace("[]","")
		tootitems.append(a)
tootitems.append("</i></details>")

with open('../README.md','w',encoding="utf-8") as file:
	for x in tootitems:
		file.write(str(x))
		file.write("\n")
