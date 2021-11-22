from whatsmyip.ip import get_ip
from whatsmyip.providers import GoogleDnsProvider

myip = get_ip(GoogleDnsProvider)

print(myip)

while True:
    print("Entrer votre commande")
    commande = input()
    if commande == "stop":
        print("Arret du programme")
        break
    elif commande == "ip":
        print("votre adresse ip est: " + myip)
    else:
        print("une erreur à été detecté")

