# Input section
nama_lengkap = input("Masukkan nama lengkap: ")  # string
nama_panggilan = input("Masukkan nama panggilan: ")  # string
umur = int(input("Masukkan umur: "))  # integer
prodi = input("Masukkan program studi anda: ")  # string
fakultas = input("Masukkan fakultas anda: ")
nim = int(input("Masukkan NIM: "))  # integer
suhu_badan = float(input("Masukkan suhu badan terakhir (dalam celcius): "))  # float
tinggi_badan = float(input("Masukkan tinggi badan (dalam meter): "))  # float
    
# Output section
print(f"Haloo semua, perkenalkan nama saya {nama_lengkap}, bisa dipanggil {nama_panggilan}, Saat ini saya berumur {umur} tahun.")
print(f"Saya adalah salah satu mahasiswa di prodi {prodi}, fakultas {fakultas}. Nim saya {nim}.")
print(f"Suhu badan terakhir saya adalah {suhu_badan} celcius dan Tinggi badan saya {tinggi_badan} meter")
print(f"Salam kenal semuanyaa")

# Modulus operation on the last 3 digits of NIM
tiga_angka_terakhir = nim % 1000  # get the last three digits
hasil_modulus = tiga_angka_terakhir % 6  # modulus 6
print(f"Tiga angka terakhir NIM saya adalah {tiga_angka_terakhir}, dan jika dimoduluskan 6 hasilnya adalah {hasil_modulus}.")