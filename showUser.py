import mongoDbConnection as mongo


def show_user(lastname, firstname):
    """
        :param lastname:
        :param firstname:
        :return:
        """

    user = mongo.find_data({"lastname": lastname, "firstname": firstname})
    return ("L'utilisateur s'appelle {} {}, il posséde ces tag : {}".format(user["firstname"], user["lastname"],
                                                                            user["tag"]))
