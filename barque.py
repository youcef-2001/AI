 
class barque:


    def __init__( self , nom , places , *arg):

      print("I AM A NEW BARQUE !!")
      self.nom=nom
      self.places=places
      for ele in arg :
          if( ele =="C"):
            self.contenu=self.contenu+"C"
          if( ele=="M"):
            self.contenu=self.contenu+"M"  
     


    def toString(self):
        return "Je suis une Barque  mon Nom :"+self.nom+"\n"+"Mes places :"+str(self.places)+"\n "+self.contenu
