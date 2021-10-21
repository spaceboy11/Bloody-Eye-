import os
import time
from colorama import Fore
def banner():
  os.system("clear")
  b = """        
        _     _     _               
       | |   (_)   | |              
  _ __ | |__  _ ___| |__   ___ _ __ 
 | '_ \| '_ \| / __| '_ \ / _ \ '__|
 | |_) | | | | \__ \ | | |  __/ |   
 | .__/|_| |_|_|___/_| |_|\___|_|   
 | |                                
 |_|
 """
  aa = (Fore.RED+b)
  print(aa)
 
def list():
    print("")
    time.sleep(0.07)
    print(Fore.RED+" ["+Fore.WHITE+"01"+Fore.RED+"]"+Fore.YELLOW+" Instagram")
    time.sleep(0.07)
    print(Fore.RED+" ["+Fore.WHITE+"02"+Fore.RED+"]"+Fore.YELLOW+" GitHub")
    time.sleep(0.07)
    print(Fore.RED+" ["+Fore.WHITE+"03"+Fore.RED+"]"+Fore.YELLOW+" Twitch")
    time.sleep(0.07)
    print(Fore.RED+" ["+Fore.WHITE+"04"+Fore.RED+"]"+Fore.YELLOW" Spotify")
    time.sleep(0.07)
    print(Fore.RED+" ["+Fore.WHITE+"05"+Fore.RED+"]"+Fore.YELLOW" Exit")
