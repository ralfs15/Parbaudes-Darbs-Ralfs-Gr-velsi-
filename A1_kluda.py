# ----------------------------------------------------------------------
# A1. Python — WARNING rindu skaits
# ----------------------------------------------------------------------

# Jāsaskaita, cik žurnālā ir WARNING rindu. Izvadās nulle, lai gan tādas rindas failā ir. Atrodi un salabo kļūdu.
#
# Atrodi un salabo. Tad palaid.
# ----------------------------------------------------------------------                                                                                                Rezultātu izvadi ar tekstu "Atrasts:" pirms skaitļa.

skaits = 0

with open("sistema.log", encoding="utf-8") as f:
    for rinda in f:
        dalas = rinda.split()
        # Pārliecināmies, ka rindā ir pietiekami daudz vārdu un 4. indekss ir tieši "WARNING"
        if len(dalas) > 3 and dalas[3] == "WARNING":
            skaits += 1

print(f"Atrasts: {skaits}")


