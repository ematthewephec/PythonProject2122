from whatsmyip.ip import get_ip
from whatsmyip.providers import GoogleDnsProvider


class HelpCommand:  # à placer avant les import des fichiers pour eviter des bugs
    def __init__(self, description):
        self.help = description


def getip(cmd):
    if len(cmd.split()) == 1:
        myip = get_ip(GoogleDnsProvider)
        return "votre adresse ip est: " + myip
    elif len(cmd.split()) > 1 and cmd.split()[1] == "help":
        return helpGetIp.help
    else:
        return "une erreur à été detectée"


from appellechat import *
from showOnlineUserTag import *

helpGetIp = HelpCommand("cette commande ne prend pas d'argument et renvoie votre adresse ip public")
# liste des commandes ( à completer lors de l'ajout d'une commande)
commandList = ["/getIp", "/help", "/showOnlineUserTag"]
commandString = "voici la liste des commandes : " + ", ".join(commandList)
helpGeneral = HelpCommand(commandString + ".Ajoutez \" help\" à la suite de celles-ci pour plus d'informations.")
