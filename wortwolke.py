from wordcloud import WordCloud

def wortwolke_erzeugen(datei_pfad):
    text = 'Python Kurs: mit Python programmieren lernen für Anfänger und Fortgeschrittene Dieses Python Tutorial entsteht im Rahmen von Uni-Kursen und kann hier kostenlos genutzt werden. Python ist eine für Anfänger und Einsteiger sehr gut geeignete Programmiersprache, die später auch den Fortgeschrittenen und Profis alles bietet, was man sich beim Programmieren wünscht. Der Kurs ist eine Einführung und bietet einen guten Einstieg. Es wird aktuelles Wissen vermittelt - daher schreiben wir unseren Python-Code mit der aktuellen Python-Version 3. einfach Python lernen über das Programmieren von Spielen Damit Python programmieren lernen noch mehr Spaß macht, werden wir im Kurs anhand verschiedener Spiele die Anwendung von Python kennen lernen und unser Wissen als Programmierer aufbauen. Die Grundlagen werden direkt umgesetzt in bekannte Spiele wie:'
    wortwolke = WordCloud(background_color="white").generate(text)
    wortwolke.to_file(datei_pfad)

# https://www.python-lernen.de/wordcloud-erstellen-python.htm
