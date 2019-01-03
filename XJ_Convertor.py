#!/usr/bin/python2.7
# -*-coding:Utf-8 -*

# Importation des modules nécessaires
import json
import argparse
from graphviz import Digraph

dot = Digraph(comment='Entity Relationship Diagram')
# dot.attr('node')
# dot.node('A',  shape='record', label="{Aliou | Sall}")
# dot.node('B', 'Sir Bedevere the Wise')
# dot.node('L', 'Sir Lancelot the Brave')
# print(dot.source)
# dot.render('test-output/round-table.gv', view=True)

# dot.edges(['AB', 'AL'])
# dot.edge('B', 'L', constraint='false')

# Définition de la fonction de validation
def jsonValidator(content):
    try:
        parsedJson = json.load(content)
        # jsonContent = json.dumps(parsedJson, sort_keys=True, indent = 4)
        numbItems = len(parsedJson)
        i = 2
        arrayEntities = []
        attributes = []
        while (i < numbItems):
            arrayEntities.append(parsedJson[i]['name'])
            attributes.append(parsedJson[i]['data'][0].keys())
            # print(i)
            i = i + 1
        # for item in arrayEntities:
        #     print(item)
        j = 0
        k = 0
        # l = 0
        attribArrayLength = len(attributes)
        while (k < len(arrayEntities)):
            dot.node(arrayEntities[k],  shape='record', color='blue', label=arrayEntities[k])
            while (j < attribArrayLength):
                dict = list(attributes)[j]
                for element in dict:
                    dot.node(element,  shape='record', color='blue', label=element)
                j += 1
            k += 1
        return True
    except ValueError as error:
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
dot.format = 'svg'
dot.render('test-output/round-table.gv', view=True)
