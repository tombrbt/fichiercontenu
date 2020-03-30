from os import listdir
from os.path import isfile, join

file = open("CesiDate.txt", "w" )
file.write("Nous sommes le 30 septembre 2020")
fichiers = [f for  f in listdir('c:/Users/Hanzo/Desktop/Dossier dev/test') if isfile(join('c:/path', f))]
