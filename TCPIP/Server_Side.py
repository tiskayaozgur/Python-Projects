#server codes
import socket

SERVER_PORT_NO = 50050

try:
    with socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM, proto=socket.IPPROTO_TCP) as server_sock:
        server_sock.bind(("", SERVER_PORT_NO))
        server_sock.listen(32)

        print("Waiting for connection...")
        client_sock, client_addr =  server_sock.accept()
        print(f"Server'a baglanana client'in ip-port bilgisi={client_addr}")


        while True:
            b = client_sock.recv(1024) #Clienttan gelen byte nesneyı recv ıle aldım.
            text = b.decode("UTF-8") #byte nesnesını strye cevırdım, cunku bu yazıyı ters cevırıp karsı tarafa gonderecegım

            if text == "quit":
                break
            print(text)
            client_sock.send(text[::-1].encode("UTF_8")) #Daha sonra yazıyı byte nesnesıne encode ıle cevırdım kı karsı tarafa gonderebılım.

except Exception as e:
    print(e)
