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
relationArray = []
relationContent = []

# Définition de la fonction de génération
def gener():
    
    i = 0
    j = 0
    attribArrayLength = len(attributes)
    arrayEntitiesLength = len (arrayEntities)

    while (i < arrayEntitiesLength):
        tableContent = "{" + str(arrayEntities[i])
        dictAttributes = list(attributes)[i]
        for indexAttributes, element in enumerate(dictAttributes):
            if (indexAttributes == 0):
                tableContent = tableContent + " | " + str(element)
            elif (indexAttributes == len(dictAttributes)-1):
                tableContent = tableContent + " \\l " + str(element) + " \\l " + "}"
            else:
                tableContent = tableContent + " \\l " + str(element)
        
        dot.node(arrayEntities[i], style="filled", fillcolor="#FCD975", shape='record', color='blue', label=tableContent)
        i += 1
    # print(dot.source)        
    
    dictRelation = list(relationContent)[j]  
    
    while (j < len(relationArray)):
        
        dot.node(relationArray[j], style="filled", fillcolor="#FCD975", shape='circle', color='blue', label=relationArray[0])
    
        for indexRelation, element in enumerate(dictRelation):
            print('Index : ' + str(indexRelation) + '\n Element : ' + str(element))
            if (indexRelation == 0):
                dot.edge(element, relationArray[0], xlabel="(0:1)", constraint='false', color="blue", minlen="12", arrowhead="none")
            else:
                dot.edge(relationArray[0], element, xlabel="(1:n)", constraint='false', color="blue", minlen="12", arrowhead="none")                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     
        j += 1

# Définition de la fonction d'extraction
def jsonExtractor(parsedContent):
    
    numbItems = len(parsedContent)
    j = 0
    i = 2
    while (i < numbItems):

        if (str(parsedContent[i]['type']) == 'table'):
            # Ajout d'éléments dans le tableu Entités
            arrayEntities.append(parsedContent[i]['name'])
            # Ajout d'élément dans le tableau Attributs
            attributes.append(parsedContent[i]['data'][0].keys())
        
        if (str(parsedContent[i]['type']) == 'relationship'):
            relationArray.append(parsedContent[i]['name'])
            relationContent.append(parsedContent[i]['data'][0].keys())

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

# Choix du format
dot.format = 'svg'

# Génération du fichier svg avec un nom passé en argument
dot.render(args.outputFile, view=True)
