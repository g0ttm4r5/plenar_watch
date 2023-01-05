from postgresql_import import sql_abfragen as abfr

# Nutzung der definierten Funktionen
print(abfr.alle_politiker("id,first_name, last_name"))
print("")
print(abfr.reden_eines_pol("11005308"))
#print(abfr.alle_reden("self")) ACHTUNG: Diese Funktion ist sehr langsam und sollte nur bei kleineren Datenmengen verwendet werden!
#print(type(abfr.alle_reden("self")))