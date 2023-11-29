# Votre réponse ci-dessous :

# méthode à rajouter à l'ensemble de la classe - copier coller l'écriture de la classe de la question précédente

class ArbreBinaire:
    def __init__(self, valeur):
        self.contenu = valeur
        self.filsGauche = None
        self.filsDroit = None
    
    def ajoutFilsGauche(self, valeur):
      if self.filsGauche == None:
         self.filsGauche = ArbreBinaire(valeur)  
      else :
        self.filsGauche.ajoutFilsGauche(valeur)

    def ajoutFilsDroit(self, valeur):
        if self.filsDroit == None:
          self.filsDroit = ArbreBinaire(valeur)
        else :
         self.filsDroit.ajoutFilsDroit(valeur)
    
    def ajoutContenu(self, valeur):
        if valeur > self.contenu:
          if self.filsDroit == None:
            self.ajoutFilsDroit(valeur)
          else:
            self.filsDroit.ajoutContenu(valeur)
        
        elif valeur < self.contenu:
          if self.filsGauche is None:
           self.ajoutFilsGauche(valeur)
          else:
            self.filsDroit.ajoutContenu(valeur)

    
    def __str__(self):
     return f"[Contenu : {self.contenu} | Fils droit : {self.filsDroit.__str__()} | Fils gauche : {self.filsGauche.__str__()}] / "

buisson = ArbreBinaire(10)
buisson.ajoutContenu(5)
#Che ne comprend paaaas.
#buisson.ajoutContenu(7)
print(buisson)
