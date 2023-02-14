from random import randint #Brukes i metoden generer
from celle import Celle #Importerer klassen Celle så vi kan bruke metodene i den

class Spillebrett: #Klasse som lager spillebrettet

    def __init__(self, rader, kolonner):
        self._rader = rader
        self._kolonner = kolonner
        self._rutenett = [] #Oppretter rutenettet
        self._generasjon = 0 #Teller antall generasjoner

        for i in range(self._rader):
            self.celle_liste = []
            for j in range(self._kolonner):
                self.celle_liste.append(Celle()) #Lister av celler fylles inn med døde celler
            self._rutenett.append(self.celle_liste) #Fyller rutenettet inn med lister av celler

        self.generer() #Kaller på generer for å starte med et brett med tilfeldige mengder av døde og levende celler


    def tegnBrett(self): #Metode som tegner brettet på terminalen
        for i in self._rutenett:
            for j in i:
                j.erLevende() #Sjekker om cellen er levende
                print(j.hentStatusTegn(), end="") #Skriver ut cellene
            print() #Hopper over til neste rad


    def oppdatering(self): #Metode som endrer status på cellene avhengig av nabocellene
        levende_til_doed =  []
        doed_til_levende = []

        for i in range(self._rader):
            for j in range(self._kolonner):
                naboliste = self.finnNabo(j, i) #Kaller på en metode og lager en liste av nabocellene
                levendeceller = 0 #Antall levende celler

                for nabo in naboliste:
                    if nabo.erLevende():
                        levendeceller += 1 #Øker antall levende celler for hver levende celle

                if self._rutenett[i][j].erLevende():
                    if levendeceller == 2: #Hvis to eller tre av nabocellene er levende, forblir cellen levende.
                        self._rutenett[i][j].erLevende()
                    elif levendeceller == 3:
                        self._rutenett[i][j].erLevende()
                    else:
                        levende_til_doed.append(self._rutenett[i][j]) #Hvis det er færre eller flere levende naboceller enn 2 eller 3, dør cellen

                else: #Hvis cellen er død:
                    if levendeceller == 3: #Hvis tre av nabocellene er levende, blir cellen levende.
                        doed_til_levende.append(self._rutenett[i][j]) #Blir levende
                    else: #Hvis cellen har flere eller færre enn 3 levende celler forblir den død.
                        self._rutenett[i][j].erLevende()

        for element in levende_til_doed:
            element.settDoed()

        for element in doed_til_levende:
            element.settLevende()


        self._generasjon += 1

    def finnGenerasjon(self): #Metode som henter antall generasjon
        return self._generasjon

    def finnAntallLevende(self): #Metode som regner ut hvor mange levende celler det finnes på brettet
        antallLevende_list = [] #Liste av levende celler på brettet
        for i in self._rutenett:
            for j in i:
                if j.hentStatusTegn() == "O":
                    antallLevende_list.append(j) #Listen fylles inn med levende celler
        return len(antallLevende_list) #Returnerer antall levende celler på brettet

    def generer(self):
        for i in range(self._rader):
            for j in range(self._kolonner):
                rand = randint(0, 3)
                if rand == 3:
                    self._rutenett[i][j].settLevende()

    def finnNabo(self, x, y):
        naboliste = []
        for i in range(-1, 2):
            for j in range(-1, 2):
                naboX = x + i
                naboY = y + j
                if (naboX == x and naboY == y) != True:
                    if (naboX < 0 or naboY < 0 or naboX > self._kolonner-1 or naboY > self._rader-1) != True:
                        naboliste.append(self._rutenett[naboY][naboX])
        return naboliste
