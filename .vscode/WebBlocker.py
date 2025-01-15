import socket
import time

blocked_websites = ["www.facebook.com", "facebook.com"]

def block_websites(site):
    if site in blocked_websites:
        return True
    else:
        return False
    
host = "127.0.0.1"
port = 53

try: #socket.socket membuat objek socket untuk mendengarkan koneksi
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port)) #s.bind mengikat socket ke alamat IP dan port tertentu
        s.listen() #s.listen mendengarkan koneksi yang masuk
        while True:
            clientsocket, addr = s.accept() #s.accept menerima koneksi dari klien
            print(f"CONNECTION FROM {addr}")
            request = clientsocket.recv(1024).decode()
            print(request)
            site = request.split(" ")[1][2:] #mengekstrak nama host dari permintaan

            if block_websites(site): #memanggil fungsi apakah situs diblokir
                print("BLOCKED")
                clientsocket.send("HTTP/1.1 301 Moved Permanently\nHost: www.example.com\n\n".encode())
            else: #clientsocket.send mengirim respon ke klien
                print("Allowed")
                clientsocket.sendall("HTTP/1.1 200 OK\n\n".encode())
            clientsocket.close()
except KeyboardInterrupt:
    print("\nExiting program.")