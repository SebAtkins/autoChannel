import os

def createList(account):
    return ["file " + account + "/" + file for file in os.listdir(account)]
