"""from whatsmyip.ip import get_ip
from whatsmyip.providers import GoogleDnsProvider


myip=get_ip(GoogleDnsProvider)

print(myip)
"""
import fire
from getpass import getpass
class Auth (object):
    def login(self, username = None):
        if username  == None:
            username = input ("Username: ")
        if username == None:
            print ("A username is required")
            return
        pw = getpass("Password: ")
        return username, pw

def login (username = None):
    if username == None:
        username = input ("Username: ")
    if username == None:
        print ("A username is required")
        return
    pw = getpass ("Password: ")
    return username, pw


"""
    while True:
        print("entrer votre commande")
        commande=input()
            if commande = "stop"
                break
            elif commande="ip"
                print(myip)
            else
                print("une erreur à été detecté")
"""


