# -------------------------------------------------------
# anagramme.py
#
# tp3.py jeu de l'anagramme entre le pendu et le scrabble
# cree le 12.10.2017
# bug si un anagramme a plusieurs reponses
# (ex: ZESTAIS et TASSIEZ: seul le 1er mot est reconnu)
# -------------------------------------------------------
import random
#
# listes de mots en variables globales
liste_7  = []
liste_8  = []
liste_9  = []

#------------------------
def lire_liste_de_mots():
#------------------------
  f = open("dico.txt");
  chaine = f.read()
  f.close()
  liste = chaine.split()
  print ("nombre total de mots", len(liste))
#
  global liste_7
  global liste_8
  global liste_9
#
  liste_7 = [ mot for mot in liste if len(mot) == 7 ]
  print ("nombre total de mots a 7 lettres: ", len(liste_7))
#
  liste_8 = [ mot for mot in liste if len(mot) == 8 ]
  print ("nombre total de mots a 8 lettres: ", len(liste_8))
#
  liste_9 = [ mot for mot in liste if len(mot) == 9 ]
  print ("nombre total de mots a 9 lettres: ", len(liste_9))
#
  if (len(liste_7) == 0 and len(liste_8) == 0 and len(liste_9) == 0):
    print("Le dictionnaire est vide")
#-------------------------------
def choisir_nombre_de_lettres():
#-------------------------------
  reponse = 0;

  while reponse < 7 or reponse > 9:
    reponse = int(input("Quel est le nombre de lettres pour les mots ? "))
    if (reponse == 7 and len(liste_7) ==0):
      print("Le dictionnaire des mots de 7 lettres est vide")
      reponse = 0
    if (reponse == 8 and len(liste_8) ==0):
      print("Le dictionnaire des mots de 8 lettres est vide")
      reponse = 0
    if (reponse == 9 and len(liste_9) ==0):
      print("Le dictionnaire des mots de 9 lettres est vide")
      reponse = 0
  return reponse
#----------------------
def tirer_mot(longeur):
#----------------------
  if longueur == 7:
    index = random.randrange(len(liste_7))
    return liste_7[index]
  if longueur == 8:
    index = random.randrange(len(liste_8))
    return liste_8[index]
  if longueur == 9:
    index = random.randrange(len(liste_9))
    return liste_9[index]
#---------------------
def jouer(tirage, mot):
#---------------------
  jeu_termine = False
  nombre_de_reponses = 0
  while not jeu_termine: 
    print ("Tirage: ", tirage)
    reponse_joueur = input("Quel le mot original ?")
    if ''.join(reponse_joueur.upper()) == mot:
      print ("Vous avez gagné.")
      jeu_termine = True
      return
    else:
      print ("Mauvaise réponse")
    nombre_de_reponses += 1
    if nombre_de_reponses == 3:
      print ("Vous avez perdu. Le mot original est: ", mot)
      jeu_termine = True
#-----
# main
#-----
lire_liste_de_mots()
longueur = choisir_nombre_de_lettres()
mot = tirer_mot(longueur)
tirage = sorted(mot)
jouer(tirage, mot)
