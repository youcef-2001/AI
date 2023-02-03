from etat import EtatNerveux

class Move:
    nbrMoves=0
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
        
        if(etat.posBarque):#aller
            etatn= EtatNerveux(etat.nbr,etat.nbrC-self.liste[move].cannibales,etat.nbrM-self.liste[move].missionnaires,etat.prio+10,etat.precedents,False)
            etatn.setPrecd(move)
            return etatn

          
        else:#retour
            etatn= EtatNerveux(etat.nbr,etat.nbrC+self.liste[move].cannibales,etat.nbrM+self.liste[move].missionnaires,etat.prio+10,etat.precedents,True)
            etatn.setPrecd(move)
            return etatn
    def riveSafe(self,nbrM,nbrC):
        if nbrM==0:#Rive1
            return(nbrC>=0)
        else:
            return(nbrM>=nbrC)and(nbrC>=0)and(nbrM>0)

    def possibleMove(self,etat:EtatNerveux,move:int) -> bool:
            nbrCRes=etat.nbrC-self.liste[move].cannibales
            nbrMRes=etat.nbrM-self.liste[move].missionnaires
            if(etat.posBarque):#aller
                nbrCRes=etat.nbrC-self.liste[move].cannibales
                nbrMRes=etat.nbrM-self.liste[move].missionnaires
                return self.riveSafe(nbrMRes,nbrCRes) and self.riveSafe(etat.nbr-nbrMRes,etat.nbr-nbrCRes)
               
            else:#retour
                nbrCRes=etat.nbrC+self.liste[move].cannibales
                nbrMRes=etat.nbrM+self.liste[move].missionnaires
                return self.riveSafe(nbrMRes,nbrCRes) and self.riveSafe(etat.nbr-nbrMRes,etat.nbr-nbrCRes)
               


