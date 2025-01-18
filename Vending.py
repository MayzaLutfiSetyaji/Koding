#Membuat kode program untuk sebuah Vending Machine
def hitung_total_dan_kembalian(harga_satuan, uang, jumlah):
    try:
        if harga_satuan <= 0 or jumlah <= 0:
            return None, "Harga satuan dan jumlah tidak boleh kosong"
        total = harga_satuan * jumlah
        kembalian = uang - total
        if kembalian >= 0:
            return total, kembalian
        else: #kondisi ketika kembalian memiliki nilai negatif
            return None, "Uang anda tidak cukup" #None (tidak ada nilai yang dikembalikan)
    except ValueError:
        print("Masukkan angka yang valid untuk uang dan jumlah")
        return None, None #None 1(utk total) dan None 2(utk kembalian)

#Daftar harga menggunakan dictionary dan tuple
daftar_harga = {
    1: ("Mizone", 4000),
    2: ("Pocari", 6000),
    3: ("Teh Pucuk", 3000),
    4: ("Beng-beng", 2500),
}

while True:
    print("===SELAMAT DATANG DI VENDING MACHINE===")
    for k, v in daftar_harga.items():
        print(f"{k}. {v[0]} = Rp.{v[1]}/pcs") #k(key) dan v(value/produk dan harganya)
    print("5. Keluar")

    try:
        opsi = int(input("Pilih menu (1-5): "))
        if opsi == 5:
            print("Terima kasih telah berbelanja")
            break

        minuman__pilihan, harga = daftar_harga.get(opsi, (None, None))
        if opsi is None: #kondisi ketika user tidak mengisi opsi
            print("Harap masukkan pilihan anda")
        elif opsi not in daftar_harga: #kondisi ketika user memilih opsi yang tidak tersedia pada daftar_harga
            print("Plih opsi tidak tersedia")
            continue
    
        uang = float(input("Masukkan jumlah uang anda: "))
        jumlah = int(input("Masukkan jumlah barang yang dibeli: "))
        total, kembalian = hitung_total_dan_kembalian(harga, uang, jumlah)
        if total is not None:
            print(f"Total harga: {total}")
            print(f"Kembalian: {kembalian}")
        elif uang <= 0:
            print("Maaf, Vending Machine ini bukan tempatnya ngutang dawg")
        elif jumlah <= 0:
            print("Lo serius bro??")
        
    except ValueError:
        print("Masukkan angka yang valid")    
print()
print(f"Terima kasih telah berbelanja")