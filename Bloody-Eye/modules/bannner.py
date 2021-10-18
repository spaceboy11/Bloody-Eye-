import os
import time
from colorama import Fore
def banner():
  os.system("clear")
  a = """
      _           _     
     | |         | |    
  ___| | __ _ ___| |__  
 / __| |/ _` / __| '_ \ 
 \__ \ | (_| \__ \ | | |
 |___/_|\__,_|___/_| |_|
                        """
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
  aa = (Fore.RED+a+b)
  print(aa)
 
def list():
    print("")
    time.sleep(0.07)
    print(Fore.RED+" ["+Fore.WHITE+"01"+Fore.RED+"]"+" Instagram")
    time.sleep(0.07)
    print(Fore.RED+" ["+Fore.WHITE+"02"+Fore.RED+"]"+" GitHub")
    time.sleep(0.07)
    print(Fore.RED+" ["+Fore.WHITE+"03"+Fore.RED+"]"+" Twitch")
    time.sleep(0.07)
    print(Fore.RED+" ["+Fore.WHITE+"04"+Fore.RED+"]"+" Spotify")
    time.sleep(0.07)
    print(Fore.RED+" ["+Fore.WHITE+"05"+Fore.RED+"]"+" Exit")
