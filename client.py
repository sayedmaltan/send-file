import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 50000))

# استقبال اسم الملف
# filename = client_socket.recv(1024).decode().strip()

with open("filename.mp", "wb") as f:
    while True:
        data = client_socket.recv(1024)  # نفس النمط
        if not data:
            break
        f.write(data)

print("File received")
client_socket.close()