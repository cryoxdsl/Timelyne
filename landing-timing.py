#!/usr/bin/python
# -*- coding: utf-8 -*-
#############################

# Par Paul Besson
# Description : Timing url
# Dependances :
# Utilisation : python landing-timing.py path/to/list.txt path/to/result.txt

#############################


#############################
# Libraries
#############################

import sys
import urllib.response
import urllib.request
from urllib.error import HTTPError, URLError
import socket
from socket import timeout
import requests
from time import time

##################
# Fonctions
##################

##################
# Fontion > Get arguments


def checkFile():
    nbArgument = len(sys.argv)
    if nbArgument != 3:
        print("Usage : python landing-timing.py path/to/list.txt path/to/result.txt")
        exit()
    else:
        # Init des parametres
        global fileList, fileOut
        fileList = sys.argv[1]
        fileOut = sys.argv[2]

##################
# Fontion > Get list URLs


def getList():
    # Liste des urls
    global listUrl
    listUrl = [line.rstrip() for line in open(fileList)]

##################
# Fontion > Test list URLs


def testList():
    # Tests des urls
    formatting = "url; request-time\n"
    fileWr.write(formatting)
    for urlCheck in listUrl:
        # Créer une erreur si dans le fichier de liste il y a une ligne vide, urllib bloque
        try:
            start = time()
            urllib.request.urlopen(urlCheck, timeout=60)
            endtime = time()
            delay = endtime - start
            result = "%s; %fs \n" % (urlCheck, delay)
           # On met en forme le resultat
            print(result)
            # On ecrit le resultat dans le fichier
            fileWr.write(result)
        except timeout:
            result = ("%s; Timeout \n" % (urlCheck))
            print(result)
            # On ecrit le resultat dans le fichier
            fileWr.write(result)
        except (HTTPError):
            # On met en forme le resultat
            result = ("%s; HTTPError \n" % (urlCheck))
            print(result)
            # On ecrit le resultat dans le fichier
            fileWr.write(result)
        except (URLError):
            # On met en forme le resultat
            result = ("%s; URLError \n" % (urlCheck))
            print(result)
            # On ecrit le resultat dans le fichier
            fileWr.write(result)


##################
# Main
##################
# On vérifie les parametres
checkFile()

# Lecture des URLs
getList()

# On ouvre le fichier de resultats
fileWr = open(fileOut, "w")

# On traite les Urls
testList()

# On ferme le fichier
fileWr.close()
