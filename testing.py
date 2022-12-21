from postgresql_import import sql_abfragen as abfr

# Nutzung der definierten Funktionen
print(abfr.alle_politiker("id,first_name, last_name"))
print("")
print(abfr.reden_eines_pol("11005308"))