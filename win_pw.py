# Das Modul tkinter importieren
import tkinter
from tkinter import *

from opendiscourse_page import opendiscourse as Dis

# Die Funktionen lbox_fuellen, lbox_person_auswaehlen und pruefe_lbox_eintraege sind angelehnt an:
# Basic Search and Autofill - Python Tkinter GUI Tutorial #162 (https://www.youtube.com/watch?v=0CXQ3bbBLVk)

def erstelle_liste():
    """Die Funktion erstelle_liste extrahiert aus der ..."""

    liste_p = Dis.get_list("politicians")

    daten = list()
    i = 0
    for n in liste_p['data']['politicians']:
        daten.append(liste_p['data']['politicians'][i]['firstName'] + ' ' + liste_p['data']['politicians'][i]['lastName'])
        i += 1
    return daten

def lbox_fuellen(liste, lbox):
    """Die Funktion lbox_fuellen ist dafür zuständig, die Listbox für die Politer:innen mit den entsprechenden
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


def analyse_ausgeben(name):
    """Die Funktion analyse_ausgeben ..."""
    window = Toplevel()
    # das Toplevel-Fenster erhält einen Titel, der vom aufrufenden Event übergeben wird
    window.title(name)
    # Die Größe des Fensters wird festgelegt
    window.geometry('900x250')
    #'name_auswahl' erhält den Namensstring aus dem Eingabefeld

    #name1_auswahl = eingabe_name1.get()
    name1_auswahl = lbox_name2.get(lbox_name2.curselection())

    # Ein Label wird auf dem Fenster erzeugt, ein Hinweis inklusive Name aus dem Eingabefeld wird ausgegeben
    newlabel = Label(window, text=f'Ergebnis für {name1_auswahl}', font=('calibri', 11))
    # Das Label wird auf dem Fenster platziert
    newlabel.pack()


def vergleich_ausgeben(name):
    """Die Funktion vergleich_ausgeben ..."""
    window = Toplevel()
    window.geometry('1000x400')
    newlabel = Label(window, text=name, font=('calibri', 11))
    newlabel.pack()

start_fenster = Tk()

pol_liste = erstelle_liste()

start_fenster.title('PlenarWatch')
start_fenster.geometry('900x600')

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

# Label-Widget für die Gesamtüberschrift und die allgemeine Beschreibung. Jeweils das Label definieren und im Grid platzieren.
label_titel = Label(start_fenster, text='PlenarWatch', font=('calibri', 14, 'bold'))
label_titel.grid(row=0, column=1, sticky=tkinter.SW)
label_hinweis0 = Label(start_fenster, text='Mit Hilfe von PlenarWatch können .... Beschreibung ', font=('calibri', 11, 'italic'))
label_hinweis0.grid(row=1, column=1, columnspan=4, sticky=tkinter.NW, pady=10)

# Label-Widget für die Aufgabenüberschrift "Politiker:innen-Analyse" und die Ausfüllhinweise
label_aufg1 = Label(start_fenster, text='Eine:n Politiker:in analysieren', font=('calibri', 14, 'bold'))
label_aufg1.grid(row=2, column=1, columnspan=4, sticky=tkinter.SW)
label_hinweis1 = Label(start_fenster, text='Bitte einen Namen eingeben (Vorname Nachname) oder einen Namen auswählen', font=('calibri', 11, 'italic'))
label_hinweis1.grid(row=3, column=1, columnspan=4, sticky=tkinter.SW)

# Label- und Eingabe-Widgets, um Daten für die Analyse einzugeben bzw. auszuwählen
label_name1 = Label(start_fenster, text='Namen eingeben', font=('calibri', 11))
label_name1.grid(row=4, column=1, sticky=tkinter.SW)
eingabe_name1 = Entry(start_fenster, bg='white', font=('calibri', 11))
eingabe_name1.grid(row=4, column=2, sticky=tkinter.SW)
label_name2 = Label(start_fenster, text='Namen suchen', font=('calibri', 11))
label_name2.grid(row=5, column=1, sticky=tkinter.W)
lbox_name2 = Listbox(start_fenster, height=3, bg='white', font=('calibri', 11))
lbox_name2.grid(row=5, column=2, sticky=tkinter.SW)

lbox_fuellen(pol_liste, lbox_name2)
lbox_name2.bind('<<ListboxSelect>>', lambda e: lbox_person_auswaehlen(eingabe_name1, lbox_name2))
eingabe_name1.bind('<KeyRelease>', lambda e: pruefe_lbox_eintraege(eingabe_name1, lbox_name2))

'''Schaltfläche, die die Analyse auslöst und die Funktion "analyse_ausgeben" aufruft:
lambda ist eine "Einmalfunktion", die eine Eingabe (hier die Methode mit Argumenten) entgegennimmt
und wieder zurückgibt. Über diesen "Umweg" ist es möglich, einem Ereignis eine Methode mit Argumenten
zu übergeben, das ansonsten nicht zu realisieren geht. Das "e" ist das Argument, das übergeben wird. 
Der Doppelpunkt grenzt die Argumentliste vom Rückgabewert oder Ausdruck ab. Der Teil "analyse_ausgeben(<Text>)"
 ist der Rückgabewert.'''
schaltfl1 = Button(start_fenster, text='Analysieren', background='#D8D8D8', font=('calibri', 11))
schaltfl1.grid(row=5, column=3, sticky=tkinter.SW)
schaltfl1.bind('<Button>', lambda e: analyse_ausgeben('Politiker:in analysieren'))

# Label-Widget für die Aufgabenüberschrift "Politiker:innen-Vergleich" und die Ausfüllhinweise
label_aufg2 = Label(start_fenster, text='Zwei Politiker:innen vergleichen', font=('calibri', 14, 'bold'))
label_aufg2.grid(row=7, column=1, columnspan=4, sticky=tkinter.SW)
label_hinweis2 = Label(start_fenster, text='Bitte für Politiker:in A und B jeweils einen Namen eingeben (Vorname Nachname) oder einen Namen auswählen', font=('calibri', 11, 'italic'))
label_hinweis2.grid(row=8, column=1, columnspan=4, sticky=tkinter.SW)

# Label-Widgets für die Überschriften zu "Politiker:in A" und " Politiker:in B"
label_hinweis3 = Label(start_fenster, text='Politiker:in A', font=('calibri', 11, 'bold'))
label_hinweis3.grid(row=9, column=2, sticky=tkinter.SW)
label_hinweis4 = Label(start_fenster, text='Politiker:in B', font=('calibri', 11, 'bold'))
label_hinweis4.grid(row=9, column=4, sticky=tkinter.SW)

# Label- und Eingabe-Widgets, um Daten für den Politiker:in-Vergleich einzugeben
label_name3 = Label(start_fenster, text='Namen eingeben', font=('calibri', 11))
label_name3.grid(row=10, column=1, sticky=tkinter.SW)
eingabe_name3 = Entry(start_fenster, bg='white', font=('calibri', 11))
eingabe_name3.grid(row=10, column=2, sticky=tkinter.SW)

label_name4 = Label(start_fenster, text='Namen eingeben', font=('calibri', 11))
label_name4.grid(row=10, column=3, sticky=tkinter.SW)
eingabe_name4 = Entry(start_fenster, bg='white', font=('calibri', 11))
eingabe_name4.grid(row=10, column=4, sticky=tkinter.SW)

# Label- und Listbox-Widgets, um Daten für den Politiker:in-Vergleich anzuzeigen und ggf. auszuwählen
label_name5 = Label(start_fenster, text='Namen suchen', font=('calibri', 11))
label_name5.grid(row=11, column=1, sticky=tkinter.W)
lbox_name5 = Listbox(start_fenster, height=3, bg='white', font=('calibri', 11))
lbox_name5.grid(row=11, column=2, sticky=tkinter.SW)

lbox_fuellen(pol_liste, lbox_name5)
lbox_name5.bind('<<ListboxSelect>>', lambda e: lbox_person_auswaehlen(eingabe_name3, lbox_name5))
eingabe_name3.bind('<KeyRelease>', lambda e: pruefe_lbox_eintraege(eingabe_name3, lbox_name5))

label_name6 = Label(start_fenster, text='Namen suchen', font=('calibri', 11))
label_name6.grid(row=11, column=3, sticky=tkinter.W)
lbox_name6 = Listbox(start_fenster, height=3, bg='white', font=('calibri', 11))
lbox_name6.grid(row=11, column=4, sticky=tkinter.SW)

lbox_fuellen(pol_liste, lbox_name6)
lbox_name6.bind('<<ListboxSelect>>', lambda e: lbox_person_auswaehlen(eingabe_name4, lbox_name6))
eingabe_name4.bind('<KeyRelease>', lambda e: pruefe_lbox_eintraege(eingabe_name4, lbox_name6))

#Schaltfläche, die die Analyse auslöst und die Funktion "vergleich_ausgeben" aufruft (siehe oben)
schaltfl2 = Button(start_fenster, text='Vergleichen', background='#D8D8D8', font=('calibri', 11))
schaltfl2.grid(row=11, column=5, sticky=tkinter.SW)
schaltfl2.bind('<Button>', lambda e: vergleich_ausgeben('Politiker:in vergleichen'))

label_name1 = Label(start_fenster, text='Gruppe B2-1', font=('calibri', 11, 'italic'), padx=10)
label_name1.grid(row=12, column=5, sticky=tkinter.SE)

start_fenster.mainloop()


