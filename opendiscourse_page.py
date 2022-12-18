import io
import os.path
import regex as re
import requests as req
import spacy



def get_data(url):
    # Defintion des Headers
    hdr = {'User-Agent': 'Mozilla/5.0'}
    # Abruf und R*uckgabe in einer Variable
    response = req.get(url, headers=hdr)

    if response.status_code == 200:
        return response.json()

    else:
        raise ConnectionError("Information nicht abrufbar. Parameter und Verbindung überprüfen!")


class opendiscourse:
    def __init__(self):
        self
        p_list = list()

    def get_list(liste):
        # Aufbau URL
        url = "https://api.opendiscourse.de:5300/" + liste
        return get_data(url)

    def get_speeches(politicianIdQuery):
        # Aufbau URL
        url = "https://api.opendiscourse.de:5300/?politicianIdQuery=" + politicianIdQuery
        liste = get_data(url)

        # Sofern mehr als 200 Einträge bestehen, muss ein weiterer Aufruf erfolgen! [Offen]
        if len(liste['data']['searchSpeeches']) == 200:
            print("Reden unvollständig, da mehr als 200 Einträge")

        return liste['data']['searchSpeeches']

    def get_politicians_bundestag(name, lastname):
        url = "https://www.bundestag.de/static/appdata/sitzplan/data.json"
        abgeordneter = name + " " + lastname
        p_list = get_data(url)

        for ele in p_list:
            if ele != '-1' and p_list[ele]['name'].replace("Dr. ", "") == abgeordneter:
                return p_list[ele]

class open_aufbereitung:

    def __init__(self,path):
        self.text_filtered = ""
        self.path_stopwords = path
        if not os.path.isfile(self.path_stopwords):
            raise FileNotFoundError("Datei existiert nicht")

        # Prüft ob Datei existiert
        self.stop_list = list()
        f = io.open(path,encoding = "utf-8")

        for line in f:
            if line.split(",")[0] != "":
                line = line.rstrip()
                self.stop_list.append(line.split(",")[1])

        #Laden der Spacy Datei
        self.nlp = spacy.load('de_core_news_sm')


    def filtertext(self,text, only_nouns = 1):
        #Ausfiltern von Zeilenumbrüchen
        text = text.replace('\n', ' ')
        #Ausfiltern von Satzzeichen
        text = re.sub(r'[^\w+\s]', '', text)
        #Herausfiltern von Zahlen
        text = re.sub(r'[\d+]', '', text).replace("  "," ")
        self.text_filtered = [word for word in text.split(" ") if word.lower() not in self.stop_list]

        #Sofern aktiviert, werden nur Nomen zurueckgegeben
        if only_nouns == 1:
           doc = self.nlp(text)
           self.text_filtered = [word.lemma_.capitalize() for word in doc if word.pos_ == "NOUN"]

        return self.text_filtered

