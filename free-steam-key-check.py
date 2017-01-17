# -*- coding: utf-8 -*-

__author__ = "Davyd Maker"
__version__ = "1.1.1"

from xml.dom import minidom
import requests

headers = {
    'User-Agent': 'Mozilla/5.0'
}

lastKey = open('checkKey.txt', 'a').close()
lastKey = open('checkKey.txt', 'r')
content = lastKey.readlines()

i = 1
newkey = False

r = requests.get("http://www.freesteamkeys.me/feed/",headers=headers)
xml = r.text

xmldoc = minidom.parseString(xml)
itemlist = xmldoc.getElementsByTagName('title')

if len(content) == 10:
	while i <= 10:
		if content[i-1].strip() != itemlist[i].firstChild.data:
			newkey = True
			print('['+str(i)+'][NEW] - '+itemlist[i].firstChild.data)
		else:
			print('['+str(i)+'] - '+content[i-1].strip())
		i+=1
else:
	newkey = True
	while i <= 10:
		print('['+str(i)+'][NEW] - '+itemlist[i].firstChild.data)
		i+=1


lastKey.close()
lastKey = open('checkKey.txt', 'w')

while i <= 19:
	lastKey.write(itemlist[i-10].firstChild.data+'\n')
	i+=1
lastKey.write(itemlist[10].firstChild.data)

if newkey == True:
	print('\nThere are new keys. Go to: http://www.freesteamkeys.me')
else:
	print('\nNo new keys.')

lastKey.close()
