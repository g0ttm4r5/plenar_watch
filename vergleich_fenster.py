"""
Dateiname: vergleich_fenster
Authorin: Angelika Martin
"""

from tkinter import *
from tkinter import ttk
from analyse import haeufigkeit_woerter, summe_aller_woerter, durchschnitt_laenge

def vergleichsfenster_anzeigen(name1, name2, id1, id2, anzahl_reden1, anzahl_reden2, anzahl_analysierte_reden1,
                               anzahl_analysierte_reden2):
    """Diese Funktion erstellt ein Fenster mit einem vertikalen Scrollbalken, auf dem die Ergebnisse der
    Politikeranalyse dargestellt werden"""

    # Fenstergerüst (TKinter) erstellen
    window = Toplevel()
    window.title("Analyse")
    window.geometry('1400x800')

    # Oberfläche generieren
    basisflaeche = Frame(window)
    # ganze Fläche mit dem Frame ausfüllen
    basisflaeche.pack(fill=BOTH, expand=1)

    # Zeichenfläche generieren
    zeichenflaeche = Canvas(basisflaeche)
    zeichenflaeche.pack(side=LEFT, fill=BOTH, expand=1)

    # Scrollbar zur Zeichenfläche hinzufügen
    scrollbalken = ttk.Scrollbar(basisflaeche, orient=VERTICAL, command=zeichenflaeche.yview)
    scrollbalken.pack(side=RIGHT, fill=Y)

    # Zeichenfläche konfigurieren
    zeichenflaeche.configure(yscrollcommand=scrollbalken.set)
    zeichenflaeche.bind('<Configure>', lambda e: zeichenflaeche.configure(scrollregion=zeichenflaeche.bbox('all')))

    # einen Rahmen in die bestehende Zeichenfläche einfügen
    zusatzflaeche = Frame(zeichenflaeche)

    # den Rahmen in ein Fenster in der Zeichenfläche integrieren (oben rechts, d. h. 0,0)
    zeichenflaeche.create_window((0, 0), window=zusatzflaeche, anchor='nw')
    zeichenflaeche.grid_rowconfigure(0, weight=1)
    zeichenflaeche.grid_columnconfigure(0, weight=1)

    # Zwei Label für die Ergebnisse werden erzeugt und auf dem Fenster platziert
    infolabel1 = Label(zusatzflaeche, text=f'Analyse für {name1}', font=('calibri', 24))
    infolabel2 = Label(zusatzflaeche, text=f'Analyse für {name2}', font=('calibri', 24))
    infolabel1.grid(row=1, column=0, ipady=20)
    infolabel2.grid(row=1, column=1, ipady=20)

    # Zwei Label für ein Foto des/der Politiker:in wird erzeugt und auf dem Fenster platziert
    p1_image = PhotoImage(file="tmp_images/avatar.png")
    p2_image = PhotoImage(file="tmp_images/avatar.png")
    p1_label = Label(master=zusatzflaeche, image=p1_image)
    p2_label = Label(master=zusatzflaeche, image=p2_image)
    p1_label.grid(row=2, column=0, ipady=10, ipadx=100)
    p2_label.grid(row=2, column=1, ipady=10, ipadx=100)

    # Zwei Label für die Ergebnisse werden erzeugt und auf dem Fenster platziert
    infolabel3 = Label(zusatzflaeche, text=f'Von {name1} wurden {anzahl_reden1} Reden \nvon OpenDiscourse '
                                           f'heruntergeladen.\n\n{durchschnitt_laenge(id1)}\n\nDie folgenden '
                                           f'Ergebnisse beziehen sich auf die \nletzten {anzahl_analysierte_reden1} '
                                           f'analysierten Reden:', font=('calibri', 20))
    infolabel4 = Label(zusatzflaeche, text=f'Von {name2} wurden {anzahl_reden2} Reden \nvon OpenDiscourse '
                                           f'heruntergeladen.\n\n{durchschnitt_laenge(id2)}\n\nDie folgenden '
                                           f'Ergebnisse beziehen sich auf die \nletzten {anzahl_analysierte_reden2} '
                                           f'analysierten Reden:', font=('calibri', 20))
    infolabel3.grid(row=3, column=0, ipady=20)
    infolabel4.grid(row=3, column=1, ipady=20)

    # Zwei Bilddateien werden erzeugt, auf dem Label ausgegeben und das Label platziert
    wc_image1 = PhotoImage(file="tmp_images/analyseimage1.png")
    wc_image2 = PhotoImage(file="tmp_images/analyseimage2.png")
    wc_label1 = Label(master=zusatzflaeche, image=wc_image1)
    wc_label2 = Label(master=zusatzflaeche, image=wc_image2)
    wc_label1.grid(row=4, column=0, ipady=20, ipadx=20)
    wc_label2.grid(row=4, column=1, ipady=20, ipadx=20)

    # Zwei zusätzliche Label für die Ergebnisse werden erzeugt, auf dem Label ausgegeben und das Label platziert
    infolabel5 = Label(zusatzflaeche, text=f'{summe_aller_woerter(id1)}\n\n{haeufigkeit_woerter(id1, 5)}',
                                            font=('calibri', 20))
    infolabel5.grid(row=5, column=0, ipady=10)

    infolabel6 = Label(zusatzflaeche, text=f'{summe_aller_woerter(id2)}\n\n{haeufigkeit_woerter(id2, 5)}',
                                            font=('calibri', 20))
    infolabel6.grid(row=5, column=1, ipady=10)


    # Zwei Bilddateien (Balkendiagramm) werden erzeugt, auf dem Label ausgegeben und das Label platziert
    bd_image1 = PhotoImage(file="tmp_images/balkendiagramm1.png")
    bd_image2 = PhotoImage(file="tmp_images/balkendiagramm2.png")
    balkendiagrammlabel1 = Label(master=zusatzflaeche, image=bd_image1)
    balkendiagrammlabel2 = Label(master=zusatzflaeche, image=bd_image2)
    balkendiagrammlabel1.grid(row=7, column=0, ipady=10, ipadx=20)
    balkendiagrammlabel2.grid(row=7, column=1, ipady=10, ipadx=20)

    # mainloop() aktiviert eine Ereignisschleife, die das Fenster so lange geöffnet hält, bis es geschlossen wird.
    window.mainloop()


# Quelle für den Scrollbalken: https://www.youtube.com/watch?v=0WafQCaok6g