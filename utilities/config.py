import configparser


def getConfig():
    config = configparser.ConfigParser()
    config.read("C:\\Users\\swapnil.bedse\\PycharmProjects\\TestVerve\\utilities\\base.ini")
    return config
