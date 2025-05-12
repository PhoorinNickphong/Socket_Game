# 🔢 Number Guessing Game - Socket Edition

This is a simple multiplayer **number guessing game** built using **Python sockets** for network communication and **Kivy** for graphical interface. Players take turns guessing a number between a given range, and the server provides feedback. The game was created to demonstrate socket programming and GUI handling in Python.

---

## 👨‍💻 Developer

- **นาย ณภัทร จันทร์เมือง 6510110124**
- **นาย ตะวัน สุภาพัฒน์ 6510110158**
- **นาย ภูรินทร์ นิกพงศ์ 6510110371**
- **นาย ศิวกร น้อยหรำ  6510110456**
- **นาย ทวิชา ศิริสุวรรณ์ 6510110168**
- **นางสาว สินายน์ สุนทร 6510110492**

---

## 🧰 Technologies Used

- **Python 3**
- **Kivy** – for GUI
- **Socket** – for TCP/IP communication

---

## 📁 Project Structure

```
Socket_Game/
├── client.py         # Client-side logic and UI
├── server.py         # Server-side logic
├── main.kv           # GUI layout for Kivy
├── main.py           # Main game logic
└── README.md
```

---

## 🌐 How It Works

- One player runs `server.py` to host the game
- Another player connects using `client.py`
- The client tries to guess a number between 1–100
- The server responds with:
  - "Too low!"
  - "Too high!"
  - "Correct!" (with a congratulatory message)

---

## ▶️ Getting Started

### 1. Install dependencies

```bash
pip install kivy
```

### 2. Run the server (Host)

```bash
python server.py
```

### 3. Run the client (Guesser)

```bash
python client.py
```

---

## 🖼️ Console Sample

```
ลองทายเลขสิ 1 ถึง 100 ทาย!: 50
จะมากเก็บไปแล้วน่ะ!! ลองอีกครั้งสิ.
...
ก็ไม่ได้ ก็พอกัน ดวงดี จบๆ!!
```

---

## 📌 Features

- Realtime socket-based interaction
- Thai-language responses and feedback
- Fun and educational intro to network programming
