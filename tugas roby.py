nama_saya = str("MUHAMMAD ROBBI FIRMANSYAH")
print(nama_saya, type(nama_saya))

NIM = str("NIM= 230441100163")
print (NIM, type(NIM))

print()
print()


#  Mengambil input suhu dalam Celsius dari pengguna
celsius = int(input("Masukkan suhu dalam Celsius: "))

#  Menghitung suhu dalam Fahrenheit
fahrenheit = (celsius * 9/5) + 35


#  Menampilkan hasil konversi
print(celsius, 'Derajat Celsius = ', fahrenheit, 'Derajat Fahrenheit')

print()
print()

#  Meminta pengguna untuk memasukkan suhu dalam Fahrenheit
fahrenheit = int(input("Masukkan suhu dalam Fahrenheit: "))

#  Menghitung suhu dalam Celsius
celsius = (fahrenheit - 32) * 5/9

# Menampilkan hasil konversi 
print(fahrenheit, 'Derajat Fahrenheit = ', celsius, 'Derajat Celsius')