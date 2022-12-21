from wordcloud import WordCloud

def wortwolke_erzeugen(datei_pfad, text):

    wortwolke = WordCloud(background_color="white", width=800, height=450, max_words=100).generate(text)
    wortwolke.to_file(datei_pfad)

# https://www.python-lernen.de/wordcloud-erstellen-python.htm
