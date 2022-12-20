import psycopg2 as psy
# ein Paket um auf PostgreSQL Datenbanken zugreifen zu können (siehe: https://www.psycopg.org/docs/)
# vgl: https://pynative.com/python-postgresql-tutorial/

# die Verbindung zur Datenbank aufbauen
conn = psy.connect(
    host="localhost",
    database="next",
    user="postgres",
    password="postgres",
    port="5432")
cur = None

# Abrufen von Informationen aus der Datenbank
class sql_abfragen:
    def __init__(self):
        self

    def alle_reden(self):
        try:
            conn

            cur = conn.cursor() # Erstellung einer Variable zur Übergabe von SQL Code

            # Alle Werte der Spalte "speech_content" aus der Tabelle "speeches" ausgeben
            cur.execute("SELECT speech_content FROM open_discourse.speeches;")
            for alles in cur.fetchall():
                print(alles)

        except Exception as error: # Wenn ein Fehler auftritt, wird der passende "error" ausgeworfen
            print("Fehler beim Aufbau der Datenbankverbindung (PostgreSQL): ", error)
        """finally: # Datenbankverbindung beenden
            if conn:
                cur.close()
                conn.close()
                print("Datenbankverbindung wurde beendet.")"""

    def alle_politiker(spalten):
        try:
            conn

            cur = conn.cursor()  # Erstellung einer Variable zur Übergabe von SQL Code

            # Alle Werte der ausgewählten Spalten aus der Tabelle "politicians" ausgeben
            cur.execute("select " + spalten + " from open_discourse.politicians")
            #print(cur.fetchall())
            for politiker in cur.fetchall():
                print(politiker)

        except Exception as error: # Wenn ein Fehler auftritt, wird der passende "error" ausgeworfen
            print("Fehler beim Aufbau der Datenbankverbindung (PostgreSQL): ", error)
        """finally: # Datenbankverbindung beenden
            if conn:
                cur.close()
                conn.close()
                print("Datenbankverbindung wurde beendet.")"""

    def reden_eines_pol(pol_id):
        try:
            conn

            cur = conn.cursor() # Erstellung einer Variable zur Übergabe von SQL Code

            # Alle Werte der Spalte "speech_content" aus der Tabelle "speeches" ausgeben, die zur eingegebenen ID gehören
            cur.execute("SELECT speech_content FROM open_discourse.speeches where politician_id = " + pol_id + ";")
            #print(cur.fetchall())
            for reden in cur.fetchall():
                print(reden)

        except Exception as error: # Wenn ein Fehler auftritt, wird der passende "error" ausgeworfen
            print("Fehler beim Aufbau der Datenbankverbindung (PostgreSQL): ", error)
        """finally: # Datenbankverbindung beenden
            if conn:
                cur.close()
                conn.close()
                print("Datenbankverbindung wurde beendet.")"""