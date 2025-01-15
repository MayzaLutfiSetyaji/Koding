#Membuat kode program untuk sebuah Vending Machine
Mizone = 4000
Pocari = 6000
Teh_Pucuk = 3000
Beng_beng = 2500

while True:
    print("===SELAMAT DATANG DI VENDING MACHINE===")
    print("Pilihan Menu:")
    print("1. Mizone = Rp.4.000/pcs")
    print("1. Pocari = Rp.6.000/pcs")
    print("1. Teh Pucuk = Rp.3.000/pcs")
    print("1. Beng Beng = Rp.2.500/pcs")
    print("5. Keluar")


    opsi = int(input("Pilih menu (1-5): "))

    if opsi == 1 :
        uang = float(input("Masukkan uang Anda: "))
        jumlah = int(input("Masukkan jumlah yang ingin dibeli: "))        
        if uang >= Mizone:
            total = Mizone * jumlah
            kembalian = uang - total
            print(f"Total harga: {total}")
            print(f"Kembalian: {kembalian}")
        else:
            print("Uang anda tidak cukup")
    elif opsi == 2 :
        uang = float(input("Masukkan uang Anda: "))
        jumlah = int(input("Masukkan jumlah yang ingin dibeli: "))                
        if uang >= Pocari:
            total = Pocari * jumlah
            kembalian = uang - total
            print(f"Total harga: {total}")
            print(f"Kembalian: {kembalian}")
        else:
            print("Uang anda tidak cukup")
    elif opsi == 3 :
        uang = float(input("Masukkan uang Anda: "))
        jumlah = int(input("Masukkan jumlah yang ingin dibeli: "))        
        if uang >= Teh_Pucuk:
            total = Teh_Pucuk * jumlah
            kembalian = uang - total
            print(f"Total harga: {total}")
            print(f"Kembalian: {kembalian}")
        else:
            print("Uang anda tidak cukup")
    elif opsi == 4 :
        uang = float(input("Masukkan uang Anda: "))
        jumlah = int(input("Masukkan jumlah yang ingin dibeli: "))        
        if uang >= Beng_beng:
            total = Beng_beng * jumlah
            kembalian = uang - total
            print(f"Total harga: {total}")
            print(f"Kembalian: {kembalian}")
        else:
            print("Uang anda tidak cukup")
    elif opsi == 5:
        print("Terima kasih telah berbelanja")
        break
    else:
        print("!! Masukkan opsi yang tersedia !!")
        
        
