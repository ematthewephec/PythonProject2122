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


class HelpCommande:
    def __init__(self, description):
        self.help = description


helpGetIp = HelpCommande("cette commande ne prend pas d'argument et renvoie votre adresse ip public")
commandList = ["/getIp", "/help"]
commandString = "voici la liste des commandes : " + ", ".join(commandList)
helpGeneral = HelpCommande(commandString + ".Ajoutez \" help\" à la suite de celles-ci pour plus d'informations.")


def inputcommand():
    print("Entrer votre commande:")
    command = input()
    if command != "" and command.split()[0] == "/getIp":
        getip(command)
    elif command != "" and command.split()[0] == "/help":
        print(helpGeneral.help)
    else:
        print("une erreur à été detecté")


inputcommand()
