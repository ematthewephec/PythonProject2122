from whatsmyip.ip import get_ip
from whatsmyip.providers import GoogleDnsProvider


def getip(cmd):
    if len(cmd.split()) == 1:
        myip = get_ip(GoogleDnsProvider)
        print("votre adresse ip est: " + myip)
    elif len(cmd.split()) > 1 and cmd.split()[1] == "help":
        print(helpGetIp.help)
    else:
        print("une erreur à été detecté")


class HelpFunction:
    def __init__(self, description):
        self.help = description


helpGetIp = HelpFunction("cette fonction ne prend pas d'argument et renvoie votre adresse ip public")
functionsList = ["/getIp", "/help"]
functionsString = "voici la liste des fonctions : " + ", ".join(functionsList)
helpGeneral = HelpFunction(functionsString + ".Ajoutez \" help\" à la suite de celles-ci pour plus d'informations.")


def inputcommande():
    print("Entrer votre commande:")
    commande = input()
    if commande != "" and commande.split()[0] == "/getIp":
        getip(commande)
    elif commande != "" and commande.split()[0] == "/help":
        print(helpGeneral.help)
    else:
        print("une erreur à été detecté")


inputcommande()
