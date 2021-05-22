#client codes
import socket

SERVER_PORT_NO = 50050
SERVER_HOSTNAME = "127.0.0.1"

try:
    with socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM, proto=socket.IPPROTO_TCP) as client_sock:
        client_sock.connect((SERVER_HOSTNAME, SERVER_PORT_NO))
        print("Connnected")


        while True:
            b = text.encode("UTF-8") #Gırılen str'yı byte nesnesıne cevırdım kı bunu send ıle server tarafına gonderebıleyım.
            text = input("Please enter any word or sentence=")
            client_sock.send(b)

            if text == "quit":
                break

            b = client_sock.recv(1024)
            text = b.decode("UTF-8") #serverdan gelen cevap byte oldugu ıcın bunu strye cevırıp prınt ıle bastım, yanı yazının tersını
            print(text)

except Exception as e:
    print(e)
