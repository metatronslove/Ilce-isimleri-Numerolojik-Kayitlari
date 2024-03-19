import urllib.request
import codecs
import sys
sys.stdin.reconfigure(encoding='UTF-8')
sys.stdout.reconfigure(encoding='UTF-8')
dosya=codecs.open('ilçeisimleri2024.csv', 'w', 'UTF-8')
dosya.write('Kayıt, Şehir No, Şehir, İlçe No, İlçe\n')
site = 'https://tr.wikipedia.org/wiki/T%C3%BCrkiye%27nin_il%C3%A7eleri'
temp = urllib.request.urlopen(site)
print(site + ' adresinden isimler yolunuyor :')
page = temp.read().decode('UTF-8')
cities = 1
numberofcities = 0
townsofcity = 0
totaloftowns = 0
while cities == 1:
	cityname = page.find('<span class="mw-headline"')
	if cityname != -1:
		numberofcities += 1
		bas=page.find('">', cityname)
		son=page.find('</span>', bas)
		nameofacity=page[bas+2:son]
		townsofcity = 0
		page = page[son:]
		towns = 1
		while towns == 1:
			townsofcity += 1
			totaloftowns += 1
			townname = page.find('<li><a href')
			if townname != -1:
				bas=page.find('">', townname)
				son=page.find('</a></li>', bas)
				lnk=page.find('</a>', bas)
				ctr=page.find('</a> (İl merkezi)</li>', bas)
				chk=page.find('</a></li></ul>', bas)
				if lnk == ctr:
					nameofatown=page[bas+2:lnk]
				else:	
					nameofatown=page[bas+2:son]
				if son == chk:
					towns = 0
				page = page[son:]
				if nameofacity != 'İsimlerine göre ilçeler ve nüfusları':
					recordline = str(totaloftowns) + ',' + str(numberofcities) + ',' + nameofacity + ',' + str(townsofcity) + ',' + nameofatown + '\n'
					linetoview = '' + nameofacity + " ilinin " + nameofatown + ' isimli ilçesi listeye eklenen ' + str(totaloftowns) + '. ilçe oldu. '
					dosya.write(recordline)
					print(linetoview, sep='',end =' '*19+'\b'*len(linetoview)+'\b'*19, file = sys.stdout , flush = True)
				else:
					cities = 0
print(linetoview, sep='',end ='\b\b ► \'ilçeisimleri2024.csv\' dosyasına kaydedildi\n\r', file = sys.stdout , flush = True)
dosya.close()
