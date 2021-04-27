#Nama  : Airell Aristo Subagia  
#NIM   : 71200609 
#Topik : Dictionaries

#Soal 
#Pada suatu hari Riki membangun sebuah restoran dengan menu sebagai berikut 
#menu = {'ayam goreng':15000,'kentang goreng':5000,'sosis bakar':7000}
#setelah melihat menu tersebut. Riki meminta tolong kepadamu untuk dibuatkan suatu program menggunakan dictionaries 

menu = {'ayam goreng':15000,'kentang goreng':5000,'sosis bakar':7000}
total = 0 

while (True) : 
    print('=== Menu Makanan ===')
    print('1. Ayam Goreng')
    print('2. Kentang Goreng')
    print('3. Sosis Bakar')
    print('4. Exit')
    pilihan = int(input('Masukkan Pilihan Anda : '))
    if pilihan == 1 : 
        n = int(input('Berapa Banyak Yang Ingin Dibeli : '))
        hitung = menu['ayam goreng'] * n 
        total += hitung 
        print('Total Sementara adalah Rp.',total)
        tambah = input('Apakah Masih Ingin Tambah (y/t) : ')
        if tambah == 't' : 
            print('Total Yang Harus Dibayar Adalah Rp.',total)
            print('Terima Kasih')
            break
    if pilihan == 2 : 
        n = int(input('Berapa Banyak Yang Ingin Dibeli : '))
        hitung = menu['kentang goreng']*n
        total += hitung 
        print('Total Sementara adalah Rp.',total)
        tambah = input('Apakah Masih Ingin Tambah (y/t) : ')
        if tambah == 't' : 
            print('Total Yang Harus Dibayar Adalah Rp.',total)
            print('Terima Kasih')
            break
    if pilihan == 3 : 
        n = int(input('Berapa Banyak Yang Ingin Dibeli : ')) 
        hitung = menu['sosis bakar']*n 
        total += hitung 
        print('Total Sementara adalah Rp.',total)
        tambah = input('Apakah Masih Ingin Tambah (y/t) : ')
        if tambah == 't' : 
            print('Total Yang Harus Dibayar Adalah Rp.',total)
            print('Terima Kasih')
            break
    if pilihan == 4 : 
        if total == 0 : 
            print('Terima Kasih')
            break
        else : 
            print('Total Yang Harus Dibayar Adalah Rp.',total)
            print('Terima Kasih')
            break