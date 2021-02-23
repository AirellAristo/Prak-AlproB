#Nama  : Airell Aristo Subagia 
#NIM   : 71200609
#Grup  : B 
#Topik : LAB 3-Struktur Kontrol Percabangan 

#Pada suatu hari Vina ingin mengetahui seberapa jauh teman-temannya mengetahui tentang dirinya. 
#Oleh karena itu kamu sebagai seorang programer handal dimintai untuk membuatkan sebuah kuis kecil. 
#Soal yang akan ditanyakan adalah : Siapa nama (vina), Berapa Umurnya (17), Berasal darimana(Sulawesi). 
#Bantulah Vina untuk membuat kuis tersebut !!! 

print('===== KUIS VINA =====')
main = input('Apakah kamu ingin bermain ? (Y/T) ')

if main == 'y' : 
    print('Baiklah mari kita mulai')
    soal1 = input('Siapakah nama temanmu ? ')
    if soal1 == 'vina' : 
        print('Ok kamu mengenalnya dengan cukup baik !!!')
        soal2 = int(input('Berapakah Umur Vina ? '))
        if soal2 == 17 :
            print('Wow,namkanya kamu sangat mengenalnya !!!')
            soal3 = input('Berasal darimanakah Vina ? ')
            if soal3 == 'sulawesi': 
                print('Selamat kamu adalah teman sejatinya Vina !!!')
            else : 
                print('Kayaknya kamu belum kenal dekat deh.')
        else : 
            print('Nampaknya yang tadi hanya hoki saja. ')
    else : 
        print('Masa kamu tidak mengenal teman sendiri, payah !!!')
else : 
    print('Baiklah,Sampai Jumpa !!!')