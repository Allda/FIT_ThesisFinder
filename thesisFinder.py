import urllib2
from bs4 import BeautifulSoup


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


find(name="hdr")
