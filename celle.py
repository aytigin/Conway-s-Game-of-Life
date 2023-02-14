class Celle: #Klasse som oppretter celle

    def __init__(self):
        self._celle = False #Død celle

    def settDoed(self):
        self._celle = False #Gir cellen status "død"/False

    def settLevende(self):
        self._celle = True #Gir cellen status "levende"/True

    def erLevende(self): #Sjekker om cellen er levende eller død
        if self._celle == True: #Returnerer True dersom cellen er levende
            return True
        else: #Returnerer False dersom cellen er doed
            return False

    def hentStatusTegn(self): #Returnerer 0 eller . avhengig av cellens livsstatus
        if self.erLevende():
            return "O"
        else:
            return "."
