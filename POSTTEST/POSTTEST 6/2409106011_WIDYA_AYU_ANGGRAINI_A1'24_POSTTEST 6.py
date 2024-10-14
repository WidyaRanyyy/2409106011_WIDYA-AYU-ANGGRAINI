print("""
▒█▀▀▀█ ▒█▀▀▀ ▒█░░░ ░█▀▀█ ▒█▀▄▀█ ░█▀▀█ ▀▀█▀▀   ▒█▀▀▄ ░█▀▀█ ▀▀█▀▀ ░█▀▀█ ▒█▄░▒█ ▒█▀▀█ 
░▀▀▀▄▄ ▒█▀▀▀ ▒█░░░ ▒█▄▄█ ▒█▒█▒█ ▒█▄▄█ ░▒█░░   ▒█░▒█ ▒█▄▄█ ░▒█░░ ▒█▄▄█ ▒█▒█▒█ ▒█░▄▄ 
▒█▄▄▄█ ▒█▄▄▄ ▒█▄▄█ ▒█░▒█ ▒█░░▒█ ▒█░▒█ ░▒█░░   ▒█▄▄▀ ▒█░▒█ ░▒█░░ ▒█░▒█ ▒█░░▀█ ▒█▄▄█
      
▀█▀ █▀█ █▄▀ █▀█   █▄▄ ▄▀█ █▄░█ █▀▀ █░█ █▄░█ ▄▀█ █▄░█   ░░█ ▄▀█ █▄█ ▄▀█   █▀ █▀▀ █░░ ▄▀█ █░░ █░█
░█░ █▄█ █░█ █▄█   █▄█ █▀█ █░▀█ █▄█ █▄█ █░▀█ █▀█ █░▀█   █▄█ █▀█ ░█░ █▀█   ▄█ ██▄ █▄▄ █▀█ █▄▄ █▄█
""")

# Daftar pengguna dan perannya
users = [
    {"username": "admin", "password": "admin123", "role": "admin"},
]

# Daftar inventaris menggunakan dictionary
inventory = {
    "Semen 40kg": {"stok": 150, "harga": 52000},
    "Pasir 1 Karung": {"stok": 300, "harga": 35000},
    "Batu Bata Merah 1000": {"stok": 100, "harga": 550000},
    "Cat Tembok 5kg": {"stok": 75, "harga": 125000},
    "Besi Beton 12mm 12m": {"stok": 50, "harga": 120000},
    "Paku 3 Inch (1kg)": {"stok": 200, "harga": 18000},
    "Kayu Balok 4x6 4m": {"stok": 80, "harga": 65000},
    "Triplek 9mm 122x244c": {"stok": 120, "harga": 95000},
    "Genteng Tanah Liat": {"stok": 500, "harga": 5000}
}

while True:
    print("\n=== SILAHKAN MELAKUKAN REGISTRASI LALU KEMBALI LOGIN ===")
    print("1. Login")
    print("2. Register")
    print("3. Keluar")

    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        # Login
        print("=== Login ===")
        username = input("Username: ")
        password = input("Password: ")

        user_found = None
        for user in users:
            if user['username'] == username and user['password'] == password:
                user_found = user
                break

        if user_found:
            print(f"Selamat datang, {username}!")
        else:
            print("Username atau password salah. Silakan coba lagi.")
            continue

        # Jika user adalah admin
        if user_found['role'] == 'admin':
            while True:
                print("""
                      
█▀▄▀█ █▀▀ █▄░█ █░█   ▄▀█ █▀▄ █▀▄▀█ █ █▄░█
█░▀░█ ██▄ █░▀█ █▄█   █▀█ █▄▀ █░▀░█ █ █░▀█
──────────────── ⋆⋅☆⋅⋆ ─────────────────── 
          1. Lihat Inventaris   
          2. Tambah Barang                
          3. Update Barang      
          4. Hapus Barang            
          5. Logout             
                      
""")
                pilihan_admin = input("Pilih menu: ")

                if pilihan_admin == "1":
                    # Menampilkan inventaris
                    print("\n=== Daftar Inventaris Toko ===")
                    for nama_barang, detail in inventory.items():
                        print(f"Nama Barang: {nama_barang}, Stok: {detail['stok']}, Harga: Rp{detail['harga']:,}")

                elif pilihan_admin == "2":
                    # Tambah barang
                    print("=== Tambah Barang Baru ===")
                    nama_barang = input("Masukkan nama barang: ")
                    stok = int(input("Masukkan stok barang: "))
                    harga = int(input("Masukkan harga barang: "))

                    inventory[nama_barang] = {"stok": stok, "harga": harga}
                    print(f"Barang {nama_barang} berhasil ditambahkan!")

                elif pilihan_admin == "3":
                    # Update barang
                    print("\n=== Daftar Inventaris Toko ===")
                    for nama_barang, detail in inventory.items():
                        print(f"Nama Barang: {nama_barang}, Stok: {detail['stok']}, Harga: Rp{detail['harga']:,}")

                    nama_barang = input("Masukkan nama barang yang ingin diupdate: ")
                    if nama_barang in inventory:
                        stok = int(input(f"Masukkan stok baru (sebelumnya: {inventory[nama_barang]['stok']}): "))
                        harga = int(input(f"Masukkan harga baru (sebelumnya: Rp{inventory[nama_barang]['harga']:,}): "))
                        inventory[nama_barang] = {"stok": stok, "harga": harga}
                        print(f"Barang {nama_barang} berhasil diperbarui!")
                    else:
                        print("Nama barang tidak ditemukan.")

                elif pilihan_admin == "4":
                    # Hapus barang
                    print("\n=== Daftar Inventaris Toko ===")
                    for nama_barang, detail in inventory.items():
                        print(f"Nama Barang: {nama_barang}, Stok: {detail['stok']}, Harga: Rp{detail['harga']:,}")

                    nama_barang = input("Masukkan nama barang yang ingin dihapus: ")
                    if nama_barang in inventory:
                        del inventory[nama_barang]
                        print(f"Barang {nama_barang} berhasil dihapus!")
                    else:
                        print("Nama barang tidak ditemukan.")

                elif pilihan_admin == "5":
                    break

                else:
                    print("Pilihan tidak valid. Silakan coba lagi.")

        # Jika user adalah pengguna biasa
        else:
            while True:
                print("""
                      
█▀▄▀█ █▀▀ █▄░█ █░█   █▀█ █▀▀ █▄░█ █▀▀ █▀▀ █░█ █▄░█ ▄▀█
█░▀░█ ██▄ █░▀█ █▄█   █▀▀ ██▄ █░▀█ █▄█ █▄█ █▄█ █░▀█ █▀█
─────────────────────── ⋆⋅☆⋅⋆ ───────────────────────── 
                1. Lihat Inventaris    
                2. Logout 
                                      
""")
                pilihan_user = input("Pilih menu: ")

                if pilihan_user == "1":
                    # Menampilkan inventaris
                    print("\n=== Daftar Inventaris Toko ===")
                    for nama_barang, detail in inventory.items():
                        print(f"Nama Barang: {nama_barang}, Stok: {detail['stok']}, Harga: Rp{detail['harga']:,}")

                elif pilihan_user == "2":
                    break

                else:
                    print("Pilihan tidak valid. Silakan coba lagi.")

    elif pilihan == "2":
        # Registrasi pengguna baru
        print("=== Register Pengguna Baru ===")
        username = input("Masukkan username: ")
        password = input("Masukkan password: ")
        role = input("Masukkan role (admin/user): ").lower()

        if role not in ["admin", "user"]:
            print("Role tidak valid. Silakan coba lagi.")
        else:
            # Cek apakah username sudah ada
            user_exists = False
            for user in users:
                if user['username'] == username:
                    print("Username sudah ada. Silakan coba dengan username lain.")
                    user_exists = True
                    break

            if not user_exists:
                users.append({"username": username, "password": password, "role": role})
                print(f"Pengguna {username} berhasil didaftarkan dengan role {role}!")

    elif pilihan == "3":
        print("""
              
▀▀█▀▀ ▒█▀▀▀ ▒█▀▀█ ▀█▀ ▒█▀▄▀█ ░█▀▀█ ▒█░▄▀ ░█▀▀█ ▒█▀▀▀█ ▀█▀ ▒█░▒█ 
░▒█░░ ▒█▀▀▀ ▒█▄▄▀ ▒█░ ▒█▒█▒█ ▒█▄▄█ ▒█▀▄░ ▒█▄▄█ ░▀▀▀▄▄ ▒█░ ▒█▀▀█ 
░▒█░░ ▒█▄▄▄ ▒█░▒█ ▄█▄ ▒█░░▒█ ▒█░▒█ ▒█░▒█ ▒█░▒█ ▒█▄▄▄█ ▄█▄ ▒█░▒█
             
               TELAH MENGGUNAKAN SISTEM INI
""")
        break

    else:
        print("Pilihan tidak valid. Silakan coba lagi.")
