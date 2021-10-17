from github import Github
import sys

g = Github(sys.argv[1])
listitems = g.get_user('MansiAyer').get_starred()


with open('../src/README.md','r',encoding="utf-8") as file:
	temp = str(file.read());
tootitems = [temp]

tootitems.append("<details><summary><sub>:octocat: Recently Starred Repos :octocat:</sub></summary><hr><i>")
for x in listitems:
		try:
			url = str(x.html_url)
			title = "<b>\n<a href =\"" +url+ "\">" +str(x.full_name)+ "</a>\n</b>"
		except:
			continue
		try:
			description = "<p>"+str(x.description)+"</p>"
		except:
			continue
		try:
			proglang = str(x.language)
		except:
			continue
		temp = str(title+": \n<sup>["+proglang+"]</sup><span>"+description+"</span>\n<br>\n\n")
		tootitems.append(temp)
tootitems.append("</i></details>")

with open('../README.md','w',encoding="utf-8") as file:
	for x in tootitems:
		file.write(str(x))
		file.write("\n")
