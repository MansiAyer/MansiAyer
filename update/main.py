from github import Github
import sys

g = Github(sys.argv[1])
listitems = g.get_user().get_starred()

for x in listitems:
		try:
			url = str(x.html_url)
			title = "<b><a href =\"" +url+ ">" +str(x.full_name)+ "</a></b>"
		except:
			continue
		try:
			description = str(x.description)
		except:
			continue
		try:
			proglang = str(x.language)
		except:
			continue
		temp = str(title+": <sup>"+proglang+"</sup><span>"+description+"</span>\n<br>\n\n")
		listitems.append(temp)

with open('../src/README.md','r',encoding="utf-8") as file:
	temp = str(file.read());
tootitems = [temp]

tootitems.append("<details><summary><sub>:octocat: Recently Starred Repos :octocat:</sub></summary><hr><i>")
for x in listitems:
		a = a.replace("None","<br>No description provided :/<br>")
		a = a.replace("[]","")
		tootitems.append(a)
tootitems.append("</i></details>")

with open('../README.md','w',encoding="utf-8") as file:
	for x in tootitems:
		file.write(str(x))
		file.write("\n")
