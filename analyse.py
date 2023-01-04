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
    
    # nur die letzten fünf Reden betrachten
    list_C = list_C[-5:]
    
    onlytext = list()
    
    #die Reden aus den Dictionaries filtern
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
    haeufigkeit = dict()
    
    for rede in reden:
        for wort in rede:
            if wort not in haeufigkeit:
                haeufigkeit[wort] = 1
                
            else:
                haeufigkeit[wort] = haeufigkeit[wort] + 1
    
    lst = list()
    for key, val in list(haeufigkeit.items()):
        lst.append((val, key))
          
    lst.sort(reverse = True)
     
    ergebnis ="Die"  + str(anzahl) + "häufigsten Wörter in den analysierten Reden sind:"   
     
    for key, val in lst[:anzahl + 1]:
          #print(key, val)    
         ergebnis += str(key) + " mal " + str(val) +", " 
    return ergebnis

# Summe aller Woerter
def summe_aller_woerter(PolitikerID): 
      #alle Reden zu Politiker mit ID in eine Liste schreiben
      list_C = Dis.get_speeches(PolitikerID) 
      #nur die letzten fünf Reden
      list_C = list_C[-5:]
      
      reden = []
        
      for eintrag in list_C:
          reden.append(eintrag['speechContent'])

    
      woerter = list()
      
      for rede in reden:
         woerter.extend(rede.split())
         
      total = len(woerter)
      
      ergebnis = "\n\nDie analysierten Reden haben eine Gesamtlänge von " + str(total) + " Woerter."
      
      return ergebnis

#Laenge des Textes
def durchschnitt_laenge(PolitikerID):
      #alle Reden zu Politiker mit ID in eine Liste schreiben
      list_C = Dis.get_speeches(PolitikerID) 
      reden = []
        
      for eintrag in list_C:
          reden.append(eintrag['speechContent'])
         
      
      laenge_aller_reden = 0
      zaehler = 0
      
      for rede in reden:
          laenge_aller_reden += len(rede)
          zaehler += 1
    
      durchschnitt = laenge_aller_reden / zaehler
    
      ergebnis = "\n\nDie analysierten Reden haben eine durchschnittliche Länge von " + str(durchschnitt.round(2)) + " Wörtern."
      return ergebnis

########Debug#######
#print(summe_aller_woerter("11000010"))
#print(durchschnitt_laenge("11000010"))
print(haeufigkeit_woerter("11000010",5))
 