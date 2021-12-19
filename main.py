from whatsmyip.ip import get_ip
from whatsmyip.providers import GoogleDnsProvider


class HelpCommand:  #placé avant les import des fichiers pour eviter des bugs
    def __init__(self, description):
        self.help = description




def getip(cmd):
    if len(cmd.split()) == 1:
        myip = get_ip(GoogleDnsProvider)
        print("votre adresse ip est: " + myip)
    elif len(cmd.split()) > 1 and cmd.split()[1] == "help":
        print(helpGetIp.help)
    else:
        print("une erreur à été detectée")


class HelpCommand:
    def __init__(self, description):
        self.help = description

from appellechat import *
from showOnlineUserTag import *

helpGetIp = HelpCommand("cette commande ne prend pas d'argument et renvoie votre adresse ip public")
commandList = ["/getIp", "/help","/showOnlineUserTag"]  # liste des commandes ( à completer lors de l'ajout d'une commande)
commandString = "voici la liste des commandes : " + ", ".join(commandList)
helpGeneral = HelpCommand(commandString + ".Ajoutez \" help\" à la suite de celles-ci pour plus d'informations.")

if __name__ == "__main__":
    inputcommand()



