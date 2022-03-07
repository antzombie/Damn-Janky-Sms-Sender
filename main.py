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
    number = input("Targets Number: ")
    message = input("Message to Target: ")
    requestt = str(f'curl -X POST http://{ip}:9090/text -d number={int(number)} -d "message={str(message)}"')
    os.system(str(f"{requestt}"))
    print("\n\n^ Yeah Just ignore that up there and hope it worked ^")
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nBye! have a nice time!")