#Membuat kode program untuk sebuah Vending Machine
def hitung_total_dan_kembalian(harga_satuan, uang, kembalian):
    try:
        total = harga_satuan * jumlah
        kembalian = uang - total
        if kembalian >= 0:
            return total, kembalian
        else:
            return None, "Uang anda tidak cukup"
    except ValueError:
        print("Masukkan angka yang valid untuk uang dan jumlah")
        return None, None

#Daftar harga menggunakan dictionary
daftar_harga = {
    1: ("Mizone", 4000),
    2: ("Pocari", 6000),
    3: ("Teh Pucuk", 3000),
    4: ("Beng-beng", 2500),
}

while True:
    print("===SELAMAT DATANG DI VENDING MACHINE===")
    for k, v in daftar_harga.items():
        print(f"{k}. {v[0]} = Rp.{v[1]}/pcs")
    print("5. Keluar")

    try:
        opsi = int(input("Pilih menu (1-5): "))
        if opsi == 5:
            print("Terima kasih telah berbelanja")
            break

        minuman__pilihan, harga = daftar_harga.get(opsi, (None, None))
        if opsi is None:
            print("Pilihan tidak tersedia")
            continue

        uang = float(input("Masukkan jumlah uang anda: "))
        jumlah = int(input("Masukkan jumlah barang yang dibeli: "))
        total, kembalian = hitung_total_dan_kembalian(harga, uang, jumlah)
        if total is not None:
            print(f"Total harga: {total}")
            print(f"Kembalian: {kembalian}")
    except ValueError:
        print("Masukkan angka yang valid")    