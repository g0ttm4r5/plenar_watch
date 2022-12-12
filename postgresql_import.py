import psycopg2 as psy

conn = None
cur = None
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
    print("Server Informationen:")
    print(conn.get_dsn_parameters(), "\n")
    cur.execute("SELECT version();")
    record = cur.fetchone()
    print("Folgende Verbindung ist aufgebaut: ", record, "\n")

    # cur.execute('select politicians from open_discourse;')


except Exception as error: # Wenn keine Verbindung aufgebaut werden kann, wird "error" ausgeworfen
    print("Fehler beim Aufbau der Datenbankverbindung (PostgreSQL)", error)
finally: # Datenbankverbindung beenden
    if conn:
        cur.close()
        conn.close()
        print("Datenbankverbindung wurde beendet.")