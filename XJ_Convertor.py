#!/usr/bin/python2.7
# -*-coding:Utf-8 -*

# Importation des modules nécessaires
import json
import argparse
import os.path
import requests
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import ParseError
from xml.etree.ElementTree import parse
from graphviz import Digraph

dot = Digraph(comment='Entity Relationship Diagram')

# Déclaration de la liste des entités, attributs, associations et multiplicités
arrayEntities = []
attributes = []
tableArray = []
relationArray = []
relationContent = []
multiplicty = []
nameTable = []

# Définition de la fonction de validation du fichier xml
def xmlValidator(input):
	try:
		tree = ET.parse(input)
		extractGener(tree)
		return True
	except ParseError as error:
		print("Fichier xml invalide")
		return False 

# Définition de la fonction de génération pour XML
def extractGener(input):
    root = input.getroot()
    for database in root.findall('database'):
        for indexTable, table in enumerate(database.findall('table')):
            name = table.get('name')
            nameTable.append(name)
            tableContent = "{" + str(name)
            for index, column in enumerate(table.findall('column')):
                name = column.get('name')
                if (index == 0):
                    tableContent = tableContent + " | " + str(name)
                elif (index == len(table)-1):
                    tableContent = tableContent + " \\l " + str(name) + " \\l " + "}"
                else:
                    tableContent = tableContent + " \\l " + str(name)
            print nameTable
            dot.node(nameTable[indexTable], style="filled", fillcolor="#FCD975", shape='record', color='blue', label=tableContent)
        
        for relationship in database.findall('relationship'):
            nameRelationship = relationship.get('name')
            dot.node(nameRelationship, style="filled", fillcolor="#FCD975", shape='circle', color='blue', label=nameRelationship)
            for index, multiplicity in enumerate(relationship.findall('multiplicity')):
                nameMultiplicity = multiplicity.get('name')
                multiplicityContent = multiplicity.text
                print nameMultiplicity
                if (index == 0):
                    dot.edge(nameTable[index], nameRelationship, label=multiplicityContent, constraint='false', color="blue", minlen="12", arrowhead="none")
                else:
                    dot.edge(nameRelationship, nameTable[index], label=multiplicityContent, constraint='false', color="blue", minlen="12", arrowhead="none")

# Définition de la fonction de génération pour JSON
def gener():
    
    i = 0
    j = 0
    attribArrayLength = len(attributes)
    arrayEntitiesLength = len (arrayEntities)

    # Voci ce que nous devons avoir à la sortie de la boucle {NomEntité | Attribut1 - Atribut2 ...}
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
    
    while (j < len(relationArray)):
    
        dictRelation = list(relationContent)[j]
        
        dot.node(relationArray[j], style="filled", fillcolor="#FCD975", shape='circle', color='blue', label=relationArray[0])

        for indexRelation, element in enumerate(dictRelation):
            print('Index : ' + str(indexRelation) + '\n Element : ' + str(element))
            if (indexRelation == 0):
                dot.edge(element, relationArray[0], xlabel=str(multiplicty[indexRelation]), constraint='false', color="blue", minlen="12", arrowhead="none")
            else:
                dot.edge(relationArray[0], element, xlabel=str(multiplicty[indexRelation]), constraint='false', color="blue", minlen="12", arrowhead="none")
        j += 1

# Définition de la fonction d'extraction pour JSON
def jsonExtractor(parsedContent):
    
    numbItems = len(parsedContent)
    j = 0
    i = 2

    while (i < numbItems):

        if (str(parsedContent[i]['type']) == 'table'):
            arrayEntities.append(parsedContent[i]['name']) # Ajout d'éléments dans la liste des Entités
            attributes.append(parsedContent[i]['data'][0].keys()) # Ajout d'élément dans la liste des Attributs
        
        if (str(parsedContent[i]['type']) == 'relationship'):
            relationArray.append(parsedContent[i]['name']) # Ajout d'éléments dans le tableu Relation
            relationContent.append(parsedContent[i]['data'][0].keys()) # Ajout d'éléments dans la liste du contenu des relations

            for key, value in parsedContent[i]['data'][0].items():
                multiplicty.append(value)

        i = i + 1
    
    gener()

# Définition de la fonction de validation pour un fichier JSON
def jsonValidatorFile(content):
    try:
        parsedJson = json.load(content)
        jsonExtractor(parsedJson)
        return True
    except ValueError as error:
        print("Invalid JSON : %s" %error)
        return False

# Définition de la fonction de validation pour un lien JSON
def jsonValidatorHttp():
    try:
        response = requests.get(args.http)
        json_data = response.json()
        jsonExtractor(json_data)
        return True
    except ValueError as error:
        print("Invalid JSON : %s" %error)
        return False

# Définition des différentes options et arguments
parser = argparse.ArgumentParser()

# Exclusion mutuelle de deux options
group = parser.add_mutually_exclusive_group(required=True)

group.add_argument("-f", "--file", dest="inputFile", help="permet de désigner un input de type fichier", metavar="FILE")
parser.add_argument("-i", "--input", choices=['xml','json'], help="permet de dire si l'input est en xml ou en json", required=True)
parser.add_argument("-o", "--output", dest="outputFile", help="permet de désigner le fichier de sortie", metavar="FILE", required=True)
parser.add_argument("-t", "--trace", help="permet de dire si on veut afficher les traces")
group.add_argument("--http", help="permet de désigner un input en flux http")

args = parser.parse_args()

# Type de l'input passé en argument
if (args.input == 'xml'):
    print('Il s\'agit d\'un fichier xml')
elif(args.input == 'json'):
    print('Il s\'agit d\'un fichier json')

if (args.inputFile):
    
    if (args.input == 'json'):
        content = open(args.inputFile) # Ouverture du fichier
        jsonValidatorFile(content) # Appel de la fonction de validation
    elif(args.input == 'xml'):
        xmlValidator(args.inputFile)

elif(args.http):
    if (args.input == 'json'):
        jsonValidatorHttp()
    elif(args.input == 'xml'):
        response = requests.get(args.http)
        tree = ET.fromstring(response.content)
        print("Salut")
# Choix du format
dot.format = 'svg'

# Génération du fichier svg avec un nom passé en argument
dot.render(args.outputFile, view=True)
