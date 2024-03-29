"""
Dateiname: postgresql_import.py
Autor: Marcel Weller
"""

import psycopg2 as psy

# ein Paket um auf PostgreSQL Datenbanken zugreifen zu können (siehe: https://www.psycopg.org/docs/)
# vgl: https://pynative.com/python-postgresql-tutorial/

conn = psy.connect(
    host="localhost",
    database="next",
    user="postgres",
    password="postgres",
    port="5432")
cur = None

# Initiale Prüfung, ob die Datenbank erreichbar ist
try:
    conn

    cur = conn.cursor()  # Erstellung einer Variable zur Übergabe von SQL Code

    # Überprüfen der Verbindung zur Datenbank und Ausgabe der Datenbankinformationen
    print("Datenbank Informationen:")
    print(conn.get_dsn_parameters(), "\n")
    cur.execute("SELECT version();")

    record = cur.fetchone()
    print("Folgende Verbindung ist aufgebaut: ", record, "\n")

except Exception as error:  # Wenn keine Verbindung aufgebaut werden kann, wird "error" ausgeworfen
    print("Fehler beim Aufbau der Datenbankverbindung (PostgreSQL)", error)
finally:  # Datenbankverbindung beenden
    if conn:
        cur.close()
        conn.close()
        print("Datenbankverbindung wurde beendet.")
