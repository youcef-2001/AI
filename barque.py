from etat import EtatNerveux

class Move:
    nbrMoves=1
    def __init__(self,m,c):
        self.missionnaires=m
        self.cannibales=c
        self.nbr=Move.nbrMoves
        Move.nbrMoves+=1
    def describe(self):
        print(" Move number"+str(self.nbr)+"\n Missionnaire : "
        +str(self.missionnaires)
        +"\n"+" Cannibales   : "+str(self.cannibales))

       





class Barque:


    def __init__( self , nom , places):

      print("I AM A NEW BARQUE !!")
      self.nom=nom
      self.places=places
      self.pos=False
      self.liste=self.possibilities()
      
     


    def toString(self):
        return "Je suis une Barque  mon Nom :"+self.nom+"\n"+"Mes places :"+str(self.places)+"\n "

    def possibilities(self)->list[Move]:
        liste:list[Move]=[]
        i=0
        
        while(i<=self.places):
            j=0
            while(j<=self.places-i) :
                    if(i==0 and j==0):
                        pass
                    else:
                        lis=Move(j,i)
                        liste.append(lis)             
                    j+=1
            i+=1

        
        return liste
    
    
    def changeDeCote(self,etat:EtatNerveux,move:int):
        self.pos=not self.pos
        if(self.pos):
           
            etatn= EtatNerveux(etat.nbrC-self.liste[move].cannibales,etat.nbrM-self.liste[move].missionnaires,etat.precedents)
            etatn.setPrecd("C"+str(etat.nbrC)+"M"+str(etat.nbrM))
          
        else:
            etatn= EtatNerveux(etat.nbrC+self.liste[move].cannibales,etat.nbrM+self.liste[move].missionnaires,etat.precedents)




        