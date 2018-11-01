import socket
import sys
from time import sleep



class sock:

    def __init__(self, ip, time=0):
        self.ip = ip
        self.time = time

    def run(self):
        i = 0
        control_variable = 0

        try:
            init = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            init.settimeout(5)
            init.connect((self.ip, 53))
            # init.timeout(3)
            init.shutdown(2)
            return True



        except socket.error as e:
            print("Cannot connect to ", self.ip)
            print("Something went wrong inside of Socket_teste module:", sys.exc_info()[0], sys.exc_info()[1])
            return False

