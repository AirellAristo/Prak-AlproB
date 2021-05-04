#Nama  : Airell Aristo Subagia 
#NIM   : 71200609 
#Topik : Tuple

#soal 
#Buatlah sebuah fungsi untuk menghapus isi dari sebuah tuple !!!
#isi = (1,2,3,4)

def hapusisi(daftar) :
    print(daftar) 
    masuk = []
    for i in daftar : 
        masuk.append(i)
    while True : 
        pil = int(input('Masukkan Angka Yang Mau Dihapus : '))
        if pil in masuk :
            masuk.remove(pil) 
            pil2 = input('Apakah Masih Ingin Menghapus Yang Lain ? (Y/T) ')
            if pil2 == 't' : 
                break 
        else : 
            print('Pilihan Yang Anda Masukkan Tidak Ada')
            pil2 = input('Apakah Masih Ingin Mengganti Angka ? (Y/T) ')
            if pil2 == 't' : 
                break  
    ubah = tuple(masuk)
    print(ubah)
    print(type(ubah))

            
isi = (1,2,3,4)
hapusisi(isi)