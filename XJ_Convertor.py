#!/usr/bin/python3.5
# -*-coding:Utf-8 -*

def gestiontOpt():

    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--file", dest="filename",
                    help="permet de désigner un input de type fichier", metavar="FILE")
    parser.add_argument("-i", "--input", help="permet de dire si l'input est en xml ou en json")
    parser.add_argument("-o", "--output", dest="filename", help="permet de désigner le fichier de sortie", metavar="FILE")
    parser.add_argument("-t", "--trace", help="permet de dire si on veut afficher les traces")
    parser.add_argument("--http", help="permet de désigner un input en flux http")

    args = parser.parse_args()
    file = args.filename
    content = open(file)
    print(content.read())

gestiontOpt()