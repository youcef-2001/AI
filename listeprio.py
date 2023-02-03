

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
         self.sortListePrio()
         return e


    def add(self,etat:EtatNerveux):
        self.liste.append(etat)
        self.size+=1
        self.sortListePrio()
        

    


        