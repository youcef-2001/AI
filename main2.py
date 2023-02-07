from barque import Barque
from etat import EtatSommet

places=2
unebarque=Barque("profondeur",places)


def recurProf(etatinit:EtatSommet,parcourProf:list[EtatSommet]) :
    #etatinit.marquer()
    if parcourProf ==None:
        parcourProf:list[EtatSommet]=list()
    
    parcourProf.append(etatinit)
    if etatinit.finale:
        return parcourProf
    voisin:list[EtatSommet]=list()
    for move in range(unebarque.rangy):
        if unebarque.possibleMove(etatinit,move):
            voisin.append(unebarque.changeDeCote(etatinit,move))
    
    for etat in voisin :
       b=True#contientpas
       for etat2 in parcourProf:
            if etat.__eq__(etat2):
                b=False   
       if b:        
            recurProf(etat,parcourProf)
    
    

etat=EtatSommet(3,3,3,0,[],True)
parc:list[EtatSommet]=[]
recurProf(etat,parc)
for etat in parc:
    if etat.finale:
        print(etat.precedents)



