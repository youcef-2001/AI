

class Etat :
    nbrCann=3
    nbrMiss=3

    def __init__(self,nbrC:int ,nbrM:int):
       
        self.nbrC=nbrC
        self.nbrM=nbrM
        if nbrC==0 and nbrM==0:
            self.finale=True
        else:
            self.finale=False


 
    @classmethod
    def initialiseCannMiss(cls,n: int):
        cls.nbrMiss=n
        cls.nbrCann=n

class EtatNerveux(Etat):
 

 def __init__(self, nbrC: int, nbrM: int,prio:int ,*precd):
    super().__init__( nbrC, nbrM)
    self.prio=prio
    self.precedents=precd

def setPrio(self,p):
    self.prio=p

def setPrecd(self,prec: str):
    self.precedents=+prec


