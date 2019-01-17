import urllib.request, sys, xml.dom.minidom
from bs4 import BeautifulSoup
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import parse
import requests
import svgwrite
#from XJ_Convertor import extractGener

#Définition de la fonction qui accéde au fichier par flux pour recupérer son contenu
def flux():
	adress = requests.get('http://sgbdproject.000webhostapp.com/files/kyQtZ.html')
	fichier = open("flux.xml", "w")
	fichier.write(adress.text)
	fichier.close()
	tree = ET.parse('Codification.xml')
	root = tree.getroot()
	for database in root.findall('database'):
		for table in database.findall('table'):
			name = table.get('name')
			print(name)
			tableContent = "{" + str(name)
			for index, column in enumerate(table.findall('column')):
				name = column.get('name')
				print(name)
