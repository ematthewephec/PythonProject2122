from main import *


def inputcommand(command):
    if command != "" and command.split()[0] == "/getIp":
        return getip(command)
    elif command != "" and command.split()[0] == "/help":
        return helpGeneral.help
    elif command != "" and command.split()[0] == "/showOnlineUserTag":
        return showOnlineUserTag(command, userlist)
    # elif command != "" and command.split()[0] == "/version":
    #    print(versionAPP)
    else:
        return "commande non existante , faites /help pour voir la liste des commandes"
