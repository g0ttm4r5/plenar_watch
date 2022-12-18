import psycopg2 as psy
# ein Paket um auf PostgreSQL Datenbanken zugreifen zu können (siehe: https://www.psycopg.org/docs/)
# vgl: https://pynative.com/python-postgresql-tutorial/

conn = None
cur = None

# Initiale Prüfung, ob die Datenbank erreichbar ist
try:
    # die Verbindung zur Datenbank aufbauen
    conn = psy.connect(
        host="localhost",
        database="next",
        user="postgres",
        password="postgres",
        port="5432")

    cur = conn.cursor() # Erstellung einer Variable zur Übergabe von SQL Code

    # Überprüfen der Verbindung zur Datenbank und Ausgabe der Datenbankinformationen
    print("Datenbank Informationen:")
    print(conn.get_dsn_parameters(), "\n")
    cur.execute("SELECT version();")

    record = cur.fetchone()
    print("Folgende Verbindung ist aufgebaut: ", record, "\n")

except Exception as error: # Wenn keine Verbindung aufgebaut werden kann, wird "error" ausgeworfen
    print("Fehler beim Aufbau der Datenbankverbindung (PostgreSQL)", error)
finally: # Datenbankverbindung beenden
    if conn:
        cur.close()
        conn.close()
        print("Datenbankverbindung wurde beendet.")


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

    # Alle Werte aus der Tabelle "politicians" ausgeben
    cur.execute("SELECT * FROM open_discourse.politicians;")
    for alles in cur.fetchall():
        print(alles)


except Exception as error: # Wenn ein Fehler auftritt, wird der passende "error" ausgeworfen
    print("Fehler beim Aufbau der Datenbankverbindung (PostgreSQL): ", error)
finally: # Datenbankverbindung beenden
    if conn:
        cur.close()
        conn.close()
        print("Datenbankverbindung wurde beendet.")