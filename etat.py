

class Etat :
    

    def __init__(self,nbr :int,nbrC:int ,nbrM:int,posbarque:bool):
        self.nbr=nbr
        self.nbrC=nbrC
        self.nbrM=nbrM
        self.posBarque=posbarque 
        
        if nbrM<nbrC or nbr-nbrC<nbr-nbrM:
            self.interdit=True
        else:
            self.interdit=False
        
            self.finale=False
        if nbrC==0 and nbrM==0:
            self.finale=True
        


 
  

class EtatNerveux(Etat):
 

 def __init__(self, nbr:int ,nbrC: int, nbrM: int,prio:int ,precd:list[int],posbarque:bool)  :
    super().__init__(nbr, nbrC, nbrM,posbarque)
    self.prio=prio
    if not precd==None:
        self.precedents=precd
    else:
        self.precedents=[]

 def setPrio(self,p):
    self.prio=p

 def setPrecd(self,prec: int):
    
    self.precedents.append(prec)


