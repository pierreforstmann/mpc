# Python notes
document created 03-OCT-2017

## Basics 
To exit the interpreter: 
<pre>
>> exit
Use exit() or Ctrl-D (i.e. EOF) to exit
>>> exit()
</pre>
A variable is automatically declared at definition time and can be deleted with del:
<pre>
>>> myvar=1
>>> myvar
1
>>> del myvar
>>> myvar
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'myvar' is not defined
>>> 
</pre>
<br>
Lists are indexed collection (first item has index 0) using square brackets:
<pre>
>> l = [1,2,3]
>>> l
[1, 2, 3]
>>> l[0]=0
>>> l
[0, 2, 3]
>>> 
</pre>
Dictionaries are collections of key/value pairs indexed by keys that can be alphanumeric (dictionaries are not ordered):
<pre>
>>> dic = { "one": 1, "two": 2}
>>> dic
{'two': 2, 'one': 1}
>>> dic["one"]=11
>>> dic
{'two': 2, 'one': 11}
>>> 
</pre>
Note that even if dictionaries are built using braces, values are accessed with square brackets.
<br>
<br>
IF THEN ELSE syntax has no THEN and *MUST* use indentation for THEN and ELSE blocks:
<pre>
>>> if 0 == 0:
...   print "OK"
... else:
...   print "KO"
... 
OK
>>> 
</pre>
There is a keyword for blocks with no action to avoid syntax error:
<pre>
>>> if 2 == 2:
...   pass
... 
>>> 
</pre>
WHILE loops *MUST* also use indentation for WHILE block:
<pre>
>>> i=1
>>> while i < 5:
...   print i
...   i+=1
... 
1
2
3
4
>>> 
</pre>
FOR loops *MUST* also use identation for FOR block (note that FOR loop iterates on a collection):
<pre>
>> l = [1, 2, 3, 4]
>>> for i in l:
...   print i
... 
1
2
3
4
>>> 
</pre>
Functions are defined with def keyword and *MUST* also used indentation for function block:
<pre>
>>> def printf(msg):
...   print "printf: " + msg
... 
>>> printf ("OK")
printf: OK
>>> 
</pre>
Standard methods for strings:
<br>
<br>
<code>string.split()</code> to build a list from a string
<br>
<code>string.strip()</code> to remove starting and ending space charactes
<br>
<code>string.upper()</code> to have all letters in uppercase
<br>
<code>string.lower()</code> to have all letters in lowercase
<br>
<code>string.format(variable=value</code> to replace occurences of <code>{variable}</code> by <code>value</code> 
<br>
<code>string.format(value)</code> to replace occurences of <code>{}</code> by <code>value</code>:
<pre>
>>> "Nous sommes le {} {} {}".format("vendredi","13","octobre")
'Nous sommes le vendredi 13 octobre'
>>> 
</pre>
Useful method for numbers:
<br>
<br>
<code>(number).is_integer()</code>
<br>
<br>
Standard methods for lists:
<br>
<br>
<code>list.index(value)</code> to return index of <code>value</code>
<br>
<code>list.append(value)</code> to add at list end <code>value</code>
<br>
<code>list[index] = value</code> to modify directly a list value
<br>
<code>list.remove(value)</code> to remove <code>value</code> from list
<br>
<code>len(list)</code> to get number of list items.
<br>
<br>
Standard methods for dictionaries:
<br>
<br>
<code>for k in dict.keys():</code> to loop over dictionary keys
<br>
<code>for v in dict.values():</code> to loop over dictionary values
<br>
<code>for k,v in dict.items():</code> to loop over dictionary keys and values
<br>
<code>dict.update[{key:value}]</code> to update <code>key/value</code>
<br>
<code>dict.pop(key)</code> to remove item
<br>
<code>dict.[key] = value </code> to modify directly an item.
<br>
<br>
<h3>Functions</h3>
Functions parameters have no type and cannot be overloaded (but they can have default values):
<pre>
>>> def c(x=5):
...   return x*x
... 
>>> c()
25
>>> c(4)
16
>>> 
</pre>
Lambda functions allow to define a function without naming it (function parameters are defined before ':' and function body is defined after ':'):
<pre>
>>> f = lambda x: x * x
>>> f(5)
25
>>> f(-18)
324
>>> 
</pre>
A module is a <b>.py</b> file containg python code: its content is made available with <code>import</code> statement.
<br>
Following code is only run when executing directly module file (it is <u>not</u> run at import time):
<pre>
if __name__ == "__main__":
    ...
    ...
</pre>
<h3>Exceptions</h3>
Example with different exceptions:
<pre>
try:
    ...
except NameError:
    -- some variable is not defined
except TypeError:
    -- some variable type is not compatible with some operation
except ZeroDivisionError:
    -- self explanatory
else:
    --
</pre>
Example with finally clause (code in finally clause is <u>always executed</u>):
<pre>
try:
    ...
except <i>exception_type</i>:
    ...
finally:
    # code run whether exception has been raised or not
</pre>
Example of "roulette" game:

```
# tp 2: ZCasino 

from random import *
from math import *

def jouer():
  reponse = 'O'
  while reponse == 'O':
    try:
      reponse = raw_input("Voulez-vous jouer ? (o/n) ")
    except NameError:
      pass
    reponse = reponse.upper()
    if reponse != 'O':
      exit()
 #
    numero_mise = -1 
    while numero_mise < 0 or numero_mise > 49:
      numero_mise = raw_input("Quel numero ? ")
      numero_mise = int(numero_mise)
 #
    mise = 0
    while mise <= 0:
      mise = raw_input("Quelle mise ? ")
      mise = float(mise)
 #
    print "Vous jouez ",  mise, " euro(s) sur le numero ", numero_mise, "."
 #
    numero_sorti = randrange(1, 49) 
    print "Le numero ", numero_sorti, " est sorti."
 #  
    if (numero_sorti == numero_mise): 
      print "Votre numero est sorti: vous avez gagne ", mise * 3, " euros."
    elif (numero_mise % 2 == numero_sorti % 2):
      print "Le numero sorti a la meme couleur que votre numero: vous avez gagne ", mise / 2, "euros."
    else:
      print "Vous avez perdu ", mise, "euros." 
#
jouer()
```

<h3>Lists and tuples</h3>
<li>lists are mutables sequences that can contain other objets</li>
<li>to build a list: <code> list = [ item1, item2, itemN ]</code></li>
<li>items can be inserted in a list with following methods: <code>append, insert, extend</code>
<li>lists can be concatenated with + or with <code>extend</code> method
<li>items can be removed from a list with keyword <code>del</code> or with method <code>remove</code>
<li><code>enumerate</code> function in a <code>for</code> loop on a list returns index and item</li>
<pre>
for i, elt in enumerate(my_list):
...     print("At index {} there is {}.".format(i, elt))
</pre>
<li>tuples are immutables sequences</li>
<li>to build a tuple: <code> tuple1=(1,) tuple3 = (1,2,3)</code>
<li>a function can return different variables as a tuple</li>
<br>
Strings can be turned into lists with <code>split</code> method:
<pre>
>>> ma_chaine = "Bonjour à tous"
>>> ma_chaine.split(" ")
['Bonjour', 'à', 'tous']
>>>
</pre>
Lists can be turned into strings with <code>join</code> method (note that the object used for <code>join</code> is the string to be used a separator):
<pre>
>>> ma_liste = ['Bonjour', 'à', 'tous']
>>> " ".join(ma_liste)
'Bonjour à tous'
>>>
</pre>
Functions can take a variable parameter list with:
<code>
def fonction(*parametres):
</code>
in function code all the arguments are a single tuple.
<br>
<br>
Comprehension list is way to filter data in a new list from an existing list:
<pre>
new_list = [ "expression" for element in existing_list if "condition" ]
</pre>
<h3>Dictionaries</h3>
<li>Dictonaries store keys/values</li>
<li>Dictionary is build with <code>dict = {key1:value1, key2:value2, keyN:valueN}</code></li>
<li>Dictionary element can be added or replaced with:<code> dict[key] = value</code></li>
<li>Dictionary element can be removed with <code>del</code> keyword or <code>pop()</code> method </li>
<li>Iteration on dictionaries can be made with <code>keys()</code>, <code>values()</code> or <code>items()</code>
<li>Function parameters can retrieved in a dictionary with: <code>def function (**parameters)</code></li>
<li><u>Unnamed</u> function parameters can be retrieved in <code>in_list</code> and <u>named</u> function parameters can be retrieved in <code>in_dictionary</code> in
following function declaration: <code>def f (*in_list, **in_dictionary)</code>
<h3>File management</h3>
<li><code>open</code> function is used to open a file</li>
<li><code>read</code> method is used to read from a file</li>
<li><code>write</code> method is used to write to a file</li>
<li>pickle module allows to read and write objects from/into files.</li>
<h3>Variable scope and references</h3>
<li>function can read variables from outer scope but cannot write them</li>
<li>variables defined in function are deleted after function call</li>
<li>function can modify variable indriectlry by calling object methods</li>
<li>keyword <code>global</code> allows to reference global variable in function</li>
<h3>Code example of anagram game</h3> 

```
-------------------------------------------------------
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
liste_10 = []
liste_11 = []
liste_12 = []

#------------------------
def lire_liste_de_mots():
#------------------------
  f = open("/mnt/seagate/docs_en_lecture_seule/scrabble/ods5.txt");
  chaine = f.read()
  f.close()
  liste = chaine.split()
  print "nombre total de mots", len(liste)
#
  global liste_7
  global liste_8
  global liste_9
  global liste_10
  global liste_11
  global liste_12
#
  liste_7 = [ mot for mot in liste if len(mot) == 7 ]
  print "nombre total de mots a 7 lettres: ", len(liste_7)
#
  liste_8 = [ mot for mot in liste if len(mot) == 8 ]
  print "nombre total de mots a 8 lettres: ", len(liste_8)
#
  liste_9 = [ mot for mot in liste if len(mot) == 9 ]
  print "nombre total de mots a 9 lettres: ", len(liste_9)
#
  liste_10 = [ mot for mot in liste if len(mot) == 10 ]
  print "nombre total de mots a 10 lettres: ", len(liste_10)
#
  liste_11 = [ mot for mot in liste if len(mot) == 11 ]
  print "nombre total de mots a 11 lettres: ", len(liste_11)
#
  liste_12 = [ mot for mot in liste if len(mot) == 12 ]
  print "nombre total de mots a 12 lettres: ", len(liste_12)
#
#-------------------------------
def choisir_nombre_de_lettres():
#-------------------------------
  reponse = 0;
  while reponse < 7 or reponse > 12:
    reponse = input("Quel est le nombre de lettres pour les mots ? ") 
  return reponse
#----------------------
def tirer_mot(longeur):
#----------------------
  if longueur == 7:
    index = random.randrange(len(liste_7))
  return liste_7[index]
#---------------------
def jouer(tirage, mot):
#---------------------
  jeu_termine = False
  nombre_de_reponses = 0
  while not jeu_termine: 
    print "Tirage: ", tirage
    reponse_joueur = raw_input("Quel le mot original ?")
    if ''.join(reponse_joueur.upper()) == mot:
      print "Vous avez gagne."
      jeu_termine = True
    else:
      print "Mauvaise reponse"
    nombre_de_reponses += 1
    if nombre_de_reponses ==  3:
      print "Vous avez perdu. Le mot original est: ", mot
      return
#-----
# main
#-----
lire_liste_de_mots()
longueur = choisir_nombre_de_lettres()
mot = tirer_mot(longueur)
#print "=> mot: ", mot
tirage = sorted(mot)
#print "=> tirage: ", tirage
jouer(tirage, mot)
```
<h2> Object Oriented Programming </h2>
<li>class is defined with <code>class className:</code></li>
<li>methods ade defined like functions except that code is inside class definition</li>
<li>instance methods first parameter is named <code>self</code> and represents current object instance</li>
<li>class instances are created with constructor named <code>__init__</code></li>
<li>instance attributes are set with: <code> self.attribute_name = value </code></li>
<br>
<br>
<li>properties allow to control access to instance attributes</li>
<li>properties are defined in class definition with: 
<pre>
property_name = property(get_method, set_method, delete_method, help_method)
</pre>
<li>when reading attribute , getter method is executed</li>
<li>when modifying attriubte, setter method is executed</li>
<li>note that each property parameter is optional.</li>
<br>

<li> special methods allow to change how instance attributes are accessed or how operators or conversions are handled </li>
<li> special method name must start with <code>"__"</code> and end with <code>"__"</code> </li>
<li> methods <code>__getattr__, __setattr__</code> and <code>__delattr__ </code>are used for instance attributes access </li>
<li> methods <code>__getitem__, __setitem__</code> and <code>__delitem__ </code> overload indexation (<code>[]</code>) </li>
<br>
<br> Example of how <code>__setitem__</code> is automatically called.
<br> Here is source code:

```
# -*- coding: utf8 -*-
class DictionnaireOrdonne:

  def __init__(self, base={}, **donnees):
   self._cles = [] # Liste contenant nos cles
   self._valeurs = [] # Liste contenant les valeurs correspondant a nos cles

   if type(base) not in (dict, DictionnaireOrdonne):
     raise TypeError( "le type attendu est un dictionnaire (usuel ou ordonne)")
   for cle in base:
     self[cle] = base[cle]
   for cle in donnees:
     print "=> __init__ before: cle = ", cle
     print "=> __init__ before: self._cles = ", self._cles
     print "=> __init__ before: self._valeurs = ", self._valeurs
     self[cle] = donnees[cle]
     print "=> __init__ after: self._cles = ", self._cles
     print "=> __init__ after: self._valeurs = ", self._valeurs
#
  def __setitem__(self, cle, valeur):
    print "=> __setitem__ cle=", cle, " valeur=", valeur
    if cle in self._cles:
       indice = self._cles.index(cle)
       self._valeurs[indice] = valeur
    else:
      self._cles.append(cle)
      self._valeurs.append(valeur)
#
legumes = DictionnaireOrdonne(carotte = 26, haricot = 48)
```
Running above code generates following output:

```
$ python testdo.py 
=> __init__ before: cle =  carotte
=> __init__ before: self._cles =  []
=> __init__ before: self._valeurs =  []
=> __setitem__ cle= carotte  valeur= 26
=> __init__ after: self._cles =  ['carotte']
=> __init__ after: self._valeurs =  [26]
=> __init__ before: cle =  haricot
=> __init__ before: self._cles =  ['carotte']
=> __init__ before: self._valeurs =  [26]
=> __setitem__ cle= haricot  valeur= 48
=> __init__ after: self._cles =  ['carotte', 'haricot']
=> __init__ after: self._valeurs =  [26, 48]
```

<br>
<li> methods <code>__add__, __sub__, __mul__ </code> ... overload mathematical operators </li>
<li> methods <code> _eq__, __ne__, __gt__ </code> ... overload comparison operators </li>
<li> method <code> __repr__ </code> is called by Python interpretor when instance name is typed (it must return a string) </li>
<li> method <code> __str__ </code> is called by Python when print function is called on instance name or when <code>str</code> function is called to convert instance to string</li> 
<li> method <code> __contains__ </code> is called when <code>in</code> operator is used on instance that is a collection</li>
<li> method <code> __len__ </code> is called when <code>len</code> when function is called for a instance that is a collection</li>
<br>
<li> inheritance allows a class to inherit methods from another class</li>
<li> inheritance syntax is <code> class NewClass(ParentClass):</code> </li>
<li> parent class methods can be accessed with: <code> ParentClass.method(self) </code> </li>
<li> multiple inheritance allows to inherit from several parent classes </li>
<li> multiple inheritance syntax is : <code> class NewClass(ParentClass1, ParentClass2, ParentClassN):</code></li>
<li> exceptions are objects inheriting from <code>BaseException</code> class </li>
<li> exceptions that are not errors should inherent from <code>BaseException</code> class</li>
<li> exceptions that are errors should inherit from <code> Exception </code> class.</li>
<br>
<br>
<h2> Iterators and generators</h2>
<li> when <code>for element in sequence</code> is used an sequence iterator allows to read the sequence</li>
<li> <code>iter</code> function allows to access directly a sequence iterator </li>
<li> a sequence iterator can also be accessed using special method <code>__iter__</code></li>
<li> iterator has a special method <code>__next__</code> that returns the next item or raises <code>StopIteration</code> exception that stops the loop </i>
<li> generators allow to create iterators more easily </li>
<li> generators are functions that use <code>yield</code> keyword followed by value to be returned to the loop.</li>
<br>
<br>
Manual generator:
<pre>
>>> def mygen():
...   yield 1
...   yield 2
...   yield 3
... 
>>> mygen
<function mygen at 0x7fa45e9299b0>
>>> mygen()
<generator object mygen at 0x7fa45e91dfa0>
>>> for v in mygen():
...   print v
... 
1
2
3
>>> 
</pre>
Automatic generator:
<pre>
def intervalle(borne_inf, borne_sup):
    """Generateur parcourant la serie des entiers entre borne_inf et borne_sup.
     Note: borne_inf doit etre inferieure a borne_sup"""
    borne_inf += 1
    while borne_inf < borne_sup:
        yield borne_inf
        borne_inf += 1
>>> for nombre in intervalle(5, 10):
...     print(nombre)
... 
6
7
8
9
>>>
</pre>

<h2> Sorting </h2>
<li> Python can sort data using list <code>sort</code> method that modifies the list or using the <code>sorted</code> function that does not modify the current list</li>
<li> Functions key can be specified with <code>key</code> argument. These functions are called for each sequence item to sort and return sort criteria</li>
<br>
To sort a tuple list on tuple 3rd column using a lambda function:

```
>>> sorted(etudiants, key=lambda colonnes: colonnes[2])
[
    ('Thomas', 11, 12), 
    ('Charles', 12, 15), 
    ('Damien', 12, 15), 
    ('Clement', 14, 16),
    ('Oriane', 14, 18)
]
>>>
```

To sort a list of objects on "moyenne" attribute using a lambda function:

```
>>> 
sorted(etudiants, key=lambda etudiant: etudiant.moyenne)
[

    &ltEtudiant Thomas (Age=11, moyenne=12)>,
    &ltEtudiant Charles (Age=12, moyenne=15)>,
    &ltEtudiant Damien (Age=12, moyenne=15)>,
    &ltEtudiant Clement (Age=14, moyenne=16)>,
    &ltEtudiant Oriane (Age=14, moyenne=18)>
]
>>>
```

<li> <code>operator</code> module gives <code>itemgetter</code> and <code>attrgetter</code> to allow sorting tuples list or object list by given attribute</li>
<li> Python sorting is "stable" which means that idem order is not changed if they are considered equal for sorting: this allow to chain sorting. </li>
<br>
<br>

<h3> Some learnings </h3>
<li>Python error <code>NameError: global name 'NAME' is not defined</code> in class code is likely due either to missing <code>self</code> argument in method definition or to missing <code>self</code> argument in method call.</li>
<li>Strings are immutable but a string can be built character by character with <code>'+'</code> operator: <code> s = s + 'c' </code></li>
<li>Do not mix up variable name and function name: a variable can have the same name as function but it will still be a variable (the function having the same name will NOT be called due to missing parenthesis ...)</li>
<li>If indentation is wrong in a simple function having only a return statement, nothing will be executed and Python will return a default value !</li>
<h3> Virtual Environments </h3>
To create a virtual environment (<code>-p</code> must be set to full path name of python executable </code>):
<pre>
$ virtualenv -p /usr/local/bin/python3.6 env
</pre>
To activate above created virtual environment (parameter is based on directory created by <code>virtualenv</code>:
<pre>
$ source env/bin/activate
</pre>

