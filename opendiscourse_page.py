import requests as req

def get_data(url):
    # Defintion des Headers
    hdr = {'User-Agent': 'Mozilla/5.0'}
    # Abruf und R*uckgabe in einer Variable
    response = req.get(url, headers=hdr)

    if response.status_code == 200:
        return response.json()
    else:
        print("Information nicht abrufbar. Parameter und Verbindung überprüfen!")

class opendiscourse:

    def __init__(self):
        self

    def get_list(liste):
        #Aufbau URL
        url = "https://api.opendiscourse.de:5300/" + liste
        return get_data(url)

    def get_speeches(politicianIdQuery):
        # Aufbau URL
        url = "https://api.opendiscourse.de:5300/?politicianIdQuery=" + politicianIdQuery
        liste = get_data(url)

        #Sofern mehr als 200 Einträge bestehen, muss ein weiterer Aufruf erfolgen! [Offen]
        if len(liste['data']['searchSpeeches']) == 200:
            print("Reden unvollständig, da mehr als 200 Einträge")

        return liste['data']['searchSpeeches']

