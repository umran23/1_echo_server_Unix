import socket
from validator import port_validation, ip_validation

DEFAULT_PORT = 3030
DEFAULT_IP = "127.0.0.1"


class Client:
    def __init__(self, server_ip: str, port_number: int) -> None:
        sock = socket.socket()
        sock.setblocking(1)
        sock.connect((server_ip, port_number))
        self.sock = sock
        #Woring with data from the user
        self.user_processing()
        
        self.sock.close()

    def user_processing(self):
        while True:
            msg = input("-> ")
            
            if msg == "exit": break
            
            if msg == "": msg = "None"

            
            self.sock.send(msg.encode())
            
            data = self.sock.recv(1024)
            print(f"Ответ от сервера: {data.decode()}")


def main():
    port_input = input("Enter Server Port Number -> ")
    port_flag = port_validation(port_input)
    # if many users input in at the same time
    if not port_flag:
        port_input = DEFAULT_PORT
        print(f"Chosen Port {port_input} By Default")

    ip_input = input("Enter Server IP Address -> ")
    ip_flag = ip_validation(ip_input)
    
    if not ip_flag:
        ip_input = DEFAULT_IP
        print(f"Chosen IP Address {ip_input} By Default")

    client = Client(ip_input, int(port_input))


if __name__ == "__main__":
    main()
