#!/usr/bin/python2.7
# -*-coding:Utf-8 -*

# Importation des modules nécessaires
import json
import argparse
import requests
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
multiplicity = []
nameTable = []

# Définition de la fonction de validation du fichier xml
def xmlValidator(input):
	try:
		tree = parse(input)
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
            # print (nameTable)
            dot.node(nameTable[indexTable], style="filled", fillcolor="#FCD975", shape='record', color='blue', label=tableContent)
        
        for relationship in database.findall('relationship'):
            nameRelationship = relationship.get('name')
            dot.node(nameRelationship, style="filled", fillcolor="#FCD975", shape='circle', color='blue', label=nameRelationship)
            for index, multiplicity in enumerate(relationship.findall('multiplicity')):
                nameMultiplicity = multiplicity.get('name')
                multiplicityContent = multiplicity.text
                # print (nameMultiplicity)
                if (index == 0):
                    dot.edge(nameTable[index], nameRelationship, xlabel=multiplicityContent, constraint='false', color="blue", minlen="12", arrowhead="none")
                else:
                    dot.edge(nameRelationship, nameTable[index], xlabel=multiplicityContent, constraint='false', color="blue", minlen="12", arrowhead="none")

# Définition de la fonction de génération pour JSON
def gener():
    
    i = 0
    j = 0
    k1 = 0
    k2 = 0
    attribArrayLength = len(attributes)
    arrayEntitiesLength = len (arrayEntities)
    multiplicityLength = len(multiplicity)

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
        
        dot.node(relationArray[j], style="filled", fillcolor="#FCD975", shape='circle', color='blue', label=relationArray[j])
        for indexRelation, element in enumerate(dictRelation):
            if (indexRelation == 0):
                dot.edge(element, relationArray[j], splines="ortho", xlabel=str(multiplicity[indexRelation + k1 - 1]), constraint='false', color="blue", minlen="8", arrowhead="none")
                k1 += 2
            else:
                dot.edge(relationArray[j], element, splines="ortho", xlabel=str(multiplicity[indexRelation + k2 - 1]), constraint='false', color="blue", minlen="8", arrowhead="none")
                k2 += 2
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
                multiplicity.append(value)

        i = i + 1
    
    gener()

# Définition de la fonction de validation pour un fichier JSON
def jsonValidatorFile(content):
    try:
        parsedJson = json.load(content)
        jsonExtractor(parsedJson)
        return True
    except ValueError as error:
        print("JSON invalide : %s" %error)
        return False

# Définition de la fonction de validation pour un lien JSON
def jsonValidatorHttp():
    try:
        response = requests.get(args.http)
        json_data = response.json()
        jsonExtractor(json_data)
        return True
    except ValueError as error:
        print("JSON invalide : %s" %error)
        return False

def jsonTrace():

    print ("Les entités sont : ")
    for element in arrayEntities:
        print(str(element) + "")
    
    print ("\nLes relations sont : ")
    for element in relationArray:
        print(str(element))
    
    print ("\nLes attributs sont : ")
    for element in attributes:
        for attrib in element:
            print(str(attrib))

def traceXml(fichier):

    tree = parse(fichier)
    root = tree.getroot()
    for database in root.findall('database'):
        for table in database.findall('table'):
            name = table.get('name')
            print(name, 'est une classe pour ce fichier ')
            tableContent = "{" + str(name)
            print('La liste des attributs de la classe ', name, 'est :')
            for index, column in enumerate(table.findall('column')):
                name = column.get('name')
                print(name)

# Définition des différentes options et arguments
parser = argparse.ArgumentParser()

# Exclusion mutuelle entre l'option f et http
group = parser.add_mutually_exclusive_group(required=True)

group.add_argument("-f", "--file", dest="inputFile", help="permet de désigner un input de type fichier", metavar="FILE")
parser.add_argument("-i", "--input", choices=['xml','json'], help="permet de dire si l'input est en xml ou en json", required=True)
parser.add_argument("-o", "--output", dest="outputFile", help="permet de désigner le fichier de sortie", metavar="FILE", required=True)
parser.add_argument("-t", "--trace", action="store_true", help="permet de dire si on veut afficher les traces")
group.add_argument("--http", help="permet de désigner un input en flux http")

args = parser.parse_args()

# On vérifie si l'input est un fichier
if (args.inputFile):

    if (args.input == 'json'):
        content = open(args.inputFile) # Ouverture du fichier
        jsonValidatorFile(content) # Appel de la fonction de validation

        if (args.trace): # On vérifie si l'option -t est activée
            jsonTrace()
    elif(args.input == 'xml'):
        xmlValidator(args.inputFile)
        if (args.trace): # On vérifie si l'option -t est activée
            traceXml(args.inputFile)

# On vérifie si l'input est un flux http
elif(args.http):
    if (args.input == 'json'):
        jsonValidatorHttp()
    elif(args.input == 'xml'):
        response = requests.get(args.http)
        print (response)
        # tree = ElementTree.fromstring(response.content)
        
# Choix du format
dot.format = 'svg'

# Génération du fichier svg avec un nom passé en argument
dot.render(args.outputFile, view=True)
