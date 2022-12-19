# -*- coding: utf-8 -*-
"""
Created on Sat Dec  3 19:14:34 2022

@author: Meriam Malik
"""
import string

# Daten holen

from opendiscourse_page import opendiscourse as Dis
from opendiscourse_page import open_aufbereitung 


def haeufigstes_wort(anzahl):

    list_C = Dis.get_speeches("11000010") # Id des Politikers bei Opendiscourse
    
    # dict aus Liste holen
    
    dtext = list_C[0]
    
    # Redeteil aus dict holen
    
    text = dtext["speechContent"]
    
    # Satzanfaenge klein schreiben
    
    #text = text.lower()
    
    # Sonderzeichen entfernen (?.() usw)
    
    #text = text.translate( text.maketrans("", "", string.punctuation))
    stop = open_aufbereitung("master_stopwords.csv")
    
    words = stop.filtertext(text)
    
    # in Woerter splitten
  
   # words = text.split()
    
    # Haeufigkeiten
    
    haeufigkeit = dict()
    
    for wort in words:
        if wort not in haeufigkeit:
            haeufigkeit[wort] = 1
            
        else:
            haeufigkeit[wort] = haeufigkeit[wort] + 1
            
   # print(haeufigkeit)        
    
    # Sortieren der haeufigsten Woertern
    
    lst = list()
    for key, val in list(haeufigkeit.items()):
        lst.append((val, key))
        
    lst.sort(reverse = True)
    
    ergebnis ="Die " +str(anzahl) +" häufigsten Wörter sind: "
    
    for key, val in lst[:anzahl + 1]:
        #print(key, val)    
        ergebnis += str(key) + " mal " + str(val) +", " 
    
    
    
    # Summe aller Woerter
    total = len(text.split())
    ergebnis += "\n\nEs sind " + str(total) + " Woerter."
    
    #Laenge des Textes
    
    ergebnis += "\n\nDer Text hat: " + str(len(text)) + " Zeichen."
    # Durchschnittliche Laenge aller Texte eines Politikers 
    
    return ergebnis
   
print(haeufigstes_wort(5))