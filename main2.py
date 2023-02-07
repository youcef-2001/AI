
from barque import Barque
from etat import EtatSommet
import sys
import os
# import sleep to show output for some time period




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
       
    
else:
    print("Execution par Defaut !")


    


unebarque=Barque(places)
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
for etat in parc:
    
    if etat.finale :
        listemoves.extend(etat.precedents)

print(listemoves)
#################
###############AFFICHAGE

 
def refresh(dess):
    if os.name == 'posix': 
        os.system("clear")
    else:
        os.system("cls")
    print(dess)

