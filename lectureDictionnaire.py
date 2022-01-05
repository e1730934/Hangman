import string, random


def ouvertureFichier(nomFichier):
    dictionnaire = []
    with open(nomFichier, "r", encoding="UTF-8") as source_f:
        for line in source_f:
            listElement = line.split()
            for element in listElement:
                for iteration in range(len(element)):
                    siMot = True
                    if (element[iteration]).lower() not in (string.ascii_letters + "âêîôûéàèù"):
                        siMot = False
                        break
                if siMot:
                    mot = element.upper()
                    if mot not in dictionnaire:
                        dictionnaire.append(mot)
    return dictionnaire
