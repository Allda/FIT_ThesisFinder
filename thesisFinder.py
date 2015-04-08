import urllib2
from bs4 import BeautifulSoup
import sys

def find(autor="", supevisior="", name="", keyword="", type="BP"):
	for i in range(1999,2013):
		url = "https://www.fit.vutbr.cz/study/DP/"+type+".php.cs?y="+str(i)+"&ved="+supevisior+"&st="+autor+"&t="+name+"&k="+keyword+"&SubmitButton=Hledat"
		page = urllib2.urlopen(url).read()	

		soup = BeautifulSoup(page)

		works = soup.findAll('dd')
		#print works
		for w in works:
			#print str(w) + "\n"
			soupWork = BeautifulSoup(str(w))
			print  soup.findAll('i')[0].text
			print w.text + " " + str(i)
			print "https://www.fit.vutbr.cz" + soupWork.findAll('a')[0]['href']
			print "-----------------------"

autor = ""
supevisior = ""
name = ""
keyword = ""
type = "BP"

for i in range(0, len(sys.argv)):
	option = sys.argv[i]
	try:
		if(option == "--autor"):
			autor = sys.argv[i+1]
		if(option == "--supevisior"):
			supevisior = sys.argv[i+1]
		if(option == "--name"):
			name = sys.argv[i+1]
		if(option == "--keywords"):
			keyword = sys.argv[i+1]
		if(option == "--type"):
			type = sys.argv[i+1]
	except:
		sys.stderr.write("Bad arguments\n")
		sys.exit()
	


find(autor,supevisior,name,keyword,type)
