from opendiscourse_page import opendiscourse as Dis
from opendiscourse_page import open_aufbereitung

#list_A =Dis.get_list("politicians") # Zum Beispiel "politicians" oder "factions"
#list_C = Dis.get_speeches("11000010") # Id des Politikers bei Opendiscourse

#Sucht Politiker xy auf opendiscourse und ruft weitere Daten ab auf bundestag.de
#for ele in list_A['data']['politicians']:
#    if ele['id'] == '11005260':
#        info_pol = Dis.get_politicians_bundestag(ele['firstName'], ele['lastName'])
#        break

#list_D = Dis.get_politicians_bundestag("Rolf", "Mützenich")

stop = open_aufbereitung("master_stopwords.csv")
