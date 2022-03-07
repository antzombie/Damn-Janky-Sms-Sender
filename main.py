import banner
from banner import *
import time
import os
import socket
host = socket.gethostname()
ip = socket.gethostbyname(host)
def main():
    print(banner.usedbannerr)
    print("   ¯\_(=/)_/¯ I Would put a disclaimer but there is no malicious part in texting right?")
    print("             ┻━┻ ~ \(°□°)/ ~ ┻━┻  Also @ase3p did this  ┻━┻ ~ \(°□°)/ ~ ┻━┻\n")
    print("[01] America")
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
    time.sleep(0.5)
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
