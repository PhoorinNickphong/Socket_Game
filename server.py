import random
import socket

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)

# สุ่มตัวเลข
number = random.randint(1, 100)
print('The secret number is', number)

# เริ่ม server
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print('Server is ready')
    
    # รอ client เชื่อมต่อ
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        
        # ส่งข้อมูลเริ่มต้นให้ client
        conn.sendall(b'Yin Dee Thon rub kub!!')
        count = 0