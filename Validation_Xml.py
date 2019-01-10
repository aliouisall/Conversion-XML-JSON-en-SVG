# -*-coding:Latin-1 -*

# On importe le module os qui dispose de variables 
# et de fonctions utiles pour dialoguer avec votre 
# système d'exploitation

import os.path

# Importation des packages et modules nécessaire 

import xml.etree.ElementTree as ET
from xml.etree.ElementTree import ParseError
from xml.etree.ElementTree import parse
import svgwrite

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
#Extraction des éléments 
def ExtractElt(fich):
    tree = ET.parse(fich)
    root = tree.getroot()

    for entite1 in root.findall('entite1'):
        nomEntite = entite1.find('nomEntite').text
    for attribut in entite1.findall('attribut'):
        id1 = attribut.find('id').text
        nom = attribut.find('nom').text
        prenom = attribut.find('prenom').text
        cardi1 = entite1.find('cardinalite').text

    for entite2 in root.findall('entite2'):
        nomEntite2 = entite2.find('nomEntite').text

    for attribut in entite2.findall('attribut'):
        id2 = attribut.find('id').text
        intitule = attribut.find('intitule').text
        cardi2 = entite2.find('cardinalite').text

    for association in root.findall('association'):
        nomAssociation = association.find('nomAssos').text
    for attribut in association.findall('attribut'):
        NbrEtu = attribut.find('date').text
  		
