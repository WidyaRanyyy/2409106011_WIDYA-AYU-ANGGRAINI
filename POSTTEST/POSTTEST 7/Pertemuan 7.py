# def salam():
#     print ("Selamat datang mahasiswa baru 2024")

# salam()


# def salam():
#     print(iso)

# iso = "Salam Iso"
# salam()


# def luas_persegi(sisi):
#     luas = sisi*sisi
#     return luas

# luas = luas_persegi(2)
# print(luas)


# # membuat variabel global
# Nama = "Informatika"
# Mata_Kuliah = "Algoritma dan Pemrograman Dasar"

# # membuat variabel lokal
# def info():
#     Nama = "Teknik Elektro"
#     Mata_Kuliah = "Pengantar Teknik ELektro"

#     # mengakses variabel lokal
# def info2()):   
#     print("Prodi:", Nama)
#     print("Mata Kuliah:", Mata_Kuliah)

# # mengakses variabel global
# print("Prodi:", Nama)
# print("Mata Kuliah:", Mata_Kuliah)
# # memanggil fungsi info
# info()
# info2()


# buku = []

# def show_data():
#     if len(buku) <= 0:
#         print ("Belum Ada data")
#     else:
#         print("ID", "Nama Buku")
#     for indeks in range(len(buku)):
#         print (indeks, buku[indeks])

# def insert_data():
#     buku_baru = input("judul buku : ")
#     buku.append(buku_baru)

# def edit_data():
#     show_data()
#     indeks = int(input9"masukkan ID buku: ")
#     if indeks >= len(buku) or indeks < 0 :
#         print("ID SALAH")
#     else :
#         judul_baru = input("masukkan judul buku baru: ")
#         buku[indeks] = judul_baru

# def delete_data():
#     show_data():
#     indeks = int(input("masukkan id buku"))
#     if indeks > 2 len(buku)
#         print ("ID SALAH")
#     else :
#         buku.remove(buku[indeks])

# def show_menu():
#     print ("menu")
#     print ("1. creaet")
#     print ("2. remove")
#     print ("3. update")
#     print ("4. exit")
#     pilihan = int(input("masukkan pilihan"))
#     if pilihan == 1:
#         show_data()
#     elif pilihan == 2:
#         insert_data()
#     elif pilihan == 3:
#         edit_data()
#     elif pilihan == 4:
#         exit()
#     else:
#         print ("pilihan tidak valid")

# while(True):
#     show_menu()



# #pengakaran
# import math
# angka = 49
# print(math.sqrt(angka))

def luas_segitiga():
    # Meminta input dari user untuk alas dan tinggi
    alas = float(input("Masukkan panjang alas segitiga: "))
    tinggi = float(input("Masukkan tinggi segitiga: "))

def luas_persegipanjang():
    panjang = float(input("masukkan panjang: "))
    lebar = float (input("masukkan lebar: "))
    
    # Menghitung luas segitiga
    luas1 = 0.5 * alas * tinggi
    luas2 = panjang * lebar
    
    # Mengembalikan hasil luas
    return luas1
    return luas2

# Memanggil fungsi dan menampilkan hasilnya
hasil_luas1 = luas_segitiga()
hasil_luas2 = luas_persegipanjang

print(f"Luas segitiga adalah: {hasil_luas1}")
print(f"Luas persegi panjang adalah: {hasil_luas2}")
