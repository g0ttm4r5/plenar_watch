import numpy as np
import matplotlib.pyplot as plt

def balkendiagramm_zeichnen(datei_pfad, rede_dict):

        # original default Parameter werden wiederhergestellt:
        plt.rcdefaults()
        fig, ax = plt.subplots()

        woerter = rede_dict.keys()
        anzahl = rede_dict.values()

        y_pos = np.arange(len(rede_dict))
        ax.barh(y_pos, anzahl, align='center', color='blue', ecolor='black')

        # Beschriftungsmarker auf der y-Achse ausblenden
        plt.tick_params(axis='y',  which='both',  left=False)

        # Das Diagramm etwas nach rechts verschieben (Lesbarkeit der Wörter an der y-Achse)
        plt.subplots_adjust(left=0.25, right=0.95)

        # Ermittelt die aktuelle Achseninstanz für die aktuelle Abbildung und blendet die obere und rechte Achse aus
        ax = plt.gca()
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)

        # Wörter werden als Beschriftung von oben nach unten (invert_yaxis) eingesetzt
        ax.set_yticks(y_pos)
        ax.set_yticklabels(woerter)
        ax.invert_yaxis()

        ax.set_xlabel('Anzahl')
        ax.set_title('Die zehn am häufigsten verwendeten Wörter')
        plt.savefig(datei_pfad)
