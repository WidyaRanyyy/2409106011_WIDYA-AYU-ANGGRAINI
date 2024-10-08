print( 
"""

     ▒█▀▀▀█ ▒█▀▀▀ ▒█░░░ ░█▀▀█ ▒█▀▄▀█ ░█▀▀█ ▀▀█▀▀   ▒█▀▀▄ ░█▀▀█ ▀▀█▀▀ ░█▀▀█ ▒█▄░▒█ ▒█▀▀█ 
     ░▀▀▀▄▄ ▒█▀▀▀ ▒█░░░ ▒█▄▄█ ▒█▒█▒█ ▒█▄▄█ ░▒█░░   ▒█░▒█ ▒█▄▄█ ░▒█░░ ▒█▄▄█ ▒█▒█▒█ ▒█░▄▄ 
     ▒█▄▄▄█ ▒█▄▄▄ ▒█▄▄█ ▒█░▒█ ▒█░░▒█ ▒█░▒█ ░▒█░░   ▒█▄▄▀ ▒█░▒█ ░▒█░░ ▒█░▒█ ▒█░░▀█ ▒█▄▄█
            
▀█▀ █▀█ █▄▀ █▀█   █▄▄ ▄▀█ █▄░█ █▀▀ █░█ █▄░█ ▄▀█ █▄░█   ░░█ ▄▀█ █▄█ ▄▀█   █▀ █▀▀ █░░ ▄▀█ █░░ █░█
░█░ █▄█ █░█ █▄█   █▄█ █▀█ █░▀█ █▄█ █▄█ █░▀█ █▀█ █░▀█   █▄█ █▀█ ░█░ █▀█   ▄█ ██▄ █▄▄ █▀█ █▄▄ █▄█
"""
)

# Daftar pengguna dan perannya
users = [
    {"username": "admin", "password": "admin123", "role": "admin"},
]

# Daftar inventaris menggunakan Nested List (nama_barang, stok, harga)
inventory = [
    ["Semen 40kg", 150, 52000],
    ["Pasir 1 Karung", 300, 35000],
    ["Batu Bata Merah 1000",	100, 550000],
    ["Cat Tembok 5kg", 75, 125000],
    ["Besi Beton 12mm 12m", 50, 120000],
    ["Paku 3 Inch (1kg)", 200, 18000],
    ["Kayu Balok 4x6 4m", 80, 65000],
    ["Triplek 9mm 122x244c", 120, 95000],
    ["Genteng Tanah Liat", 500, 5000]
]

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
                print( 
"""
█▀▄▀█ █▀▀ █▄░█ █░█   ▄▀█ █▀▄ █▀▄▀█ █ █▄░█
█░▀░█ ██▄ █░▀█ █▄█   █▀█ █▄▀ █░▀░█ █ █░▀█
──────────────── ⋆⋅☆⋅⋆ ─────────────────── 
          1. Lihat Inventaris   
          2. Tambah Barang                
          3. Update Barang      
          4. Hapus Barang            
          5. Logout             
"""
)
                pilihan_admin = input("Pilih menu: ")

                if pilihan_admin == "1":
                    # Menampilkan inventaris
                    print("\n=== Daftar Inventaris Toko ===")
                    for i, item in enumerate(inventory, start=1):
                        print(f"{i}. Nama Barang: {item[0]}, Stok: {item[1]}, Harga: Rp{item[2]:,}")

                elif pilihan_admin == "2":
                    # Tambah barang
                    print("=== Tambah Barang Baru ===")
                    nama_barang = input("Masukkan nama barang: ")
                    stok = int(input("Masukkan stok barang: "))
                    harga = int(input("Masukkan harga barang: "))

                    inventory.append([nama_barang, stok, harga])
                    print(f"Barang {nama_barang} berhasil ditambahkan!")

                elif pilihan_admin == "3":
                    # Update barang
                    print("\n=== Daftar Inventaris Toko ===")
                    for i, item in enumerate(inventory, start=1):
                        print(f"{i}. Nama Barang: {item[0]}, Stok: {item[1]}, Harga: Rp{item[2]:,}")

                    try:
                        index = int(input("Masukkan nomor barang yang ingin diupdate: ")) - 1
                        nama_barang = input(f"Masukkan nama barang baru (sebelumnya: {inventory[index][0]}): ")
                        stok = int(input(f"Masukkan stok baru (sebelumnya: {inventory[index][1]}): "))
                        harga = int(input(f"Masukkan harga baru (sebelumnya: Rp{inventory[index][2]:,}): "))

                        inventory[index] = [nama_barang, stok, harga]
                        print(f"Barang {nama_barang} berhasil diperbarui!")
                    except (ValueError, IndexError):
                        print("Input tidak valid atau nomor barang tidak valid.")

                elif pilihan_admin == "4":
                    # Hapus barang
                    print("\n=== Daftar Inventaris Toko ===")
                    for i, item in enumerate(inventory, start=1):
                        print(f"{i}. Nama Barang: {item[0]}, Stok: {item[1]}, Harga: Rp{item[2]:,}")

                    try:
                        index = int(input("Masukkan nomor barang yang ingin dihapus: ")) - 1
                        deleted_item = inventory.pop(index)
                        print(f"Barang {deleted_item[0]} berhasil dihapus!")
                    except (ValueError, IndexError):
                        print("Input tidak valid atau nomor barang tidak valid.")

                elif pilihan_admin == "5":
                    break

                else:
                    print("Pilihan tidak valid. Silakan coba lagi.")

        # Jika user adalah pengguna biasa
        else:
            while True:
                print(
"""
█▀▄▀█ █▀▀ █▄░█ █░█   █▀█ █▀▀ █▄░█ █▀▀ █▀▀ █░█ █▄░█ ▄▀█
█░▀░█ ██▄ █░▀█ █▄█   █▀▀ ██▄ █░▀█ █▄█ █▄█ █▄█ █░▀█ █▀█
─────────────────────── ⋆⋅☆⋅⋆ ───────────────────────── 
                1. Lihat Inventaris    
                2. Logout                 
"""
)

                pilihan_user = input("Pilih menu: ")

                if pilihan_user == "1":
                    # Menampilkan inventaris
                    print("\n=== Daftar Inventaris Toko ===")
                    for i, item in enumerate(inventory, start=1):
                        print(f"{i}. Nama Barang: {item[0]}, Stok: {item[1]}, Harga: Rp{item[2]:,}")
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
        print(
"""
▀▀█▀▀ ▒█▀▀▀ ▒█▀▀█ ▀█▀ ▒█▀▄▀█ ░█▀▀█ ▒█░▄▀ ░█▀▀█ ▒█▀▀▀█ ▀█▀ ▒█░▒█ 
░▒█░░ ▒█▀▀▀ ▒█▄▄▀ ▒█░ ▒█▒█▒█ ▒█▄▄█ ▒█▀▄░ ▒█▄▄█ ░▀▀▀▄▄ ▒█░ ▒█▀▀█ 
░▒█░░ ▒█▄▄▄ ▒█░▒█ ▄█▄ ▒█░░▒█ ▒█░▒█ ▒█░▒█ ▒█░▒█ ▒█▄▄▄█ ▄█▄ ▒█░▒█
             
               TELAH MENGGUNAKAN SISTEM INI
"""
)
        break

    else:
        print("Pilihan tidak valid. Silakan coba lagi.")
