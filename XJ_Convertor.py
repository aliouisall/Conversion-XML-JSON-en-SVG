#!/usr/bin/python2.7
# -*-coding:Utf-8 -*

# Importation des modules nécessaires
import json
import argparse
from graphviz import Digraph

dot = Digraph(comment='Entity Relationship Diagram')

# dot.edges(['AB', 'AL'])
# dot.edge('B', 'L', constraint='false')

# Déclaration du tableau des entités et de celui des attributs
arrayEntities = []
attributes = []
tableArray = []

# Définition de la fonction de génération
def gener():
    i = 0
    attribArrayLength = len(attributes)
    arrayEntitiesLength = len (arrayEntities)

    while (i < arrayEntitiesLength):
        tableContent = "{" + str(arrayEntities[i])
        dict = list(attributes)[i]
        for index, element in enumerate(dict):
            if (index == 0):
                tableContent = tableContent + " | " + str(element)
            elif (index == len(dict)-1):
                tableContent = tableContent + " \\n " + str(element) + "}"
            else:
                tableContent = tableContent + " \\n " + str(element)
        print(tableContent)
        dot.node(arrayEntities[i], style="filled", fillcolor="#FCD975", shape='record', color='blue', label=tableContent)
        i += 1
    dot.edge('Chambre', 'Etudiant', constraint='false', color="blue", minlen="17", arrowhead="none")
    

# Définition de la fonction d'extraction
def jsonExtractor(parsedContent):
    numbItems = len(parsedContent)
    i = 2
    while (i < numbItems):
        arrayEntities.append(parsedContent[i]['name'])
        attributes.append(parsedContent[i]['data'][0].keys())
        i = i + 1
    gener()

# Définition de la fonction de validation
def jsonValidator(content):
    try:
        parsedJson = json.load(content)
        jsonExtractor(parsedJson)
        return True
    except ValueError as error:
        print("Error : %s" %error)
        return False

# Définition des différentes options et arguments
parser = argparse.ArgumentParser()
parser.add_argument("-f", "--file", dest="inputFile", help="permet de désigner un input de type fichier", metavar="FILE")
parser.add_argument("-i", "--input", help="permet de dire si l'input est en xml ou en json")
parser.add_argument("-o", "--output", dest="outputFile", help="permet de désigner le fichier de sortie", metavar="FILE")
parser.add_argument("-t", "--trace", help="permet de dire si on veut afficher les traces")
parser.add_argument("--http", help="permet de désigner un input en flux http")

args = parser.parse_args()

# Ouverture du fichier
content = open(args.inputFile)

# Appel de la fonction de validation
jsonValidator(content)
dot.format = 'svg'
dot.render(args.outputFile, view=True)
