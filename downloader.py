import urllib2,time, sys
count = 336
while count<=336:
	try:
		page = str(count)
		
		url = "https://babel.hathitrust.org/cgi/imgsrv/download/pdf?id=mdp.39015004530591;orient=0;size=100;seq="+page+";attachment=0"
		print "opening: "+url
		name = "Electronic Engineering"+page+".pdf"
		file = open(name,"wb")
		
		
		request = urllib2.Request(url)
		request.add_header("User-Agent","Mozilla/5.0 (Windows NT 6.1; WOW64; rv:42.0) Gecko/20100101 Firefox/42.0")
		request.add_header("Accept","text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8")
		response = urllib2.urlopen(request,None,100)
		print "opened: "+url
		print "writing to: "+name
		CHUNK = 16*1024
		with open(name,"wb") as f:
			while True:
				chunk = response.read(CHUNK)
				if not chunk: break
				f.write(chunk)
		
		count+=1
		print "done writing"
	except:
		print "Terjadi Error, Coba Ulang"
		time.sleep(120)