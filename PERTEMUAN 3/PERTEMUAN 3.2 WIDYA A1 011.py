print ("=== Menu ===")
print ("1. Penjumlahan")
print ("2. Pengurangan")
print ("3. Perkalian")
print ("4. Pembagian")
pilihan = int(input("Masukkan pilihan"))
if pilihan == 1:
    input1 = int(input("Masukkan angka pertama:"))
    input2 = int(input("Masukkan angka kedua:"))
    print(f"Hasil penjumlahan {input1} + {input2} = {input1 + input2}")
elif pilihan == 2:
    input1 = int(input("Masukkan angka pertama:"))
    input2 = int(input("Masukkan angka kedua:"))
    print(f"Hasil pengurangan {input1} - {input2} = {input1 - input2}")
elif pilihan == 3:
    input1 = int(input("Masukkan angka pertama:"))
    input2 = int(input("Masukkan angka kedua:"))
    print(f"Hasil perkalian {input1} * {input2} = {input1 * input2}")
elif pilihan == 4:
    input1 = int(input("Masukkan angka pertama:"))
    input2 = int(input("Masukkan angka kedua:"))
    print(f"Hasil pembagian {input1} / {input2} = {input1 / input2}")
else:
    print("Pilihan tidak valid")