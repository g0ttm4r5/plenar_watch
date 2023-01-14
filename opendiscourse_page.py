"""
Dateiname: opendiscourse_page.py
Author: Daniel Sellerberg
"""


import io
import os.path
import regex as re
import requests as req
import spacy
import pandas as pd


def asign_cat():
    df = pd.read_csv('output_word2.csv')
    nlp = spacy.load('de_core_news_sm')
    type_word = list()
    counter = 0
    long_counter = 0

    for word2 in df["Wort"]:
        counter += 1
        doc = nlp(str(word2))
        for word in doc:
            if word.pos_ == "NOUN":
                type_word.append(word2)
        if counter == 1000:
            long_counter += counter
            print(long_counter)
            counter = 1

    df_noun = df[df['Wort'].isin(type_word)]
    df_noun.to_csv("output_words_nouns.csv",index=False,encoding= "utf-8")
    print("Ende!")

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
    def get_list(liste):
        # Aufbau URL
        url = "https://api.opendiscourse.de:5300/" + liste
        return get_data(url)

    def get_speeches(politicianIdQuery):
        # Aufbau URL
        url = "https://api.opendiscourse.de:5300/?politicianIdQuery=" + politicianIdQuery
        liste = get_data(url)

        # Sofern mehr als 200 Einträge bestehen, muss ein weiterer Aufruf erfolgen!
        if len(liste['data']['searchSpeeches']) == 200:
            print("Reden unvollständig, da mehr als 200 Einträge")
        elif len(liste['data']['searchSpeeches']) == 0:
            print("keine Reden hinerlegt!")

        return liste['data']['searchSpeeches']

    def get_politicians_bundestag(name, lastname):
        url = "https://www.bundestag.de/statnlp = spacy.load('de_core_news_sm')ic/appdata/sitzplan/data.json"
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

        #Sofern aktiviert, werden nur Nomen zurueckgegeben
        if only_nouns == 1:
            doc = self.nlp(text)
            self.text_filtered = [word.lemma_.capitalize() for word in doc if word.pos_ == "NOUN" and word.text.lower() not in self.stop_list]
        else:
            self.text_filtered = [word for word in text.split(" ") if word.lower() not in self.stop_list]

        return self.text_filtered

