"""
Dateiname: wortwolke.py
Authorin: Angelika Martin
"""

from wordcloud import WordCloud

def wortwolke_erzeugen(datei_pfad, text):
    """Diese Funktion erstellt eine Wortwolke aus den 100 häufigsten Wörtern einer Politikerin oder eines
    Politikers und speichert sie als Datei ab."""

    # Wenn kein Text für die Politiker:innen gespeichert ist, wird ein 'Dummybild' gespeichert
    if not text:
        wortwolke = WordCloud(background_color="white", width=650, height=300, max_words=100).generate('keine Daten')
        wortwolke.to_file(datei_pfad)
    # ansonsten wird eine Wortwolke erzeugt und als Bild abgespeichert
    else:
        wortwolke = WordCloud(background_color="white", width=650, height=300, max_words=100).generate(text)
        wortwolke.to_file(datei_pfad)

# Quelle: https://www.python-lernen.de/wordcloud-erstellen-python.htm
