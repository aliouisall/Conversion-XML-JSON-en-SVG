# -*-coding:Latin-1 -*

# On importe le module os qui dispose de variables 
# et de fonctions utiles pour dialoguer avec votre 
# système d'exploitation

import os.path

# Importation des packages et modules nécessaire 

import xml.etree.ElementTree as ET
from xml.etree.ElementTree import ParseError

# Définition de la fonction vérifiant léxtenxion du fichier choisi

def extensionValidator(fichier):
	extension = os.path.splitext(fichier)[1][1:]
	if extension != 'xml' :
		print("Veuillez choisir un fichier xml svp")
	else:
		return xmlValidator(fichier)
		
# Définition de la fonction de validation d'fichier 

def xmlValidator(fic):
	try:
		tree = ET.parse(fic)
		return True
	except ParseError as error:
		print("Fichier xml invalid")
		return False 
