from barque import Barque
from etat import EtatSommet

places=10
nbrT=50
nbrc=0
nbrm=0
pos=False
unebarque=Barque("profondeur",places)


def recurProf(etatinit:EtatSommet,parcourProf:list[EtatSommet]) :
    
    if parcourProf ==None:
        parcourProf:list[EtatSommet]=list()
    
    parcourProf.append(etatinit)    
    voisin:list[EtatSommet]=list()
    for move in range(unebarque.rangy):
        if unebarque.possibleMove(etatinit,move):
           
            voisin.append(unebarque.changeDeCote(etatinit,move))
    
    for etat in voisin :
       b=True#contientpas
       c=10
       index=0
       for etat2 in parcourProf:
            if etat.__eq__(etat2):
                b=False
                c=etat.dijkstraBest(etat2)
                index=parcourProf.index(etat2)
       if b:        
            recurProf(etat,parcourProf)
       else:
        if(c<0):
            parcourProf.pop(index)
            recurProf(etat,parcourProf)
    
    

etat=EtatSommet(nbrT,nbrc,nbrm,0,[],pos)

parc:list[EtatSommet]=[]
recurProf(etat,parc)
for etat in parc:
    if etat.nbrC==nbrT and etat.nbrM==nbrT :
        print("initiale"+str(etat.precedents))
    if etat.finale :
        print("finale "+str(etat.precedents))



