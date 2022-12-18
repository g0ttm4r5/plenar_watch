import psycopg2 as psy
# ein Paket um auf PostgreSQL Datenbanken zugreifen zu können (siehe: https://www.psycopg.org/docs/)
# vgl: https://pynative.com/python-postgresql-tutorial/

conn = None
cur = None

# Abrufen von Informationen aus der Datenbank
try:
    # die Verbindung zur Datenbank aufbauen
    conn = psy.connect(
        host="localhost",
        database="next",
        user="postgres",
        password="postgres",
        port="5432")

    cur = conn.cursor() # Erstellung einer Variable zur Übergabe von SQL Code

    # Alle Werte der Spalte "speech_content" aus der Tabelle "speeches" ausgeben
    cur.execute("SELECT speech_content FROM open_discourse.speeches;")
    for alles in cur.fetchall():
        print(alles)

except Exception as error: # Wenn ein Fehler auftritt, wird der passende "error" ausgeworfen
    print("Fehler beim Aufbau der Datenbankverbindung (PostgreSQL): ", error)
finally: # Datenbankverbindung beenden
    if conn:
        cur.close()
        conn.close()
        print("Datenbankverbindung wurde beendet.")