import urllib2
import json
while True:
	ip1=raw_input("\033[93m IP Address: ")
	url = "http://ip-api.com/json/"
	response = urllib2.urlopen(url + ip1)
	data = response.read()
	values = json.loads(data)
	os.system("reset")
	print("\033[93m" + "\n IP: " + values['query'])
	print("\033[93m" + " Status: " + values['status'])
	print("\033[93m" + " Region: " + values['regionName'])
	print("\033[93m" + " Country: " + values['country'])
	print("\033[93m" + " City: " + values['city'])
	print("\033[93m" + " ISP: " + values['isp'])
	print("\033[93m" + " Lat,Lon: " + str(values['lat']) + "," + str(values['lon']))
	print("\033[93m" + " ZIPCODE: " + values['zip'])
	print("\033[93m" + " TimeZone: " + values['timezone'])
	print("\033[93m" + " AS: " + values['as'] + "\n")
	break
