# Türkiye İlçe İsimleri için Numerolojik Kayıtlar
## Wikipedia kayıtlarından isim listeleri edindim...

Türk Alfabe Sıra No numerolojisi değerlerini [Sahur Özel'in Ebced Hesaplayan Makrolarındaki Kullanıcı Tanımlı Fonksiyonlarla](https://github.com/metatronslove/abjad) hesaplattık.

```extractnamestocsv.py``` dosyasını çalıştırarak; ```ilçeisimleri2024.csv``` isimli liste oluşturuldu. ```İlçe İsimleri Numerolojik Kayıtları.ods```, ```İlçe İsimleri Numerolojik Kayıtları.xlsm``` dosyalarına fonksiyonları içeren makro kodları iliştirilmiştir. [Wikipedia](https://tr.wikipedia.org/wiki/T%C3%BCrkiye%27nin_il%C3%A7eleri) kayıtlarında not edildiği üzere 2024 yılında 81 il ve 973 ilçe var. Bu 973 ilçe ismi listesinde sadece 51 il ismi aynı zamanda ilk ilçe ismi kaydına eşittir böylece MERKEZ İLÇE olarak listelenen bu 51 kaydın haricinde 922 ilçe kalır. 

```ilçeisimleri2024.csv``` listesini üretmek için python kodunu çalıştırabilirsin:
### python3 extractnamestocsv.py