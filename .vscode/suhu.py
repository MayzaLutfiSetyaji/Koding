#Kode program untuk konversi suhu
def konversi_suhu():
    print("\nSELAMAT DATANG PADA KALKULATOR KONVERSI SUHU\n")
    print(
        "Pilih opsi satuan suhu yang tersedia",
        "\n1. Celcius",
        "\n2. Reamur",
        "\n3. Fahrenheit",
        "\n4. Kelvin"
        )
#Menginput opsi dari berbagai suhu
while True:
    try:
        suhu = input("Masukkan pilihan anda: ")
        if suhu in ["1", "Celcius"]:
            celcius = float(input("Masukkan suhu: "))
            reamur = (4/5) * celcius
            fahrenheit = ((9/5) * celcius) + 32
            kelvin = celcius + 273

        elif suhu in ["2","Reamur"]:
            reamur = float(input("Masukkan suhu: "))
            celcius = (5/4) * reamur
            fahrenheit = ((9/4) * reamur) + 32
            kelvin = ((5/4) * reamur) + 273
    
        elif suhu in ["3", "Fahrenheit"]:
            fahrenheit = float(input("Masukkan suhu: "))
            celcius = 5/9 * (fahrenheit - 32)
            reamur = 4/9 * (fahrenheit - 32)
            kelvin = 5/9 * (fahrenheit - 32) + 273

        elif suhu in ["4", "Kelvin"]:
            kelvin= float(input("Masukkan suhu: "))
            celcius = kelvin - 273
            reamur = 4/5 * (kelvin - 273)
            fahrenheit = 9/5 * (kelvin - 273) + 32

        else:
            print("!! Harap pilih opsi yang tersedia !!")
            continue
    

        print(f"Suhu dalam Celcius: {celcius:.2f}")
        print(f"Suhu dalam Reamur: {reamur:.2f}")
        print(f"Suhu dalam Kelvin: {kelvin:.2f}")
        print(f"Suhu dalam Fahrenheit: {fahrenheit:.2f}")

        ulang = str(input("Apakah anda ingin mengulangnya? (y/n):"))
        if ulang.lower() != "y":
            break
    
    except ValueError:
        print("!! Masukkan suhu dengan angka !!")

if __name__ == "__main__":
    konversi_suhu()