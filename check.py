import socket
from typing import Any


def port_validation(value: Any, check_open: bool = False) -> bool:
    #check if the port is correct
    try:
        # converting to int number
        value = int(value)
        
        if 1 <= value <= 65535:
            # if Port Busy
            if check_open:
                return check_port_open(value)
            print(f"Correct Port {value}")
            return True

        print(f"Wrong Value {value} for the Port")
        return False

    except ValueError:
        print(f"Value {value} is not a number")
        return False


def check_port_open(port: int) -> bool:
  
    #check if the port busy or if its avaliable
  
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = sock.connect_ex(('127.0.0.1', port))
    sock.close()
    if result == 0:
        print(f"Port {port} Busy")
        return False
    else:
        print(f"Port {port} Free")
        return True


def ip_validation(address: str) -> bool:
    #check IP V4
    error_message = f"Wrong ip-address {address}"
    ok_message = f"correct ip-address {address}"
    try:
        socket.inet_pton(socket.AF_INET, address)
    except AttributeError:  # no inet_pton here, sorry
        try:
            socket.inet_aton(address)
        except socket.error:
            print(error_message)
            return False
        return address.count('.') == 3
    except socket.error:  # not a valid address
        print(error_message)
        return False

    print(ok_message)
    return True
