#
# roulette.py
#
from random import *
from math import *

def jouer():
  reponse = 'O'
  while reponse == 'O':
    try:
      reponse = input("Voulez-vous jouer ? (o/n) ")
    except NameError:
      pass
    reponse = reponse.upper()
    if reponse != 'O':
      exit()
 #
    numero_mise = -1 
    while numero_mise < 0 or numero_mise > 49:
      numero_mise = input("Quel numero ? ")
      numero_mise = int(numero_mise)
 #
    mise = 0
    while mise <= 0:
      mise = input("Quelle mise ? ")
      mise = float(mise)
 #
    print("Vous jouez ",  mise, " euro(s) sur le numero ", numero_mise, ".")
 #
    numero_sorti = randrange(1, 49) 
    print ("Le numero ", numero_sorti, " est sorti.")
 #  
    if (numero_sorti == numero_mise): 
      print ("Votre numero est sorti: vous avez gagne ", mise * 3, " euros.")
    elif (numero_mise % 2 == numero_sorti % 2):
      print ("Le numero sorti a la meme couleur que votre numero: vous avez gagne ", mise / 2, "euros.")
    else:
      print ("Vous avez perdu ", mise, "euros.") 
#
jouer()
