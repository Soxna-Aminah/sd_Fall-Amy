
from csv import*
from json import*
import json
import re
from yaml import*
from xml import*
import xml.etree.ElementTree as et
import xmltodict
from pprint import pprint

#Fonction pour déterminer l'extension du fichier
def determineExtension():
    fic=input("Veuillez saisir le chemine du fichier: ")
    nfic=fic
    fic=fic.split(".")
    if len(fic)==2:
        extens=fic[1]
        li=[nfic,extens]
        return li
    else: return False
#Fonction pour importer et lire le fichier
def lectureFichier(extens,fic):
    myfile=[]
    if extens=='csv':
        file=open(fic,'r',encoding="utf8")
        csv_reader=DictReader(file)
        for row in csv_reader:
            myfile.append(row)
    elif extens=="json":
         with open(fic) as json_data:
            data_dict = load(json_data)
            myfile.append(data_dict)
    elif extens=="yaml" or extens=="yml":
        with open(fic,'r') as f:
             nf=load(f)
             myfile.append(nf)
    elif extens=="xml":
        with open(fic,"r") as xml_data:
            nfile=xmltodict.parse(xml_data.read(),dict_constructor=dict)
            myfile.append(nfile)
    else: return False
    return myfile
#Fonction pour vérifier la validité
def verifValidite(extens):
    extens=extens.lower()
    listextens=['csv','json','yaml','yml','xml']
    if extens in listextens:
        return True
    else:
        return False
#Transformer un dic en csv
def dictocsv(myfile):
    with open("mynewfile.csv","w") as csv_out:
        csv_writer=writer(csv_out)
        csv_writer.writerows(myfile)

#Transformer un dic en json
def dictojson(myfile):
    with open("mynewfile.json","w") as json_out:
        json_out.write(dumps(myfile))
#Transformer un dic en yaml
def dictoymal(myfile):
    with open("mynewfile.yaml","w") as yaml_out:
        yaml_out.write(dump(myfile))
#Transformer un dic en xml
def dictoxml(myfile):
    myfile=dict(myfile)
    with open("mynewfile.xml","w") as xml_out:
        xmltodict.unparse(myfile)

#Fonction pour transformer le fichier csv aux autres formats au choix
def transformcsv(myfile):
    rep=True
    while rep:
            print(""" 
                    1.Format json
                    2.Format yaml
                    3.Format xml
                    4.Quitter
            """)
            rep=input("Faites votre choix: ")
            if rep=="1":
                print("Transformation format json")
                dictojson(myfile)
            elif rep=="2":
                print("Transformation format yaml")
                dictoymal(myfile)
            elif rep=="3":
                print("Transformation format xml")
                dictoxml(myfile)
            elif rep=="4":
                rep=False
            else:
                 rep=False

#Fonction pour transformer le fichier json aux autres formats au choix
def transformjson(myfile):
    rep=True
    while rep:
            print(""" 
                    1.Format csv
                    2.Format yaml
                    3.Format xml
                    4.Quitter
            """)
            rep=input("Faites votre choix: ")
            if rep=="1":
                print("Transformation format csv")
                dictocsv(myfile)
            elif rep=="2":
                print("Transformation format yaml")
                dictoymal(myfile)
            elif rep=="3":
                print("Transformation format xml")
                dictoxml(myfile)
            elif rep=="4":
                rep=False
            else:
                 rep=False
#Fonction pour transformer le fichier xml aux autres formats au choix
def transformxml(myfile):
    rep=True
    while rep:
            print(""" 
                    1.Format json
                    2.Format yaml
                    3.Format csv
                    4.Quitter
            """)
            rep=input("Faites votre choix: ")
            if rep=="1":
                print("Transformation format csv")
                dictocsv(myfile)
            elif rep=="2":
                print("Transformation format yaml")
                dictoymal(myfile)
            elif rep=="3":
                print("Transformation format xml")
                dictoxml(myfile)
            elif rep=="4":
                rep=False
            else:
                 rep=False
#Fonction pour transformer le fichier yaml aux autres formats au choix
def transformyaml(myfile):
    rep=True
    while rep:
            print(""" 
                    1.Format json
                    2.Format csv
                    3.Format xml
                    4.Quitter
            """)
            rep=input("Faites votre choix: ")
            if rep=="1":
                print("Transformation format json")
                dictojson(myfile)
            elif rep=="2":
                print("Transformation format csv")
                dictocsv(myfile)
            elif rep=="3":
                print("Transformation format xml")
                dictoxml(myfile)
            elif rep=="4":
                rep=False
            else:
                 rep=False
