from main import *
import showUser


def inputcommand(command):
    if command != "" and command.split()[0] == "/getIp":
        return getip(command)
    elif command != "" and command.split()[0] == "/help":
        return helpGeneral.help
    elif command != "" and command.split()[0] == "/showOnlineUserTag":
        return showOnlineUserTag(command, userlist)
    # elif command != "" and command.split()[0] == "/version":
    #    print(versionAPP)
    elif command != "" and command.split()[0] == "/showUser":
        if command.split()[1] == "help":
            return helpShowUser.help
        else:
            return showUser.show_user(command.split()[1], command.split()[2])
    else:
        return "commande non existante , faites /help pour voir la liste des commandes"
