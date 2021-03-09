#Nama  : Airell Aristo Subagia 
#NIM   : 71200609 
#Topik : Struktur Kontrol Perulangan

#Pada suatu hari Gilbert mengalami kesusahaan saat mengerjakan tugas yang diberikan oleh gurunya. 
#tugas tersebut adalah mencari berapa hasil kuadrat dari bilangan 1 - 10.
#Bantulah Gilbert mengerjakan tugasnya !!!

x = int(input('Masukkan Nilai : '))
a = 0
bil = 0 

for i in range (0,x) : 
     a += 1
     rumus = a**2
     bil += 1 
     print(bil,'kuadrat adalah ',rumus)