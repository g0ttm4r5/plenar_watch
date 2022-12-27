# -*- coding: utf-8 -*-
"""
Created on Sat Dec  3 19:14:34 2022

@author: Meriam Malik
"""


# Daten holen

from opendiscourse_page import opendiscourse as Dis
from opendiscourse_page import open_aufbereitung 


def zerlege_Rede(ID):

    #alle Reden zu Politiker mit ID in eine Liste schreiben
    list_C = Dis.get_speeches(ID) 
    
    list_C = list_C[:1]
    
    onlytext = list()
    
    #alle Reden aus den Dictionaries filtern
    i = 0
    for rede in list_C:
        text = list_C[i]['speechContent']
        
        #Satzzeichen, Füllwörter etc. rausfiltern
        stop = open_aufbereitung("master_stopwords.csv")   
        filteredtext = stop.filtertext(text)
        
        onlytext.append(filteredtext)
        i += 1
 
    return onlytext


def haeufigkeit_woerter(PolitikerID, anzahl):
    reden = zerlege_Rede(PolitikerID)
    woerter = list()
    
    for rede in reden:
       woerter.append(rede.split())
    
    
    haeufigkeit = dict()
    
    for wort in woerter:
        if wort not in haeufigkeit:
            haeufigkeit[wort] = 1
            
        else:
            haeufigkeit[wort] = haeufigkeit[wort] + 1
    
    lst = list()
    for key, val in list(haeufigkeit.items()):
        lst.append((val, key))
          
    lst.sort(reverse = True)
     
    ergebnis ="Die " +str(anzahl) +" häufigsten Wörter sind: "
     
    for key, val in lst[:anzahl + 1]:
          #print(key, val)    
         ergebnis += str(key) + " mal " + str(val) +", " 
    return ergebnis

# Summe aller Woerter
def summe_aller_woerter(PolitikerID): 
      reden = zerlege_Rede(PolitikerID)
      woerter = list()
      
      for rede in reden:
         woerter.append(rede.split())
         
      total = len(woerter)
      
      ergebnis = "\n\nEs sind " + str(total) + " Woerter."
      
      return ergebnis

#Laenge des Textes
def durchschnitt_laenge(PolitikerID):
      reden = zerlege_Rede(PolitikerID)
      
      laenge_aller_reden = None
      zaehler = 0
      
      for rede in reden:
          laenge_aller_reden += len(rede)
          zaehler += 1
    
      durchschnitt = laenge_aller_reden / zaehler
    
      ergebnis = "\n\nDie Reden haben eine durchscnittliche Länge von: " + durchschnitt + " Wörtern."
      return ergebnis

########Debug#######
print(summe_aller_woerter("11000010"))
 