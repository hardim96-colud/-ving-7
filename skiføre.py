from datetime import datetime 

filnavn= "sinnes_2014_2025.csv"

aar =int(input("Skriv inn årstall: "))

startdato = datetime(aar -1, 11, 1)
sluttdato =datetime(aar, 5, 31)

antall_skidager = 0

with open(filnavn, "r", encoding="UTF-8") as fil:
    next(fil)

    for linje in fil:
        data = linje.strip().split(";")
        if len(data) <7: 
            continue
        if not data[2].strip():
            continue
        dato = datetime.strptime(data[2], "%d.%m.%Y")
        sno = data[6]
        if dato.year == 2024 and dato.month == 2: 
            print(dato, sno)

    if sno != "-":
        snodybde = float(sno.replace(",", "."))

        if startdato <= dato <= sluttdato: 
            if snodybde >= 20:
                antall_skidager +=1 

print(f"Antall dager med skriføre: {antall_skidager}")

