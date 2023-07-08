"""
 cce.py:
"""
colonnes = "abcdefgh"
colonne_pos = -1 
while colonne_pos == -1:
    colonne = input("Entrez colonne:")
    colonne_pos = colonnes.find(colonne)

lignes = "12345678"
ligne_pos = -1
while ligne_pos == -1:
    ligne=(input("Entrez ligne:"))
    ligne_pos = lignes.find(ligne)
#
colonnes_impaires = "aceg"
colonnes_paires = "bdfh"
lignes_impaires = "1357"
lignes_paires = "2468"

if (colonnes_impaires.find(colonne) >= 0 and lignes_impaires.find(ligne) >= 0) or (colonnes_paires.find(colonne) >= 0 and lignes_paires.find(ligne) >= 0):
    print(f"case {colonne}{ligne}: noire")
else:
    print(f"case {colonne}{ligne}: blanche")
