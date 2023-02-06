
from barque import Barque,Move
from etat import EtatNerveux
from listeprio import ListePrio


mybarque = Barque("maBarque",2)
etatinit=EtatNerveux(3,3,3,0,None,True)

listeprio=ListePrio([etatinit],1)
listeprio2=ListePrio([],0)

rangy=int((mybarque.places+1)*(mybarque.places+2)/2-1)#nombre de Moves
etatact:EtatNerveux=listeprio.remove()
listeprio2.add(etatact)
while etatact.prio<6:
    for move in  range(rangy):
        
        if(mybarque.possibleMove(etatact,move)):
            etatneuf=mybarque.changeDeCote(etatact,move)
            if not etatneuf.interdit:
                listeprio.add(etatneuf)
    etatact=listeprio.remove()
    #listeprio2.add(etatact)
    #print(etatact.precedents)
m=[3,0,4,2,1,3,1,2,4,2,4]
for i in m:
    etatneuf=mybarque.changeDeCote(etatinit,i)
    etatact=etatneuf

print(etatact.nbrC)
print(etatact.nbrM)
print(etatact.finale)
