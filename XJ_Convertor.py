#!/usr/bin/python3.5
# -*-coding:Utf-8 -*

# Importation des modules nécessaires
import json
import argparse

# Définition de la fonction de validation
def jsonValidator(content):
    try:
        parsedJson = json.load(content)
        # jsonContent = json.dumps(parsedJson, sort_keys=True, indent = 4)
        numbItems = len(parsedJson)
        i = 2
        arrayEntities = []
        while (i < numbItems):
            arrayEntities.append(parsedJson[i]['name'])
            i = i + 1
        for item in arrayEntities:
            print(item)
        return True
    except Exception as error:
        print("Error : %s" %error)
        return False

# Définition des différentes options et arguments
parser = argparse.ArgumentParser()
parser.add_argument("-f", "--file", dest="filename", help="permet de désigner un input de type fichier", metavar="FILE")
parser.add_argument("-i", "--input", help="permet de dire si l'input est en xml ou en json")
parser.add_argument("-o", "--output", dest="filename", help="permet de désigner le fichier de sortie", metavar="FILE")
parser.add_argument("-t", "--trace", help="permet de dire si on veut afficher les traces")
parser.add_argument("--http", help="permet de désigner un input en flux http")

args = parser.parse_args()

# Récupération du fichier passé en argument
file = args.filename

# Ouverture du fichier
content = open(file)

# Appel de la fonction de validation
jsonValidator(content)
