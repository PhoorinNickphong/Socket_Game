import socket

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65432        # The port used by the server

# เชื่อมต่อกับ server
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    print('Connected to server')    

    # รับข้อมูลจาก server ว่าเริ่มเกมหรือยัง
    data = s.recv(1024)
    print(data.decode())
    
    while True:
        guess = input('ลองทายเลขสิ 1 ถึง 100 หนะ!: ')
        
        # ส่งข้อมูลตัวเลขให้ server
        s.sendall(guess.encode())
        
        # รับข้อมูลจาก server
        data = s.recv(1024)
        message = data.decode()

        # ตรวจสอบผลลัพธ์
        if message == 'correct':
            print('ก็ไม่ได้เก่งหนิ ดวงดีเฉยๆ!!')
            break
        elif message == 'small':
            print('ต้องมากกว่านั้นสิ!!. ลองอีกครั้งซิ.')
        elif message == 'large':
            print('จะมากเกินไปแล้วน่ะ!!. ลองอีกครั้งซิ.')
        elif message == 'limit':
            print('ถ้าจะผิดขนาดนี้เลิกเล่นเหอะ!!. เหยาะ แหยะ:p')
            break