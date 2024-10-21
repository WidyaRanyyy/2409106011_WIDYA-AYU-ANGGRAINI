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

# Variabel users dengan satu akun admin bawaan
users = [
    {"username": "admin", "password": "admin123", "role": "admin"}
]

print("""
▒█▀▀▀█ ▒█▀▀▀ ▒█░░░ ░█▀▀█ ▒█▀▄▀█ ░█▀▀█ ▀▀█▀▀   ▒█▀▀▄ ░█▀▀█ ▀▀█▀▀ ░█▀▀█ ▒█▄░▒█ ▒█▀▀█ 
░▀▀▀▄▄ ▒█▀▀▀ ▒█░░░ ▒█▄▄█ ▒█▒█▒█ ▒█▄▄█ ░▒█░░   ▒█░▒█ ▒█▄▄█ ░▒█░░ ▒█▄▄█ ▒█▒█▒█ ▒█░▄▄ 
▒█▄▄▄█ ▒█▄▄▄ ▒█▄▄█ ▒█░▒█ ▒█░░▒█ ▒█░▒█ ░▒█░░   ▒█▄▄▀ ▒█░▒█ ░▒█░░ ▒█░▒█ ▒█░░▀█ ▒█▄▄█
      
▀█▀ █▀█ █▄▀ █▀█   █▄▄ ▄▀█ █▄░█ █▀▀ █░█ █▄░█ ▄▀█ █▄░█   ░░█ ▄▀█ █▄█ ▄▀█   █▀ █▀▀ █░░ ▄▀█ █░░ █░█
░█░ █▄█ █░█ █▄█   █▄█ █▀█ █░▀█ █▄█ █▄█ █░▀█ █▀█ █░▀█   █▄█ █▀█ ░█░ █▀█   ▄█ ██▄ █▄▄ █▀█ █▄▄ █▄█
""")

# Fungsi untuk login
def login(users):
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
        return user_found  # Mengembalikan objek user yang ditemukan
    else:
        print("Username atau password salah. Silakan coba lagi.")
        return None  # Jika user tidak ditemukan

# Fungsi untuk registrasi akun user baru
def registrasi_pengguna(users):
    print("=== Register Akun User Baru ===")
    username = input("Masukkan username: ")
    password = input("Masukkan password: ")
    
    role = "user"  # Semua registrasi pengguna biasa sebagai "user"

    # Cek apakah username sudah ada
    user_exists = any(user['username'] == username for user in users)
    if user_exists:
        print("Username sudah ada. Silakan coba dengan username lain.")
    else:
        users.append({"username": username, "password": password, "role": role})
        print(f"Pengguna {username} berhasil didaftarkan dengan role {role}!")

# Fungsi khusus untuk admin menambah akun admin lain
def tambah_admin(users, current_user):
    if current_user['role'] != "admin":
        print("Hanya admin yang bisa menambahkan admin baru.")
        return

    print("=== Tambah Admin Baru ===")
    username = input("Masukkan username admin baru: ")
    password = input("Masukkan password admin baru: ")

    # Cek apakah username sudah ada
    user_exists = any(user['username'] == username for user in users)
    if user_exists:
        print("Username sudah ada. Silakan coba dengan username lain.")
    else:
        users.append({"username": username, "password": password, "role": "admin"})
        print(f"Admin {username} berhasil didaftarkan!")

# Fungsi untuk menampilkan inventaris
def tampilkan_inventaris(inventory):
    print("\n=== Daftar Inventaris Toko ===")
    for nama_barang, detail in inventory.items():
        print(f"Nama Barang: {nama_barang}, Stok: {detail['stok']}, Harga: Rp{detail['harga']:,}")

# Fungsi untuk menangani pilihan user dalam menu
def menu_user(inventory):
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
            tampilkan_inventaris(inventory)
        elif pilihan_user == "2":
            print("Keluar dari menu.")
            return "Logout"
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

# Fungsi untuk menangani pilihan admin dalam menu
def menu_admin(inventory, users, current_user):
    while True:
        print("""
                      
█▀▄▀█ █▀▀ █▄░█ █░█   ▄▀█ █▀▄ █▀▄▀█ █ █▄░█
█░▀░█ ██▄ █░▀█ █▄█   █▀█ █▄▀ █░▀░█ █ █░▀█
──────────────── ⋆⋅☆⋅⋆ ─────────────────── 
          1. Lihat Inventaris   
          2. Tambah Barang                
          3. Update Barang      
          4. Hapus Barang  
          5. Tambah Admin Baru        
          6. Logout             
""")
        pilihan_admin = input("Pilih menu: ")

        if pilihan_admin == "1":
            tampilkan_inventaris(inventory)

        elif pilihan_admin == "2":
            tambah_barang(inventory)

        elif pilihan_admin == "3":
            update_barang(inventory)

        elif pilihan_admin == "4":
            hapus_barang(inventory)

        elif pilihan_admin == "5":
            tambah_admin(users, current_user)

        elif pilihan_admin == "6":
            print("Keluar dari menu.")
            break

        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

def tambah_barang(inventory):
    print("=== Tambah Barang Baru ===")
    nama_barang = input("Masukkan nama barang: ")
    stok = int(input("Masukkan stok barang: "))
    harga = int(input("Masukkan harga barang: "))
    
    inventory[nama_barang] = {"stok": stok, "harga": harga}
    print(f"Barang {nama_barang} berhasil ditambahkan!")
    tampilkan_inventaris(inventory)

def update_barang(inventory):
    tampilkan_inventaris(inventory)
    nama_barang = input("Masukkan nama barang yang ingin diupdate: ")
    
    if nama_barang in inventory:
        stok = int(input(f"Masukkan stok baru (sebelumnya: {inventory[nama_barang]['stok']}): "))
        harga = int(input(f"Masukkan harga baru (sebelumnya: Rp{inventory[nama_barang]['harga']:,}): "))
        inventory[nama_barang] = {"stok": stok, "harga": harga}
        print(f"Barang {nama_barang} berhasil diperbarui!")
        tampilkan_inventaris(inventory)
    else:
        print("Nama barang tidak ditemukan.")

def hapus_barang(inventory):
    tampilkan_inventaris(inventory)
    nama_barang = input("Masukkan nama barang yang ingin dihapus: ")
    
    if nama_barang in inventory:
        del inventory[nama_barang]
        print(f"Barang {nama_barang} berhasil dihapus!")
        tampilkan_inventaris(inventory)
    else:
        print("Nama barang tidak ditemukan.")

# Fungsi utama untuk menangani pilihan menu user atau registrasi pengguna
def menu_utama():
    while True:
        pilihan = input("Pilih menu: \n1. Login\n2. Registrasi Akun User Baru\n3. Keluar\nPilihan: ")

        if pilihan == "1":
            user_found = login(users)  # Memanggil fungsi login
            if user_found:
                # Jika user adalah admin
                if user_found['role'] == 'admin':
                    menu_admin(inventory, users, user_found)  # Memanggil menu admin

                # Jika user adalah user biasa
                elif user_found['role'] == 'user':
                    menu_user(inventory)  # Memanggil menu user

        elif pilihan == "2":
            registrasi_pengguna(users)  # Memanggil fungsi registrasi untuk user

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

# Memanggil fungsi utama
menu_utama()
