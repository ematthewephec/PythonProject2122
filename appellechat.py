from main import *

def inputcommand():
    print("Entrer votre commande:")
    command = input()
    if command != "" and command.split()[0] == "/getIp":
        getip(command)
    elif command != "" and command.split()[0] == "/help":
        print(helpGeneral.help)
    elif command != "" and command.split()[0] == "/showOnlineUserTag":
        showOnlineUserTag(command,userlist)
    else:
        print("commande non existante , faites /help pour voir la liste des commandes ")