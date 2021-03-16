#Nama  : Airell Aristo Subagia 
#NIM   : 71200609 
#Topik : Percabangan dan Perulangan Kompleks 

#Buatlah Sebuah Program penjumlahan dan pengurangan menggunakan While.
#Yang dimana jika user memasukkan perintah keluar dan tidak ada nilai yang dimasukkan 
#Maka pesan yang dibuat harus berbeda.

a = 0 
b = 0 

while (True) : 
    print('1.Penjumlahan')
    print('2.Pengurangan')
    print('3.Keluar')
    pil = int(input('Masukkan Pilihan : '))
    if pil == 1 : 
        a = int(input('Masukkan Nilai : '))
        b += a
    elif pil == 2 : 
        a = int(input('Masukkan Nilai : '))
        b -= a
    elif pil == 3 : 
        if b != 0 : 
            print('Maka Hasilnya Adalah',b)
            break
        else : 
            print('Belum ada nilai yang dimasukkan')
            break
    else : 
        print('Pilihan Yang Anda Masukkan Tidak Ada.')
        break