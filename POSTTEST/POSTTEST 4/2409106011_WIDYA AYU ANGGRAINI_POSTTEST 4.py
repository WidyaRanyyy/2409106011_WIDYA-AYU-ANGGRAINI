daftarkan_username=input("daftarkan nama anda:")
daftarkan_password=input("daftarkan password anda:")

salah=0

while salah <3:
    masukkan_nama=input("masukkan nama anda:")
    masukkan_password=input("masukkan password akun kamu:")
    if daftarkan_username==masukkan_nama and daftarkan_password==masukkan_password:
        print("login berhasil")
        while True:
                
            #pilih gender
            print("Pilih Jenis Kelamin")
            print("A. Pria")
            print("B. Wanita")
            gender = str(input("Pilihan (A/B): "))

            if gender not in ['A', 'B']:
                    print("Pilihan tidak valid!")
                    exit()
            #input umur, berat badan, tinggi badan
            berat_badan = float(input("Masukkan berat badan (gram): "))
            tinggi_badan = float(input("Masukkan tinggi badan (km): "))
            umur = int(input("Masukkan umur: "))

            #rumus BMR
            bmr_pria = (0.01 * berat_badan) + (625000 * tinggi_badan) - (5 * umur) + 5
            bmr_wanita = (0.01 * berat_badan) + (625000 * tinggi_badan) - (5 * umur) - 161

            #menentukan level aktivitas
            print ("Terdapat tiga opsi pada level aktivitas yaitu minimal, sedang, dan tinggi")
            aktivitas = str(input("Masukkan level aktivitas: "))

            if gender == "A":
                if aktivitas == "minimal":
                    tdee = bmr_pria * 1.25
                elif aktivitas == "sedang":
                    tdee = bmr_pria * 1.36
                elif aktivitas == "tinggi":
                    tdee = bmr_pria * 1.72
                else:
                    print ("invalid")

            elif gender == "B":
                if aktivitas == "minimal":
                    tdee = bmr_wanita * 1.25
                elif aktivitas == "sedang":
                    tdee = bmr_wanita * 1.36
                elif aktivitas == "tinggi":
                    tdee = bmr_wanita * 1.72
                else:
                    print ("invalid")

            print(f"\nKebutuhan Kalori Harian Anda (TDEE) adalah: {tdee:.2f} kalori per hari.")

            # Menanyakan apakah pengguna ingin mengulang
            ulangi = input("Apakah Anda ingin menghitung lagi? Ketik 'ya' untuk melanjutkan, atau 'exit' untuk keluar: ")
            if ulangi == "exit":
                    print("Program dihentikan.")
                    exit()
            
    else:
        print("login gagal")
        salah+=1
print("Anda keluar prorgam")