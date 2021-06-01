#Nama  : Airell Aristo Subagia 
#NIM   : 71200609 
#Topik : Rekursif
#Link soal : https://www.w3resource.com/python-exercises/data-structures-and-algorithms/python-recursion.php

#Soal 
#buatlah suatu fungsi untuk menambah semua isi dalam list menggunakan rekursif ! 

def jumlah_list(lst) : 
    if len(lst) == 1 : 
        return lst[0]
    else : 
        return lst[0] + jumlah_list(lst[1:])

print(jumlah_list([1,2,3,4]))