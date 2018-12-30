#!/usr/bin/python3.5
# -*-coding:Utf-8 -*

def getOpt():

    from optparse import OptionParser

    parser = OptionParser()
    parser.add_option("-f", "--file", dest="filename",
                    help="permet de désigner un input de type fichier", metavar="FILE")
    parser.add_option("-i", "--input", help="permet de dire si l'input est en xml ou en json")
    parser.add_option("-o", "--output", dest="filename", help="permet de désigner le fichier de sortie", metavar="FILE")
    parser.add_option("-t", "--trace", help="permet de dire si on veut afficher les traces")
    parser.add_option("--http", help="permet de désigner un input en flux http")

    (options, args) = parser.parse_args()