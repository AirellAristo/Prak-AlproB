#Nama  : Airell Aristo Subagia 
#NIM   : 71200609 
#Grup  : B 
#Topik : Variable,Expressions, dan Statements

#Soal 
#Pada suatu hari Vina disuruh oleh Ibunya untuk membeli bahan-bahan untuk memasak telur dadar.
#Vina diberi uang Rp.50.000 oleh Ibunya. 
#bahan-bahan yang akan dibeli adalah : 2 Telur, 1 kg minyak,3 kg garam. 
#Sebagai seorang yang handal bantulah Vina untuk menghitung harga 
#yang harus dibayar menggunakan program! Dan juga tidak lupa carilah kembaliannya jika ada
#Ps : 1 buah telur berharga Rp. 5.000, 1kg minyak berharga Rp. 10.000, 1kg garam berharga Rp. 3.000

#input 
modal = eval(input('Masukkan uang yang diberi oleh Ibu : Rp. '))
telur = eval(input('Berapa banyak telur yang akan dibeli ? \n '))
harga_telur = eval(input('Masukkan harga 1 butir telur : Rp. '))
minyak = eval(input('Berapa kg minyak yang akan dibeli ? \n '))
harga_minyak = eval(input('Masukkan harga 1 kg minyak : Rp. '))
garam = eval(input('Berapa kg garam yang akan dibeli ? \n '))
harga_garam = eval(input('Masukkan harga 1 kg garam : Rp. '))

#proses 
a = telur * harga_telur
b = minyak * harga_minyak
c = garam * harga_garam
total = a + b + c 
kembalian = modal - total 

#output 
print('Jadi total harga yang harus dibayar oleh Vina adalah Rp. %.2f ' % (total))
print('Maka kembalian yang akan didapatkan oleh Vina adalah Rp. %.2f' % (kembalian))