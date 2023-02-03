
from barque import Barque,Move
from etat import EtatNerveux
from listeprio import ListePrio


mybarque = Barque("maBarque",2)
etatinit=EtatNerveux(3,3,3,0,None,True)

listeprio=ListePrio([etatinit],1)

rangy=int((mybarque.places+1)*(mybarque.places+2)/2-1)#nombre de Moves
etatact:EtatNerveux=listeprio.remove()

while( etatact.prio<102 ):
    for move in  range(rangy):
        
        if(mybarque.possibleMove(etatact,move)):
            etatneuf=mybarque.changeDeCote(etatact,move)
            if not etatneuf.interdit:
                listeprio.add(etatneuf)
                
    
    etatact=listeprio.remove()
    print(etatact.prio)

print(etatact.precedents)