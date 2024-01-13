import socket, cv2, pickle,struct,imutils, threading

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ADDR = (socket.gethostbyname(socket.gethostname()), 1010)

server.bind(ADDR)

server.listen()
print(f"Server Listening on {ADDR}")

def clientManager(inc, out):
    print("Start")

    while True:
        print("Loop")
        packet = inc.recv(4*1024) # 4K
        out.sendall(packet)
    print("Send")


def roomManager():
    while True:
        c1, a1 = server.accept()
        print("User 1 connected")
        c2, a2 = server.accept()
        print("User 2 connected")
        sub1 = threading.Thread(target=clientManager, args=(c2, c1))
        sub1.start()
        
roomManager()
