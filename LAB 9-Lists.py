#Nama  : Airell Aristo Subagia 
#NIM   : 71200609 
#Topik : Lists

#Soal 
#Pada suatu hari Arlin di beri tugas oleh gurunya untuk menghitung suatu angka berbasis random ke basis 10
#Akan tetapi Arlin sedikit kesulitan untuk mengerjakannya.oleh karena itu bantulah temanmu dengan program buatanmu! 

simpan = []
total = 0

digit = int(input('Masukkan Berapa Digit Angka : '))
basis = int(input('Masukkan Basis Awal : '))

for i in range(digit) : 
    angka = int(input('Masukkan Digit :'))
    simpan.append(angka)

pangkat = digit - 1 

for i in simpan : 
    i = i * (basis**pangkat)
    total += i
    pangkat -= 1 

print(total)