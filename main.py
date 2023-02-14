from spillebrett import Spillebrett #Importerer klassen Spillebrett

def Spill():
    rad = int(input("Oppgi hoeyde paa brettet: ")) #Brukerangitte verdier på rad og kolonne
    kolonne = int(input("Oppgi bredde paa brettet: "))
    brett = Spillebrett(rad, kolonne) #Opretter objekt med brukerangitt tall paa rad og kolonne
    brett.tegnBrett() #Tegner brettet til den nulte generasjonen
    print("Generasjon: " + str(brett.finnGenerasjon()) + " --- Antall levende celler: " + str(brett.finnAntallLevende())) #Skriver ut antall levende celler

    valg = input("Trykk Enter for aa fortsette, eller q og saa Enter for aa avslutte: ")

    while valg != "q": #Slutter dersom brukeren taster inn "q", fortsetter ellers
        if valg == "": #Hvis brukeren trykker bare på enter gjør programmet følgende:
            print() #Pause mellom generasjonene
            brett.oppdatering() #Oppdaterer brettet
            brett.tegnBrett() #Tegner det oppdaterte brettet
            print("Generasjon: " + str(brett.finnGenerasjon()) + " --- Antall levende celler: " + str(brett.finnAntallLevende()))
            valg = input("Trykk Enter for aa fortsette, eller q og saa Enter for aa avslutte: ")

Spill() #Kaller på prosedyren Spill
