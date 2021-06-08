#Nama  : Airell Aristo Subagia
#NIM   : 71200609 
#Topik : Regex 

#Soal 
#buatlah suatu fungsi untuk mengecek jika sandi mengandung huruf besar,kecil,angka maka sandi tersebut valid
#Akan tetapi jika sandi tidak mengandung salah satu ketentuan diatas maka sandi tersebut invalid.

import re 

def cek_pass(sandi) : 
    if re.findall('[A-Z]',sandi) : 
        if re.findall('[a-z]',sandi) :
            if re.findall('[0-9]',sandi) : 
                print('Valid')
            else : 
                print('Invalid')
        else : 
            print('Invalid')
    else : 
        print('Invalid')


sandi = input('Masukkan Sandi : ')

cek_pass(sandi)