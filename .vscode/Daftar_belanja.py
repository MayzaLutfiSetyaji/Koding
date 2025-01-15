def tambah_item(daftar_belanja):
    item = input("Masukkan item yang ingin ditambahkan: ")
    daftar_belanja.append(item)
    print(f"Item {item} berhasil ditambahkan")

def hapus_item(daftar_belanja):
    item = input("Masukkan item yang ingin dihapus ")
    if item in daftar_belanja:
        daftar_belanja.remove(item)
        print(f"Item {item} berhasil dihapus")
    else:
        print(f"Item tidak ada di daftar belanja")

def tampilkan_daftar(daftar_belanja):
    print("Daftar Belanja:")
    for item in daftar_belanja:
        print("-" + item)

def simpan_daftar(daftar_belanja, nama_file):
    with open (nama_file, "w") as file:
        for item in daftar_belanja:
            file.write(item + "\n")

def baca_daftar(nama_file):
    daftar_belanja = []
    try:
        with open(nama_file, "r") as file:
            for line in file:
                daftar_belanja.append(line.strip())
    except FileNotFoundError:
        print(f"File daftar belanja belum ada. Daftar belanja baru akan dibuat")
        return daftar_belanja

def main():
    daftar_belanja = []
    nama_file = "daftar_belanja.txt"
    while True:
        print(
            "\nMenu:",
            "\n1. Tambah item",
            "\n2. Hapus item",
            "\n3. Tampilkan daftar",
            "\n4. Keluar"
        )
    
        opsi = input("Pilih opsi (1-4): ")

        if opsi == "1":
            tambah_item(daftar_belanja)
        elif opsi == "2":
            hapus_item(daftar_belanja)
        elif opsi == "3":
            tampilkan_daftar(daftar_belanja)
        elif opsi == "4":
            simpan_daftar(daftar_belanja, nama_file)
            print(f"Terima Kasih")
            break
        else:
            print("!! Pilih opsi yang tersedia !!")

    if __name__ == "__main__":
        main()
