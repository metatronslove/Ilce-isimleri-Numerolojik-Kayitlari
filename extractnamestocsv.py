import urllib.request
import codecs
import sys
import time
start = time.time()
sys.stdin.reconfigure(encoding='UTF-8')
sys.stdout.reconfigure(encoding='UTF-8')
dosya=codecs.open('ilçeisimleri2024.csv', 'w', 'UTF-8')
dosya.write('Kayıt, Şehir No, Şehir, İlçe No, İlçe\n')
site = 'https://tr.wikipedia.org/wiki/T%C3%BCrkiye%27nin_il%C3%A7eleri'
temp = urllib.request.urlopen(site)
print('\n\r\033[1m' + site + '\033[0m adresinden isimler yolunuyor :')
page = temp.read().decode('UTF-8')
cities = 1
expectedentry = 973
numberofcities = totaloftowns = 0
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
			percentage = 100*totaloftowns/expectedentry
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
				page = page[lnk:]
				if nameofacity != 'İsimlerine göre ilçeler ve nüfusları':
					total = '0'*len(str(expectedentry)) + str(totaloftowns)
					recordline = str(totaloftowns) + ',' + str(numberofcities) + ',' + nameofacity + ',' + str(townsofcity) + ',' + nameofatown + '\n'
					linetoview = '\033[92m' + total[-1*len(str(expectedentry)):] + ' ► %' + str(percentage)[:5] + ' tamamlandı ► \033[0m' + nameofacity + " ilinin " + nameofatown + ' ilçesi eklendi. '
					dosya.write(recordline)				
					print(linetoview, sep='',end =' '*19+'\b'*len(linetoview)+'\b'*19, file = sys.stdout , flush = True)
				else:
					cities = 0
dosya.close()
end = time.time()
print(linetoview, sep='',end ='\b\b \033[92m►\033[0m \033[1m\'ilçeisimleri2024.csv\'\033[0m dosyasına kaydedildi \033[92m►\033[0m ' + str(end - start)[:5] + ' saniyede sonlandı\n\r\n\r', file = sys.stdout , flush = True)