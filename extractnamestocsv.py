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
				recordline = str(totaloftowns) + ',' + str(numberofcities) + ',' + str(nameofacity) + ',' + str(townsofcity) + ',' + str(nameofatown) + '\n'
				linetoview = 'Allah yıkıcı bir zelzele ile yıkmak istediğinde hangi adayı başkanı seçmiş olmanızın sonucu etkileyemeyeceği ' + str(nameofacity) + " ilinin " + str(townsofcity) + ' isimli ilçesi listeye eklenen ' + str(totaloftowns) + '. ilçe oldu. '
				lengthtoview = len(linetoview)
				if nameofacity != 'İsimlerine göre ilçeler ve nüfusları':
					dosya.write(recordline)
					print(linetoview, sep='',end ='', file = sys.stdout , flush = False)
					sys.stdout.flush()
				else:
					cities = 0
dosya.close()