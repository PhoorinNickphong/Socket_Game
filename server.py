import random

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)

# สุ่มตัวเลข
number = random.randint(1, 100)
print('The secret number is', number)