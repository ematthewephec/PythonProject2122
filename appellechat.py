from main import *

def inputcommand(command):
    if command != "" and command.split()[0] == "/getIp":
        getip(command)
    elif command != "" and command.split()[0] == "/help":
        print(helpGeneral.help)
    elif command != "" and command.split()[0] == "/showOnlineUserTag":
        showOnlineUserTag(command,userlist)
    else:
        return "commande non existante , faites /help pour voir la liste des commandes "