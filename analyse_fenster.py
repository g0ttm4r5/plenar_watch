from tkinter import *
from tkinter import ttk

def analysefenster_anzeigen(name, id):
    """Diese Funktion erstellt ein Fenster mit einem vertikalen Scrollbalken, auf dem die Ergebnisse der
    Politikeranalyse dargestellt werden"""

    window = Toplevel()
    window.title("Analyse")
    window.geometry('1000x900')

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
    zeichenflaeche.create_window((0, 0), window=zusatzflaeche, anchor='center')
    zeichenflaeche.grid_rowconfigure(0, weight=1)
    zeichenflaeche.grid_columnconfigure(0, weight=1)

    # Ein Label für die Ergebnisse wird erzeugt und auf dem Fenster platziert
    infolabel = Label(zusatzflaeche, text=f'Analyse für {name}', font=('calibri', 32))
    infolabel.grid(row=1, column=0, columnspan=3, ipady=20, ipadx=100)

    # Ein Label für ein Foto des/der Politiker:in wird erzeugt und auf dem Fenster platziert
    p_image = PhotoImage(file="tmp_images/avatar.png")
    wc_label = Label(master=zusatzflaeche, image=p_image)
    wc_label.grid(row=2, column=0, ipady=20, ipadx=100)

    # Eine Bilddatei wird erzeugt, auf dem Label ausgegeben und das Label platziert
    wc_image = PhotoImage(file="tmp_images/analyseimage.png")
    wc_label = Label(master=zusatzflaeche, image=wc_image)
    wc_label.grid(row=4, column=0, ipady=20, ipadx=100)

    # Eine Bilddatei (Balkendiagramm) wird erzeugt, auf dem Label ausgegeben und das Label platziert
    bd_image = PhotoImage(file="tmp_images/balkendiagramm.png")
    balkendiagrammlabel = Label(master=zusatzflaeche, image=bd_image)
    balkendiagrammlabel.grid(row=5, column=0, ipady=20, ipadx=100)

    window.mainloop()

# https://www.youtube.com/watch?v=0WafQCaok6g