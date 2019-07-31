import os
import sys

#sys.stdout.write("\033[1;31m")
while True:
    os.system("clear")
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

    print("Bienvenido a el sistema de actualización.\n")
    opcion= input("Quiere seguir con la actualización?: (s/n)")
    if opcion == "s":
        os.system("https://github.com/cipotemanx/ciporat/blob/master/cipote.py")
    else:
        os.system("python ciporat.py")
