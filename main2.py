from barque import Barque
from etat import EtatNerveux
from parcourProf import graph,sommet

places=2
unebarque=Barque("profondeur",places)
nbr=3
mongraph=graph()

for i in range(nbr+1):
    for j in range(nbr+1):
        st=sommet(EtatNerveux(nbr,i,j,0,[],True))
        
        mongraph.adds(st)
        sf=sommet(EtatNerveux(nbr,i,j,0,[],False))
        mongraph.adds(sf)

