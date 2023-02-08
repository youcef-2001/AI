
from barque import Barque
from etat import EtatSommet
import sys
import os

places=2
nbrT=3
pos=True
if sys.argv:
    if "-nbr" in sys.argv:
        nb=sys.argv.index("-nbr") 
        nbrT=int(sys.argv.pop(nb+1))
       
    if "-places" in sys.argv:
        nb=sys.argv.index("-places") 
        places=int(sys.argv.pop(nb+1))
       
    



    


unebarque=Barque(places)
def refresh(dess:list()):
    if os.name == 'posix': 
        os.system("clear")
    else:
        os.system("cls")
    for aff in dess:
        aff()

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
    

etat=EtatSommet(nbrT,nbrT,nbrT,0,[],pos)

parc:list[EtatSommet]=[]
recurProf(etat,parc)
listemoves=[]
siz=0
for etat in parc:
    
    if etat.finale :
        listemoves.extend(etat.precedents)
        siz=etat.prio



###############AFFICHAGE#################

 
if siz==0:
    print("No Solution Founded!")
    exit(0)
etat=EtatSommet(nbrT,nbrT,nbrT,0,[],pos)
aff=[]
aff.append(etat)
etatn=etat
for m in listemoves:
  
    etatn=unebarque.changeDeCote(etatn,m)
    aff.append(etatn)
    

state=0
while state  < siz+1: 
    refresh([aff[state].describe,print,print,print,print])    
    if ( not input("clic enter for next or 'p' for previous  ")=="P"):
        state=state+1
    else:
        state=state-1

