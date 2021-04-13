#Nama  : Airell Aristo Subagia
#NIM   : 71200609 
#Topik : Files

#Pada suatu hari datang seorang bapak yang kesusahan untuk memasukkan nama nama keluarganya kedalam list.txt nya. 
#Sebagai seorang yang handal.Bapak tersebut meminta kamu untuk membantunya membuat program untuk menuliskan nama
#dan juga memasukkannya kedalam list.txt tersebut! 

while(True): 
    print('===== Keluarga Cemara =====')
    print('1. Tambahkan Nama ')
    print('2. Liat Keluarga')
    print('3. Keluar')
    pil = int(input('Masukkan Pilihan Anda : '))
    if pil == 1 : 
        o_file = open('list.txt','a')
        nama = input('Masukkan Nama Keluarga : ')
        text = nama + '\n'
        o_file.write(text)
    if pil == 2 : 
        o_file = open('list.txt')
        print(o_file.read())
    if pil == 3 : 
        o_file.close()
        break 