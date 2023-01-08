"""
Dateiname: plenarwatch_fenster
Authorin: Angelika Martin
"""

# Import der Bibliotheken
from opendiscourse_page import opendiscourse as Dis, open_aufbereitung
from wortwolke import wortwolke_erzeugen
from balkendiagramm import balkendiagramm_zeichnen
from tkinter import *
from tkinter import messagebox
from analyse_fenster import analysefenster_anzeigen
from vergleich_fenster import vergleichsfenster_anzeigen

# ------------------------- Funktionen ----------------------------------

def erstelle_liste():
    """Diese Funktion extrahiert aus der Politiker:innenliste die Vornamen und Nachnamen der Politiker:innen
    und erzeugt daraus eine Liste im Format 'Vorname Nachname'"""

    liste_p = Dis.get_list("politicians")
    daten = list()
    i = 0
    for n in liste_p['data']['politicians']:
        # übernimmt alle Politiker:innen mit einer id ungleich -1
        if liste_p['data']['politicians'][i]['id'] != '-1':
            daten.append(liste_p['data']['politicians'][i]['firstName'] + ' ' + liste_p['data']['politicians'][i]['lastName'])
            i += 1
    return daten


def suche_polid(name):
    "Diese Funktion holt sich die ID eines/einer Politiker:in aus der Politikerliste"
    liste_p = Dis.get_list("politicians")

    i = 0
    for n in liste_p['data']['politicians']:
        t = liste_p['data']['politicians'][i]['firstName'] + ' ' + liste_p['data']['politicians'][i]['lastName']
        if name == t:
            polid = liste_p['data']['politicians'][i]['id']
            break
        i += 1

    return polid


def hole_reden(id):
    """Diese Funktion holt sich die Wörter einer bestimmten oder eines bestimmten Politikers aus der bereinigten Rede."""

    # Eine Instanz des Objekts open_aufbereitung wird erstellt
    Auf = open_aufbereitung("master_stopwords.csv")

    # Zunächst werden Reden geladen, danach auf die letzten fünf Reden reduziert
    all_speeches = Dis.get_speeches(id)
    anzahl_reden = len(all_speeches)
    all_speeches = all_speeches[-5:]
    anzahl_analysierte_reden= len(all_speeches)

    # Die Inhalte der Reden werden extrahiert und in einer Liste gespeichert
    liste_reden = list()
    i = 0
    for n in range(i, len(all_speeches)):
        liste_reden.append(all_speeches[i]['speechContent'])
        i += 1

    # Alle Listeneinträge werden als String mit einem Leerzeichen als Trenner zusammengesetzt, um sie mit der Stoppwort-
    # liste bereinigen zu können (filtertext).
    trennzeichen = ' '
    text_reden = trennzeichen.join(liste_reden) # string
    reden_gefiltert = Auf.filtertext(text_reden) # list

    return liste_reden, reden_gefiltert, anzahl_reden, anzahl_analysierte_reden

def hole_zehnwoerter(liste):

    d = dict()
    for w in liste:
        d[w] = d.get(w,0) + 1  # dictionary

    list_sorted = sorted(d.items(), key=lambda e:e[1], reverse=True)   # list
    d_sorted = dict(list_sorted[:10])   # dictionary
    return d_sorted


def lbox_fuellen(liste, lbox):
    """Diese Funktion ist dafür zuständig, die Listbox für die Politer:innen mit den entsprechenden
    Namen zu füllen. Sie übernimmt als Argumente die Politiker:innenliste und den Namen der Listbox. Diese Funktion
    befüllt, da sie als Argument auch den Listboxnamen übernimmt alle Listboxen auf der grafischen Oberfläche."""

    # Die Listbox wird geleert (alles: zwischen Anfang (0) und Ende)
    lbox.delete(0, END)
    # Jedes Element in der Liste wird in der Listbox ergänzt. Die Methode insert ist folgendermaßen
    # definiert: insert (Index, elements). Wird END als Index eingegeben, dann  werden neue Zeilen mit dem Wert "item"
    # an das Ende der Listbox gesetzt."""
    for item in liste:
        lbox.insert(END, item)


def lbox_person_auswaehlen(ebox, lbox):
    """Die Funktion lbox_person_auswaehlen wird ausgeführt, wenn ein Wert in einer Listbox ausgewählt wird.
    Sie weist der entsprechenden Eingabebox den Wert zu, der in der Listbox ausgewählt wurde."""

    # Das Eingabefeld wird geleert (alles: zwischen Anfang (0) und Ende)
    ebox.delete(0, END)
    # Das Eingabefeld übernimmt den Wert aus der Listbox, der dort markiert ist (wenn etwas in der Listbox
    # durch einen Mausklick markiert ist, dann erhält dieses Element den "ANCHOR"), an die Position 0 (Index)
    ebox.insert(0, lbox.get(ANCHOR))


def pruefe_lbox_eintraege(ebox, lbox):
    """Die Funktion pruefe_lbox_eintraege realsiert die Suche- und Auto-Fill-Funktionalität und ist an die Eingabefelder
    gebunden. Immer wenn ein Zeichen eingeben wurde (und ein neuer Teilstring entsteht), wird in der Politiker:innenliste
    überprüft, ob dieser Teilstring in den einzelnen Namen vorhanden ist. Ist das der Fall, wird eine neue Liste erstellt,
    die nur die Einträge enthält, in denen der Teilstring vorkommt."""

    # Der Wert aus dem Eingabefeld wird übernommen
    eingabe = ebox.get()
    # Wenn das Eingabefeld leer ist, übernimmt data die gesamte Politiker:innenliste
    if eingabe == '':
        data = pol_liste
        # ansonsten übernimmt data nur die Werte, die mit dem eingegebenen Teilstring übereinstimmen
    else:
        data = []
        for item in pol_liste:
            # Fehler durch Groß- und Kleinschreibung werden verhindert, indem die Strings in Kleinschreibung
            # # verglichen werden
            if eingabe.lower() in item.lower():
                data.append(item)
    # Die Funktion lbox_füllen wird mit den Argumenten data (aktuelle Liste, die angezeigt werden soll) und dem Namen
    # der entsprechenden Listbox aufgerufen
    lbox_fuellen(data, lbox)


def analyse_ausgeben():
    """Diese Funktion übernimmt den Politiker:innennamen aus dem Textfeld und sammelt alle Informationen über diese
    Person, die dann als Ergebnisse auf dem Analysefenster ausgegeben werden (inklusive Balkendiagramm und Wortwolke)."""

    # Den ausgewählten Namensstring aus dem Listenfeld in name1_auswahl übernehmen
    name1_auswahl = eingabe_name1.get()

    # Für den Fall, dass ein korrekter Name für eine:n Politiker:in im Textfeld steht
    try:
        # Die Politiker-ID zum Namen ermitteln und in polid übernehmen
        polid = suche_polid(name1_auswahl)

        # Hinweis darauf, dass die Analyse längere Zeit in Anspruch nehmen kann
        messagebox.showinfo('Analyse läuft', 'Bitte etwas Geduld!\n\nDie Analyse kann einige Minuten dauern ...\n\n'
                                         'Auf die Schaltfläche OK klicken, um die Analyse zu starten!', icon='info')

        # Die Informationen zu den Reden werden ermittelt
        liste_reden, reden_gefiltert, anzahl_reden, anzahl_analysierte_reden = hole_reden(polid)
        trenner = ' '
        substantive_reden = trenner.join(reden_gefiltert) # string

        # Die häufigsten zehn Wörter für das Diagramm werden ermittelt
        diagram_werte = hole_zehnwoerter(reden_gefiltert)

        # Die Wortwolke und das Diagramm werden erzeugt
        wortwolke_erzeugen('tmp_images/analyseimage.png', substantive_reden)
        balkendiagramm_zeichnen('tmp_images/balkendiagramm.png', diagram_werte)

        # Das Analysefenster wird erzeugt
        analysefenster_anzeigen(name1_auswahl, polid, anzahl_reden, anzahl_analysierte_reden)
    # Wird ein Name im Textfeld erkannt, der sich nicht in der Politiker:innenliste befindet, wird ein Hinweis in
    # Form eines Infofensters ausgegeben

    except:
        messagebox.showinfo('Politiker:in nicht gefunden!', 'Bitte einen Namen im Textfeld "Namen suchen (Filter)"\n'
                                                            'eingeben und im Listenfeld "Name auswählen" anklicken.\n\n'
                                                            'Dann erneut die Schaltfläche "Analysieren" anklicken.',
                                                            icon='info')

def vergleich_ausgeben():
    """Diese Funktion übernimmt die Politiker:innennamen aus den Textfeldern und sammelt alle Informationen über diese
    Personen, die dann als Ergebnisse auf dem Vergleichsfenster ausgegeben werden (inklusive Balkendiagramm und
    Wortwolke)."""

    # Die ausgewählten Namen aus den Textfeldern übernehmen
    name5_auswahl = eingabe_name3.get()
    name6_auswahl = eingabe_name4.get()

    # Für den Fall, dass korrekte Namen für zwei Politiker:innen im Textfeld stehen
    try:
        # Die Politiker-IDs zu den Namen ermitteln und in polid übernehmen
        polid1 = suche_polid(name5_auswahl)
        polid2 = suche_polid(name6_auswahl)

        # Hinweis darauf, dass die Analyse längere Zeit in Anspruch nehmen kann
        messagebox.showinfo('Analyse läuft', 'Bitte etwas Geduld!\n\nDie Analyse kann einige Minuten dauern ...\n\n'
                                         'Auf die Schaltfläche OK klicken, um die Analyse zu starten!', icon='info')

        # Die Informationen zu den Reden werden ermittelt
        liste_reden1, reden_gefiltert1, anzahl_reden1, anzahl_analysierte_reden1 = hole_reden(polid1)
        liste_reden2, reden_gefiltert2, anzahl_reden2, anzahl_analysierte_reden2 = hole_reden(polid2)
        trenner = ' '
        substantive_reden1 = trenner.join(reden_gefiltert1)  # string
        substantive_reden2 = trenner.join(reden_gefiltert2)

        # Die häufigsten zehn Wörter für die Diagramme werden ermittelt
        diagram_werte1 = hole_zehnwoerter(reden_gefiltert1)
        diagram_werte2 = hole_zehnwoerter(reden_gefiltert2)

        # Die Wortwolken und die Diagramme werden erzeugt
        wortwolke_erzeugen('tmp_images/analyseimage1.png', substantive_reden1)
        wortwolke_erzeugen('tmp_images/analyseimage2.png', substantive_reden2)
        balkendiagramm_zeichnen('tmp_images/balkendiagramm1.png', diagram_werte1)
        balkendiagramm_zeichnen('tmp_images/balkendiagramm2.png', diagram_werte2)

        # Das Vergleichsfenster wird erzeugt
        vergleichsfenster_anzeigen(name5_auswahl, name6_auswahl, polid1, polid2, anzahl_reden1, anzahl_reden2,
                               anzahl_analysierte_reden1, anzahl_analysierte_reden2)

    # Wird ein Name im Textfeld erkannt, der sich nicht in der Politiker:innenliste befindet, wird ein Hinweis in
    # Form eines Infofensters ausgegeben
    except:
        messagebox.showinfo('Politiker:innen nicht gefunden!', 'Bitte je einen Namen im Textfeld "Namen suchen (Filter)"\n'
                                                               'eingeben und im Listenfeld "Namen auswählen" anklicken.\n\n'
                                                               'Dann erneut die Schaltfläche "Vergleichen" anklicken.',
                                                                icon='info')

# ----------------------------------------------- Fenster aufbauen -------------------------------------------------

# Fenstergerüst (TKinter) erstellen
start_fenster = Tk()
start_fenster.title('PlenarWatch')
start_fenster.geometry('900x600')

# Die Politikerliste erstellen, um sie in die Listenfelder aufzunehmen
pol_liste = erstelle_liste()

# Definition des grid-Rasters zur Platzierung der Widgets. Für die Reihendefinition:
start_fenster.grid_rowconfigure(0, weight=1)
start_fenster.grid_rowconfigure(1, weight=4)
start_fenster.grid_rowconfigure(2, weight=1)
start_fenster.grid_rowconfigure(3, weight=1)
start_fenster.grid_rowconfigure(4, weight=4)
start_fenster.grid_rowconfigure(5, weight=1)
start_fenster.grid_rowconfigure(7, weight=4)
start_fenster.grid_rowconfigure(8, weight=1)
start_fenster.grid_rowconfigure(9, weight=4)
start_fenster.grid_rowconfigure(10, weight=1)
start_fenster.grid_rowconfigure(11, weight=1)
start_fenster.grid_rowconfigure(12, weight=4)

# Definition des grid-Rasters zur Platzierung der Widgets. Für die Spaltendefinition:
start_fenster.grid_columnconfigure(0, weight=1)
start_fenster.grid_columnconfigure(1, weight=1)
start_fenster.grid_columnconfigure(2, weight=1)
start_fenster.grid_columnconfigure(3, weight=1)
start_fenster.grid_columnconfigure(4, weight=1)
start_fenster.grid_columnconfigure(5, weight=1)

# Label-Widgets für die Gesamtüberschrift und die allgemeine Beschreibung. Jeweils das Label definieren und im Grid platzieren.
label_titel = Label(start_fenster, text='PlenarWatch', font=('calibri', 14, 'bold'))
label_titel.grid(row=0, column=1, sticky=SW)
label_hinweis0 = Label(start_fenster, text='PlenarWatch ist ein Projekt zur Analsyse und dem Vergleich von '
                                           'Plenarprotokollen der Reden von Bundestagsabgeordnete:n',
                                            font=('calibri', 11, 'italic'))
label_hinweis0.grid(row=1, column=1, columnspan=4, sticky=NW, pady=10)

# Label-Widgets für die Aufgabenüberschrift "Politiker:innen-Analyse" und die Ausfüllhinweise
label_aufg1 = Label(start_fenster, text='Eine:n Politiker:in analysieren', font=('calibri', 14, 'bold'))
label_aufg1.grid(row=2, column=1, columnspan=4, sticky=SW)
label_hinweis1 = Label(start_fenster, text='Bitte für die/den Politiker:in einen Namen suchen und aus dem'
                                           ' Listenfeld auswählen', font=('calibri', 11, 'italic'))
label_hinweis1.grid(row=3, column=1, columnspan=4, sticky=SW)

# Label-Widgets, um Daten für die Analyse einzugeben bzw. auszuwählen
label_name1 = Label(start_fenster, text='Namen suchen (Filter)', font=('calibri', 11))
label_name1.grid(row=4, column=1, sticky=SW)
label_name2 = Label(start_fenster, text='Namen auswählen', font=('calibri', 11))
label_name2.grid(row=5, column=1, sticky=W)

# Label-Widget für die Aufgabenüberschrift "Politiker:innen-Vergleich" und die Ausfüllhinweise
label_aufg2 = Label(start_fenster, text='Zwei Politiker:innen vergleichen', font=('calibri', 14, 'bold'))
label_aufg2.grid(row=7, column=1, columnspan=4, sticky=SW)
label_hinweis2 = Label(start_fenster, text='Bitte für Politiker:in A und B jeweils einen Namen suchen und '
                                           'aus dem Listenfeld auswählen', font=('calibri', 11, 'italic'))
label_hinweis2.grid(row=8, column=1, columnspan=4, sticky=SW)

# Label-Widgets für die Überschriften zu "Politiker:in A" und " Politiker:in B"
label_hinweis3 = Label(start_fenster, text='Politiker:in A', font=('calibri', 11, 'bold'))
label_hinweis3.grid(row=9, column=2, sticky=SW)
label_hinweis4 = Label(start_fenster, text='Politiker:in B', font=('calibri', 11, 'bold'))
label_hinweis4.grid(row=9, column=4, sticky=SW)

# Label- und Eingabe-Widgets, um Daten für den Politiker:in-Vergleich einzugeben
label_name3 = Label(start_fenster, text='Namen suchen (Filter)', font=('calibri', 11))
label_name3.grid(row=10, column=1, sticky=SW)
label_name4 = Label(start_fenster, text='Namen suchen (Filter)', font=('calibri', 11))
label_name4.grid(row=10, column=3, sticky=SW)

# Label- und Listbox-Widgets, um Daten für den Politiker:in-Vergleich anzuzeigen und ggf. auszuwählen
label_name5 = Label(start_fenster, text='Namen auswählen', font=('calibri', 11))
label_name5.grid(row=11, column=1, sticky=W)
label_name6 = Label(start_fenster, text='Namen auswählen', font=('calibri', 11))
label_name6.grid(row=11, column=3, sticky=W)
label_name1 = Label(start_fenster, text='Gruppe B2-1', font=('calibri', 11, 'italic'), padx=10)
label_name1.grid(row=12, column=5, sticky=SE)

eingabe_name1 = Entry(start_fenster, bg='white', font=('calibri', 11))
eingabe_name1.grid(row=4, column=2, sticky=SW)
eingabe_name3 = Entry(start_fenster, bg='white', font=('calibri', 11))
eingabe_name3.grid(row=10, column=2, sticky=SW)
eingabe_name4 = Entry(start_fenster, bg='white', font=('calibri', 11))
eingabe_name4.grid(row=10, column=4, sticky=SW)

lbox_name2 = Listbox(start_fenster, height=3, bg='white', font=('calibri', 11))
lbox_name2.grid(row=5, column=2, sticky=SW)
lbox_name5 = Listbox(start_fenster, height=3, bg='white', font=('calibri', 11))
lbox_name5.grid(row=11, column=2, sticky=SW)
lbox_name6 = Listbox(start_fenster, height=3, bg='white', font=('calibri', 11))
lbox_name6.grid(row=11, column=4, sticky=SW)

lbox_fuellen(pol_liste, lbox_name2)
lbox_name2.bind('<<ListboxSelect>>', lambda e: lbox_person_auswaehlen(eingabe_name1, lbox_name2))
eingabe_name1.bind('<KeyRelease>', lambda e: pruefe_lbox_eintraege(eingabe_name1, lbox_name2))

lbox_fuellen(pol_liste, lbox_name5)
lbox_name5.bind('<<ListboxSelect>>', lambda e: lbox_person_auswaehlen(eingabe_name3, lbox_name5))
eingabe_name3.bind('<KeyRelease>', lambda e: pruefe_lbox_eintraege(eingabe_name3, lbox_name5))

lbox_fuellen(pol_liste, lbox_name6)
lbox_name6.bind('<<ListboxSelect>>', lambda e: lbox_person_auswaehlen(eingabe_name4, lbox_name6))
eingabe_name4.bind('<KeyRelease>', lambda e: pruefe_lbox_eintraege(eingabe_name4, lbox_name6))

#Schaltfläche, die die Analyse auslöst und die Funktion "analyse_ausgeben" aufruft
schaltfl1 = Button(start_fenster, text='Analysieren', background='#D8D8D8',
                   font=('calibri', 11), command=analyse_ausgeben)
schaltfl1.grid(row=5, column=3, sticky=SW)

#Schaltfläche, die die Analyse auslöst und die Funktion "vergleich_ausgeben" aufruft
schaltfl2 = Button(start_fenster, text='Vergleichen', background='#D8D8D8',
                   font=('calibri', 11), command=vergleich_ausgeben)
schaltfl2.grid(row=11, column=5, sticky=SW)

# mainloop() aktiviert eine Ereignisschleife, die das Fenster so lange geöffnet hält, bis es geschlossen wird.
start_fenster.mainloop()


# Die Funktionen lbox_fuellen, lbox_person_auswaehlen und pruefe_lbox_eintraege sind angelehnt an:
# Basic Search and Autofill - Python Tkinter GUI Tutorial #162 (https://www.youtube.com/watch?v=0CXQ3bbBLVk)