


import etat
class etat :
    nbrCann=3
    nbrMiss=3

    def __init__(self,parent : etat ,nbrC:int ,nbrM:int,finale :bool):
        self.parent=parent
        self.nbrC=nbrC
        self.nbrM=nbrM
        self.finale=finale

 
    @classmethod
    def initialiseCannMiss(cls,n: int):
        cls.nbrMiss=n
        cls.nbrCann=n

