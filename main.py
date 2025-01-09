import time
start_time = time.time()


print("Hello World")
print("Mayza Lutfi Setyaji")
print(
    "Mahasiswa semester 1",
    "\nUniversitas Tidar")

"""
Cara meng-compile
1. Buka terminal
2. Ketik "python -m py_compile "nama file"", maka akan muncul file baru bernama "__pycache__"

Compiled lebih cepat daripada interpreted
"""
print(time.time() - start_time, "detik") #total waktu eksekusi kode program

a = 10
print("Nilai a = ", a)