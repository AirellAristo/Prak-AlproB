#Nama  : Airell Aristo Subagia 
#NIM   : 71200609 
#Topik : Pengolahan String


#airell@gmail.com
#aristo@yahoo.co.id
#subagia@hotmail.com
#Pisahkanlah nama pengguna dengan penyedia layanan email diatas !!!
#Nama Pengguna harus diawali dengan huruf besar

email = input('Masukkan email anda : ')
x = email.find('@')
a = email.capitalize()

print('Nama anda adalah',a[:x],'layanan email yang anda gunakan adalah',a[x+1:])