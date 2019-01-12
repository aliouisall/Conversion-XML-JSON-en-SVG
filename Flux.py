import urllib.request, sys, xml.dom.minidom
from bs4 import BeautifulSoup
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import parse
import requests
import svgwrite
#from Validation_Xml import ExtractElt
def flux(url):
	adress = requests.get(url)
	fichier = open("flux.xml", "w")
	fichier.write(adress.text)
	fichier.close()
	
	tree = ET.parse("flux.xml")
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
		cardi21 = entite2.find('cardinalite').text

	for entite3 in root.findall('entite3'):
		nomEntite3 = entite3.find('nomEntite').text
	for attribut in entite3.findall('attribut'):
		id3 = attribut.find('id').text
		intitule = attribut.find('intitule').text
		cardi3 = entite3.find('cardinalite').text

	for association in root.findall('association'):
		nomAssociation = association.find('nomAssos').text
	for attribut in association.findall('attribut'):
		NbrEtu = attribut.find('date').text

#Creation du fichier svg
	dwg = svgwrite.Drawing('flux.svg')

#Creation de la première entité 
	dwg.add(dwg.rect((10, 10), (200, 100), stroke=svgwrite.rgb(0,0, 0, '%'), fill='blue'))
	dwg.add(dwg.text(id1, insert=(30,60), stroke='none', fill=svgwrite.rgb(15, 15, 15, '%'), font_size='15px', font_weight="bold"))
	dwg.add(dwg.text(nom, insert=(30,80), stroke='none', fill=svgwrite.rgb(15, 15, 15, '%'), font_size='15px', font_weight="bold"))
	dwg.add(dwg.text(prenom, insert=(30,100), stroke='none', fill=svgwrite.rgb(15, 15, 15, '%'), font_size='15px', font_weight="bold"))
	dwg.add(dwg.text(cardi1, insert=(65,125), stroke='none', fill=svgwrite.rgb(15, 15, 15, '%'), font_size='15px', font_weight="bold"))
	dwg.add(dwg.line((210, 40), (8, 40),  stroke=svgwrite.rgb(0,0,0, '%')))
	dwg.add(dwg.text(nomEntite, insert=(65,25), stroke='none', fill='black', font_size='15px', font_weight="bold", font_family="Arial"))

#Creation de la seconde entité
	dwg.add(dwg.rect((10, 400), (200, 100), stroke=svgwrite.rgb(0, 0, 0, '%'), fill='blue'))
	dwg.add(dwg.text(nomEntite2, insert=(70, 420), fill='black', font_size='15px', font_weight="bold", font_family="Arial"))
	dwg.add(dwg.text(id2, insert=(30,450), stroke='none', fill=svgwrite.rgb(15, 15, 15, '%'), font_size='15px', font_weight="bold"))
	dwg.add(dwg.text(cardi21, insert=(215,445), stroke='none', fill=svgwrite.rgb(15, 15, 15, '%'), font_size='15px', font_weight="bold"))
	dwg.add(dwg.text(intitule, insert=(30,470), stroke='none', fill=svgwrite.rgb(15, 15, 15, '%'), font_size='15px', font_weight="bold"))
	dwg.add(dwg.text(cardi2, insert=(65,395), stroke='none', fill=svgwrite.rgb(15, 15, 15, '%'), font_size='15px', font_weight="bold"))
	dwg.add(dwg.line((100, 110), (100, 400),  stroke=svgwrite.rgb(0,0,0, '%')))

#Creation de la troisième entité
	dwg.add(dwg.rect((500, 400), (200, 100), stroke=svgwrite.rgb(0, 0, 0, '%'), fill='blue'))
	dwg.add(dwg.text(nomEntite3, insert=(550, 420), fill='black', font_size='15px', font_weight="bold", font_family="Arial"))
	dwg.add(dwg.text(id3, insert=(520, 450), stroke='none', fill=svgwrite.rgb(15, 15, 15, '%'), font_size='15px', font_weight="bold"))
	dwg.add(dwg.text(intitule, insert=(520,470), stroke='none', fill=svgwrite.rgb(15, 15, 15, '%'), font_size='15px', font_weight="bold"))
	dwg.add(dwg.text(cardi3, insert=(470,445), stroke='none', fill=svgwrite.rgb(15, 15, 15, '%'), font_size='15px', font_weight="bold"))
	dwg.add(dwg.line((500, 430), (700, 430),  stroke=svgwrite.rgb(0,0,0, '%')))
	dwg.add(dwg.line((210, 450), (500, 450),  stroke=svgwrite.rgb(0,0,0, '%')))


#Creation de l'association
	dwg.add(dwg.line((210, 430), (8, 430),  stroke=svgwrite.rgb(0,0,0, '%')))
	dwg.add(dwg.circle(center=(100,250), r=60,  stroke=svgwrite.rgb(15, 15, 15, '%'), fill='white'))
	dwg.add(dwg.line((158, 230), (42, 230),  stroke=svgwrite.rgb(0,0,0, '%')))
	dwg.add(dwg.text(nomAssociation, insert=(80, 220), fill='black', font_size='15px', font_weight="bold", font_family="Arial"))
	dwg.add(dwg.text(NbrEtu, insert=(50, 250), fill='black', font_size='15px', font_weight="bold", font_family="Arial"))

# Affichage de notre image svg
	print(dwg.tostring())

# Sauvegarde du fichier svg dans le disque
	dwg.save()