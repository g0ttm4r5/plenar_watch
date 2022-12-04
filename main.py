from opendiscourse_page import opendiscourse as Dis
from opendiscourse_page import open_aufbereitung


#list_A =Dis.get_list("politicians") # Zum Beispiel "politicians" oder "factions"
list_C = Dis.get_speeches("11000010") # Id des Politikers bei Opendiscourse

#Sucht Politiker xy auf opendiscourse und ruft weitere Daten ab auf bundestag.de
#for ele in list_A['data']['politicians']:
#    if ele['id'] == '11005260':
#        info_pol = Dis.get_politicians_bundestag(ele['firstName'], ele['lastName'])
#        break


#list_D = Dis.get_politicians_bundestag("Rolf", "Mützenich")

#print(list_A)
#print(info_pol)

stop = open_aufbereitung("master_stopwords.csv")

output_liste = list()

c = 1
for ele in list_C:
    abc = ele['speechContent']

    print("Org: " + str(c) + ": " + str(len(abc)))
    print(abc)
    abc = stop.filtertext(abc)
    print (abc)
    print("Gefiltert: " + str(c) + ": " + str(len(abc)))

    for i in abc:
        output_liste.append(i)

    #break

with open(r'/home/daniel/PycharmProjects/opendiscourse/output_test.txt', 'w') as fp:
    fp.write('\n'.join(map(str, output_liste)))
