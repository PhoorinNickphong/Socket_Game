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

        # รับข้อมูลจาก client
        while True:
            data = conn.recv(1024)
            
            # ตรวจสอบข้อมูล
            if not data:
                break
            
            # แปลงข้อมูลเป็นตัวเลข
            guess = int(data.decode())
            count += 1
            
            # ตรวจสอบค่า
            if guess == number:
                conn.sendall(b'correct')
                break
            elif count >= 10:
                conn.sendall(b'limit')
                break
            elif guess < number:
                conn.sendall(b'small')
            elif guess > number:
                conn.sendall(b'large')