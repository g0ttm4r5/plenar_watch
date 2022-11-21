from opendiscourse_page import opendiscourse as Dis

#list_A =Dis.get_list("politicians") # Zum Beispiel "politicians" oder "factions"
list_C = Dis.get_speeches("11000010") # Id des Politikers bei Opendiscourse
#print(list_A)
print(list_C)

