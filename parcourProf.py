


from barque import Barque
from etat import EtatSommet


class sommet:
    def __init__(self,val:EtatSommet) -> None:
        self.val=val
        self.voisin :list[sommet]=[]
    def __eq__(self, __o:cl) -> bool:
        return self.val.__eq__(__o.val)
       
    def parcours_prof(self,  vus = None)->set():
    # Parcours en profondeur à partir du sommet s
    #    --> vus contient l'ensemble des sommets visités
    
        if vus is None:
            vus = set()
        if not s in vus:
            vus.add(s)
        for v in self.voisin:
                v.parcours_prof( vus)
        return vus



class graph:
    def __init__(self) :
        self.sommets:list[sommet]=[]
        self.arc=[]
    def adds(self,e):
        self.sommets.append(e)



graphy=graph()

barque=Barque("Graphuiste",2)
for i in range(4):
    for j in range(4):
        graphy.sommets.append(sommet(EtatSommet(3,i,j,0,[],True)))
        graphy.sommets.append(sommet(EtatSommet(3,i,j,0,[],False)))
for s in graphy.sommets:#voisin pour chaque sommet
    for vp in graphy.sommets:
        for move in barque.liste:
            if barque.changeDeCote(s,move).__eq__(vp):
                s.voisin.append(vp)


vus=graphy.sommets[0].parcours_prof(None)

for v in vus :
    print(v.val.nbrC)

