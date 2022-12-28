import banner
from banner import *
import time
import os
import socket
def main():
    os.system('nodejs textbelt/server/app.js > /dev/null 2>&1 &')
    print(banner.usedbannerr)
    print("   ¯\_(=/)_/¯ Disclaimer: please dont use for any illegal activity")
    print("             ┻━┻ ~ \(°□°)/ ~ ┻━┻  Also @antzombie did this  ┻━┻ ~ \(°□°)/ ~ ┻━┻\n")
    print("Enter Your IP Adress")
    ip = input("IP: ")
    print("\n[01] America")
    print("[02] Canada")
    print("[03] Other")
    location = input("Target Location: ")
    if location == "01" or location == "1":
        location = str("text")
    if location == "02" or location == "2":
        location = str("canada")
    if location == "03" or location == "3":
        location = str("intl")
    number = input("Targets Number: ")
    message = input("Message to Target: ")
    requestt = str(f'curl -X POST http://{ip}:9090/{str(location)} -d number={int(number)} -d "message={str(message)}"')
    os.system(str(f"{requestt} > /dev/null 2>&1"))
    time.sleep(2)
    print('''
                                                             )
    )      (             )  (  (     (          (         ( /(
   (      ))\ (   (   ( /(  )\))(   ))\   (    ))\  (     )\())
   )\  ' /((_))\  )\  )(_))((_))\  /((_)  )\  /((_) )\ ) (_))/
 _((_)) (_)) ((_)((_)((_)_  (()(_)(_))   ((_)(_))  _(_/( | |_
| '  \()/ -_)(_-<(_-</ _` |/ _` | / -_)  (_-</ -_)| ' \))|  _|
|_|_|_| \___|/__//__/\__,_|\__, | \___|  /__/\___||_||_|  \__|
                           |___/
''')
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nBye! have a nice time!")
