import socket
import logging
import random
from validator import port_validation, check_port_open

DEFAULT_PORT = 3030


logging.basicConfig(
    filename="server.log",
    filemode="w",
    format="%(asctime)-15s [%(levelname)s] %(funcName)s: %(message)s",
    level=logging.INFO,
)
logger = logging.getLogger(__name__)


class Server:
    def __init__(self, port_number: int) -> None:
        sock = socket.socket()
        sock.bind(("", port_number))
        sock.listen(0)
        # Socket
        self.sock = sock
        
        logging.info(f"Server Listing to the Port : {port_number}")
        # Wating a new connection
        while True:
            conn, addr = self.sock.accept()
            self.new_connection(conn, addr)

    def new_connection(self, conn, addr):

        logging.info(f"new conection from {addr}")
        msg = ""
        while True:
            
            data = conn.recv(1024)
            
            if not data:
                break
            msg += data.decode()
            conn.send(data)
            data_str = str(data, "utf-8")
            logging.info(f"Receving message from the client : '{data_str}'")


def main():
    port_input = input("choose a port number for the server : ")
    # check weather busy or not 
    port_flag = port_validation(port_input, check_open=True)

    if not port_flag:
        # if busy so choose another port by default
        if not check_port_open(DEFAULT_PORT):
            print(
                f"Port By defalut {DEFAULT_PORT} Busy! Entering Random Port.."
            )
            stop_flag = False
            while not stop_flag:
                current_port = random.randint(49152, 65535)
                print(f"Generate Random Port {current_port}")
                stop_flag = check_port_open(current_port)

            port_input = current_port
        else:
            port_input = DEFAULT_PORT
        print(f"Chosen Port {port_input} By Default")

    server = Server(int(port_input))


if __name__ == "__main__":
    main()
