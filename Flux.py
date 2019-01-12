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
	
	