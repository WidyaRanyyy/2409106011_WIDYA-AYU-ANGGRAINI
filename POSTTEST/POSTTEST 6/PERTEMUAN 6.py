# daftar_buku = {
#     "Buku1" : "Harry Potter",
#     "Buku2" : "Percy Jackson",
#     "Buku3" : "Twillight"
# }
# print(daftar_buku["Buku1"])
# print(daftar_buku["Buku2"])
# print(daftar_buku["Buku3"])
# print(daftar_buku)

# musik = {
#     "judul" : "All we Know",
#     "judul" : "Something Just Like This"
# }
# print(musik["judul"])

# Biodata = {
#     "Nama" : "WIDYA AYU ANGGRAINI",
#     "Umur": 18,
#     "NIM" : 2409106011,
#     "Jurusan" : "Informatika",
#     "Angkatan" : 24
    # "KRS" : [""],
    # "Mahasiswa_Aktif" :True,
    # "Social Media" : {
    # "Instagram" : "@Rany.Janoor",
    # "Discord" : "\'WidyaRanyy"
    # }
# }

# Biodata["Asal"] = "Bontang"
# print(Biodata)

# Biodata["Umur"] = "20"
# Biodata.update({"Umur" : "20"}) 
# print (Biodata)

# print(Biodata["Nama"])


# print(Biodata["KRS"][1])
# print(Biodata.get("KRS"))
# print(Biodata.get("Alamat")) #none
# print(Biodata.get("Alamat", "Kosong Bang"))

# games = dict(Sekiro = "Action", Pokemon = "Adventure",
# Valorant = "FPS")
# print(games)

# for i, j in Biodata.items():
#     print(f"Key = {i} dan Value = {j}")

# for i in Biodata:
#     print(Biodata[i])

# Film = {
#     "Avenger Endgame" : "Action",
#     "Sherlock Holmes" : "Mystery",
#     "The Conjuring" : "Horror"
# }
# #Sebelum Ditambah

# Film["ZombieLand"] = "Comedy"
# print(Film) #nambah dictionary

# del Film["The Conjuring"]
# print(Film) #terhapus semua

# hapus = Film.pop("The Conjuring")
# print(Film)
# print(f"Key yang dihapus = {hapus}") #mirip fungsi cut di word

# Film.clear()
# print(Film) #menghapus bersih

# print("Jumlah data dalam dict Biodata = ", len(Biodata))

# pinjamdict = Biodata.copy()
# print(pinjamdict)

# key = "apel", "jeruk", "mangga"
# value = 1

# buah = dict.fromkeys(key,value)
# print(buah)

# for i in Film.values():
#     print(i, end =" ")

# print("Film : ", Film.setdefault("Oldbook","horror"))
# print(Film)

# Musik = {
#     "The Chainsmoker" : ["All we Know", "The Paris"],
#     "Alan Walker" : ["Alone", "Lily"],
#     "Neffex" : ["Best of Me", "Memories"]
# }
# for i, j in Musik.items():
#     print(f"Musik milik {i} adalah : ")
#     for song in j:
#         print(song)
#     print("")

# mahasiswa = {
    # 101 : {"Nama" : "Aldy", "Umur" : 19},
    # 111 : {"Nama" : "Abdul", "Umur" : 18}
# }
# print (f"sebelum : {mahasiswa}")
# mahasiswa[101]["Angkatan"] =2023
# del mahasiswa[111]["Umur"]
# print (mahasiswa)

# for key, value in mahasiswa.items():
#     print("ID Mahasiswa : ", key)
#     for key_a, value_a in value.items():
#         print (key_a, " : ", value_a)


Biodata = {}

while True:
    print("1. Tambah")
    print("2. Tampilakan")
    print("3. Exit")
    pilihan =  int(input("(1/2/3) : "))

    if pilihan == 1:
        nama = input("Masukkan nama :")
        umur = input("Masukkan umur :")
        alamat = input("Masukkan alamat :")

        Biodata[nama] = { 
            'Umur' : umur,
            'Alamat' : alamat
        }

    elif pilihan == 2:
        for nama, info in Biodata.items():
            print(f"Nama : {nama}")
            print(f"Umur : {info['Umur']}")
            print(f"Alamat : {info['Alamat']}")

    elif pilihan == 3:
        print("exit ...")
        break

    else:
        print("Invalid ... ... ")