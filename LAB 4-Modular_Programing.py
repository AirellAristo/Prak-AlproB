# Nama  : Airell Aristo Subagia 
# NIM   : 71200609 
# Topik : Modular Programing (fungsi)

# Vasan mempunyai 2 buah barang yang ingin dia jual. 
# Barang - barangnya adalah telur, roti 
# Harga : 1 telur Rp. 3.000 , 1 roti Rp. 5.000
# Bantulah Vasan dalam menghitung harga yang harus dibayar oleh setiap pembeli. 

def telur(buahT,hargaT) : 
    rumusT = buahT * hargaT
    return rumusT
def roti(buahR,hargaR) : 
    rumusR = buahR * hargaR 
    return rumusR 

def pilihan (opsi) : 
    if opsi == 1 : 
        buahT = int(input('Berapa banyak telur yang anda beli ? \n '))
        hargaT = int(input('Berapa harga 1 buah telur ? \n '))
        print('Total harga yang harus anda bayar adalah %.2f '% (telur(buahT,hargaT)))
    elif opsi == 2 : 
        buahR = int(input('Berapa banyak roti yang anda beli ? \n'))
        hargaR = int(input('Berapa harga 1 buah roti ? \n'))
        print('Total harga yang harus anda bayar adalah Rp. %.2f ' % (roti(buahR,hargaR)))
    else : 
        print('Maaf pilihan yang anda masukkan tidak tersedia !!!')

print('===== Toko Vasan =====')
print('1.Telur')
print('2.Roti')
opsi = int(input('Masukkan pilihan yang anda inginkan : '))
pilihan(opsi)
