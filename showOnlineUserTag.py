from main import *
from appellechat import *
import matplotlib.pyplot as plt
import numpy

userlist = [{'userid': 1, 'tag': ['1T', 'ActivUser', 'python']},
            {'userid': 2, 'tag': ['2T', 'ActivUser']}]  # exemple de liste de user recevable par la fonction
helpShowOnlineUserTag = HelpCommand(
    "cette commande ne prend pas d'argument et renvoie un grahique en batonnets du nombre de personne par tag ")


def showOnlineUserTag(cmd, ulist):
    if len(cmd.split()) == 1:  # en cas de /showOnlineUserTag
        listetag = []
        numberoftag = []
        for i in ulist:
            for ii in i["tag"]:
                if ii in listetag:
                    numberoftag[listetag.index(ii)] += 1  # trouve index du tag dans la liste at incrémente de 1
                else:
                    listetag.append(ii)
                    numberoftag.append(1)
        plt.bar(listetag, numberoftag, color='r')
        plt.xlabel('tags')
        plt.ylabel('nombre d\'utilisateurs')
        plt.suptitle('repartition des utilisateurs par tag')
        plt.show()
        return "your graph is open in another window"
    elif len(cmd.split()) > 1 and cmd.split()[1] == "help":  # en cas de /showOnlineUserTag help
        return helpShowOnlineUserTag.help
    else:
        return "une erreur à été detectée"
