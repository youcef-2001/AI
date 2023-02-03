

from etat import EtatNerveux

class ListePrio :
    

    def __init__(self,liste:list[EtatNerveux],size=0):
        self.liste=liste
        self.size=size
      
       


    def sortListePrio(self):
        self.liste.sort(key=lambda a:a.prio)
    def remove(self)->EtatNerveux:
        if(self.size>0):
         e:EtatNerveux=self.liste.pop(0)
         self.size=self.size-1
         return e


    def add(self,etat:EtatNerveux):
        self.liste.append(etat)
        self.size+=1
        self.sortListePrio()
        

    
#test=ListePrio([EtatNerveux(3,3,3,0,[])],1)
#test.add(EtatNerveux(3,2,2,1,[1]))
#print(test.remove().nbrC)
#print(test.remove().nbrC)

        