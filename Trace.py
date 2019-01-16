# -*-coding:Latin-1 -*
import xml.etree.ElementTree as ET
from graphviz import Digraph
def trace(fichier):
    dot = Digraph(comment='Entity Relationship Diagram')

    tree = ET.parse(fichier)
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
                if (index == 0):
                    tableContent = tableContent + " | " + str(name)
                elif (index == len(table)-1):
                    tableContent = tableContent + " \\l " + str(name) + " \\l " + "}"
                else:
                    tableContent = tableContent + " \\l " + str(name)