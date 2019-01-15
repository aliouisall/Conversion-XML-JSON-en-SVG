#!/usr/bin/python2.7
# -*-coding:Utf-8 -*
import xml.etree.ElementTree as ET
from graphviz import Digraph

dot = Digraph(comment='Entity Relationship Diagram')

tree = ET.parse('Codification.xml')
root = tree.getroot()
for database in root.findall('database'):
    for table in database.findall('table'):
        name = table.get('name')
        tableContent = "{" + str(name)
        for index, column in enumerate(table.findall('column')):
            name = column.get('name')
            if (index == 0):
                tableContent = tableContent + " | " + str(name)
            elif (index == len(table)-1):
                tableContent = tableContent + " \\l " + str(name) + " \\l " + "}"
            else:
                tableContent = tableContent + " \\l " + str(name)
        dot.node(name, style="filled", fillcolor="#FCD975", shape='record', color='blue', label=tableContent)
    
# Choix du format
dot.format = 'svg'

# Génération du fichier svg avec un nom passé en argument
dot.render('Test', view=True)