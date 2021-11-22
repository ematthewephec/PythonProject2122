from whatsmyip.ip import get_ip
from whatsmyip.providers import GoogleDnsProvider


myip=get_ip(GoogleDnsProvider)

print(myip)


    while True:
        print("entrer votre commande")
        commande=input()
            if commande = "stop":
                break
            elif commande= "ip" :
                print(myip)
            else :
                print("une erreur à été detecté")



