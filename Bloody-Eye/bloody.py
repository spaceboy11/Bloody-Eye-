import sys
import time
from colorama import Fore, init
from modules import localhost
from modules import bannner
import os
try:
    bannner.banner()
    print(Fore.RED+" Select Any Attack for your Victim")
    bannner.list()

    print("")
    a = input(Fore.RED+" ["+Fore.WHITE+"~"+Fore.RED+"]"+Fore.CYAN+" Select an option : ")
    if a == "01":
        def b():
            localhost.instagram()
        b()
    elif a == "02":
        def c():
            localhost.github()
        c()
    elif a == "03":
        def d():
            localhost.twitch()
        d()
        
    elif a == "04":
        def e():
            localhost.spotify()
        e()
    elif a == "05":
        os.system("cls")
        os.system("exit")
except:
    os.system("cls")
    sys.exit()


