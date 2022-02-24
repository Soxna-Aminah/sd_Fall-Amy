from fonction import*
print("Récuperation du fichier")
myext=determineExtension()
extens=myext[1]
fic=myext[0]
verif=verifValidite(extens)
if verif==True:
    print("Veuillez choisir un format")
    myfile=lectureFichier(extens,fic)
    if extens=='csv':
        transformcsv(myfile)
    elif extens=="json":
        transformjson(myfile)
    elif extens=="yaml":
        transformyaml(myfile)
    elif extens=="xml":
        transformxml(myfile)
