
from listeprio import ListePrio
from etat import EtatNerveux

class ListePrio :
    

    def __init__(self,liste:list[EtatNerveux],size=0):
        self.liste=liste
        self.size=size
      
       


    def sortListePrio(self):
        self.liste.sort(key=lambda a:a.prio)
    def remove(self):
        if(self.size>0):
         self.liste.pop(0)
         self.size=self.size-1
        

    



        