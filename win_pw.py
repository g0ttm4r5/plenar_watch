# Das Modul tkinter importieren
import tkinter
from tkinter import *

def analyse_ausgeben(name):
    window = Toplevel()
    window.geometry('750x250')
    newlabel = Label(window, text=name, font=('calibri', 11))
    newlabel.pack()

def vergleich_ausgeben(name):
    window = Toplevel()
    window.geometry('750x250')
    newlabel = Label(window, text=name, font=('calibri', 11))
    newlabel.pack()

start_fenster = Tk()
start_fenster.title('PlenarWatch')
start_fenster.geometry('1000x500')

# Definition des grid-Rasters zur Platzierung der Widgets
start_fenster.grid_rowconfigure(0, weight=8)
start_fenster.grid_rowconfigure(2, weight=1)
start_fenster.grid_rowconfigure(3, weight=1)
start_fenster.grid_rowconfigure(4, weight=6)
start_fenster.grid_rowconfigure(5, weight=1)
start_fenster.grid_rowconfigure(7, weight=8)
start_fenster.grid_rowconfigure(8, weight=1)
start_fenster.grid_rowconfigure(9, weight=6)
start_fenster.grid_rowconfigure(10, weight=1)
start_fenster.grid_rowconfigure(11, weight=1)
start_fenster.grid_rowconfigure(12, weight=8)
start_fenster.grid_rowconfigure(14, weight=1)

start_fenster.grid_columnconfigure(0, weight=1)
start_fenster.grid_columnconfigure(1, weight=1)
start_fenster.grid_columnconfigure(2, weight=1)
start_fenster.grid_columnconfigure(3, weight=1)
start_fenster.grid_columnconfigure(4, weight=1)
start_fenster.grid_columnconfigure(5, weight=1)


label_hinweis1 = Label(start_fenster, text='Mit Hilfe von PlenarWatch können .... Beschreibung ', font=('calibri', 11, 'italic'))
label_hinweis1.grid(row=0, column=1, columnspan=4, sticky=tkinter.NW, pady=10)
# Label-Widget für die Überschrift und den Ausfüllhinweis
label_aufg1 = Label(start_fenster, text='Eine:n Politiker:in analysieren', font=('calibri', 14, 'bold'))
label_aufg1.grid(row=2, column=1, sticky=tkinter.SW)
label_hinweis1 = Label(start_fenster, text='Bitte einen Namen eingeben (Nachname, Vorname) oder einen Namen auswählen', font=('calibri', 11, 'italic'))
label_hinweis1.grid(row=3, column=1, columnspan=3, sticky=tkinter.SW)

# Label- und Eingabe-Widgets, um Daten für die Analyse einzugeben bzw. auszuwählen
label_name1 = Label(start_fenster, text='Namen eingeben', font=('calibri', 11))
label_name1.grid(row=4, column=1, sticky=tkinter.SW)
eingabe_name1 = Entry(start_fenster, bg='white', font=('calibri', 11))
eingabe_name1.grid(row=4, column=2, sticky=tkinter.SW)

label_name2 = Label(start_fenster, text='Namen suchen', font=('calibri', 11))
label_name2.grid(row=5, column=1, sticky=tkinter.SW)
eingabe_name2 = Entry(start_fenster, bg='white', font=('calibri', 11))
eingabe_name2.grid(row=5, column=2, sticky=tkinter.SW)

'''Schaltfläche, die die Analyse auslöst und die Funktion "analyse_ausgeben" aufruft:
lambda ist eine "Einmalfunktion", die eine Eingabe (hier die Methode mit Argumenten) entgegennimmt
und wieder zurückgibt. Über diesen "Umweg" ist es möglich, einem Ereignis eine Methode mit Argumenten
zu übergeben, das ansonsten nicht zu realisieren geht. Das "e" ist das Argument, das übergeben wird. 
Der Doppelpunkt grenzt die Argumentliste vom Rückgabewert oder Ausdruck ab. Der Teil "analyse_ausgeben()"
 ist der Rückgabewert.'''
schaltfl1 = Button(start_fenster, text='Analysieren', background='#D8D8D8', font=('calibri', 11))
schaltfl1.grid(row=5, column=3, sticky=tkinter.SW)
schaltfl1.bind('<Button>', lambda e: analyse_ausgeben('Politiker:in analysieren'))

# Label-Widget für die Überschrift
label_aufg2 = Label(start_fenster, text='Zwei Politiker:innen vergleichen', font=('calibri', 14, 'bold'))
label_aufg2.grid(row=7, column=1, sticky=tkinter.SW)
label_hinweis2 = Label(start_fenster, text='Bitte für Politiker:in A und B jeweils einen Namen eingeben (Nachname, Vorname) oder einen Namen auswählen', font=('calibri', 11, 'italic'))
label_hinweis2.grid(row=8, column=1, columnspan=3, sticky=tkinter.SW)

# Label- und Eingabe-Widgets, um Daten für den Vergleich einzugeben bzw. auszuwählen
label_hinweis3 = Label(start_fenster, text='Politiker:in A', font=('calibri', 11, 'bold'))
label_hinweis3.grid(row=9, column=2, sticky=tkinter.SW)
label_name3 = Label(start_fenster, text='Namen eingeben', font=('calibri', 11))
label_name3.grid(row=10, column=1, sticky=tkinter.SW)
eingabe_name3 = Entry(start_fenster, bg='white', font=('calibri', 11))
eingabe_name3.grid(row=10, column=2, sticky=tkinter.SW)

label_hinweis4 = Label(start_fenster, text='Politiker:in B', font=('calibri', 11, 'bold'))
label_hinweis4.grid(row=9, column=4, sticky=tkinter.SW)
label_name4 = Label(start_fenster, text='Namen suchen', font=('calibri', 11))
label_name4.grid(row=11, column=1, sticky=tkinter.SW)
eingabe_name4 = Entry(start_fenster, bg='white', font=('calibri', 11))
eingabe_name4.grid(row=11, column=2, sticky=tkinter.SW)

label_name5 = Label(start_fenster, text='Namen eingeben', font=('calibri', 11))
label_name5.grid(row=10, column=3, sticky=tkinter.SW)
eingabe_name5 = Entry(start_fenster, bg='white', font=('calibri', 11))
eingabe_name5.grid(row=10, column=4, sticky=tkinter.SW)

label_name6 = Label(start_fenster, text='Namen suchen', font=('calibri', 11))
label_name6.grid(row=11, column=3, sticky=tkinter.SW)
eingabe_name6 = Entry(start_fenster, bg='white', font=('calibri', 11))
eingabe_name6.grid(row=11, column=4, sticky=tkinter.SW)

#Schaltfläche, die die Analyse auslöst und die Funktion "vergleich_ausgeben" aufruft (siehe oben)
schaltfl2 = Button(start_fenster, text='Vergleichen', background='#D8D8D8', font=('calibri', 11))
schaltfl2.grid(row=11, column=5, sticky=tkinter.SW)
schaltfl2.bind('<Button>', lambda e: vergleich_ausgeben('Politiker:in vergleichen'))

label_name1 = Label(start_fenster, text='Gruppe B2-1', font=('calibri', 11, 'italic'), padx=10)
label_name1.grid(row=12, column=5, sticky=tkinter.SE)

start_fenster.mainloop()


