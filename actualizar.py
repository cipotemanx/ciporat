import os
import sys
import time

#sys.stdout.write("\033[1;31m")
os.system("cls" if os.name == "nt" else "clear")
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
print(r"#############################################################")
print(r"#                                                           #")
print(r"#                 ╔╦═╦══╦╦═════╦╦╦═══════╗                  #")
print(r"#                 ║║║╠═╦╣╠╦╗╔╦═╣╠╬══╦═╦═╗║                  #")
print(r"#                 ║║╩║╠╬╗╔╣╚╝╠╝║║╠╝╔╬╝║╠╝║                  #")
print(r"#                 ║╚╩╩═╝╚═╩══╩═╩╩╩══╩═╩╝.║                  #")
print(r"#                 ╚══════════════════════╝                  #")
print(r"#                 Loading…                                  #")
print(r"#                 █▒▒▒▒▒▒▒▒▒                                #")
print(r"#                 10%                                       #")
print(r"#                 ███▒▒▒▒▒▒▒                                #")
print(r"#                 30%                                       #")
print(r"#                 █████▒▒▒▒▒                                #")
print(r"#                 50%                                       #")
print(r"#                 ███████▒▒▒                                #")
print(r"#                 70%                                       #")
print(r"#                 ██████████                                #")
print(r"#                 100%                                      #")
print(r"#                                         _  _              #")
print(r"#             _ .                        ( `   )_           #")
print(r"#   ███۞███████ ]▄▄▄▄▄▄▄▄▄▄▄▄▃         (    )    `)         #")
print(r"#  ▂▄▅█████████▅▄▃▂                   (_   (_ .  _) _)      #")
print(r"# [███████████████████].                                    #")
print(r"#  ◥⊙▲⊙▲⊙▲⊙▲⊙▲⊙▲⊙◤...                                       #")
print(r"#                                                           #")
print("#############################################################\n")

print("Bienvenido a el sistema de actualización de CipoRat.\n")
opcion= input("Quiere continuar con la actualización? (s/n): ")
if opcion == "s" or "S":
    os.system("" if os.name == "nt" else "rm ciporat.py")
    os.system("start https://github.com/cipotemanx/ciporat/archive/master.zip" if os.name == "nt" else "wget https://raw.githubusercontent.com/cipotemanx/ciporat/master/ciporat.py")
    print("\nAbriendo página de descarga.." if os.name == "nt" else "\nTerminando actualización")
    time.sleep(3)

else:
    os.system("python ciporat.py" if os.name == "nt" else "python3 ciporat.py")
