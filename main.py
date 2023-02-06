
from barque import Barque,Move
from etat import EtatNerveux
from listeprio import ListePrio


mybarque = Barque("maBarque",2)
etatinit=EtatNerveux(3,3,3,0,None,True)
etatinit.describe()
listeprio=ListePrio([etatinit],1)

rangy=int((mybarque.places+1)*(mybarque.places+2)/2-1)#nombre de Moves

etat=listeprio.remove()
while (etat):
    for move in range(rangy):
        if(mybarque.possibleMove(etatinit,move)):
            e=mybarque.changeDeCote(etatinit,3)
            listeprio.add(e)
            print("hello")
            if e.finale:
                break
    etat=listeprio.remove()

print(mybarque.possibleMove(etatinit,3))
etatinit=mybarque.changeDeCote(etatinit,3)
etatinit.describe()
print(mybarque.possibleMove(etatinit,0))
etatinit=mybarque.changeDeCote(etatinit,0)
etatinit.describe()
print(mybarque.possibleMove(etatinit,4))
etatinit=mybarque.changeDeCote(etatinit,4)
etatinit.describe()
print(mybarque.possibleMove(etatinit,2))
etatinit=mybarque.changeDeCote(etatinit,2)
etatinit.describe()
print(mybarque.possibleMove(etatinit,1))
etatinit=mybarque.changeDeCote(etatinit,1)
etatinit.describe()
print(mybarque.possibleMove(etatinit,3))
etatinit=mybarque.changeDeCote(etatinit,3)
etatinit.describe()
print(mybarque.possibleMove(etatinit,1))
etatinit=mybarque.changeDeCote(etatinit,1)
etatinit.describe()
print(mybarque.possibleMove(etatinit,2))
etatinit=mybarque.changeDeCote(etatinit,2)
etatinit.describe()
print(mybarque.possibleMove(etatinit,4))
etatinit=mybarque.changeDeCote(etatinit,4)
etatinit.describe()
print(mybarque.possibleMove(etatinit,2))
etatinit=mybarque.changeDeCote(etatinit,2)
etatinit.describe()
print(mybarque.possibleMove(etatinit,4))
etatinit=mybarque.changeDeCote(etatinit,4)
etatinit.describe()

print(etatinit.precedents)
print(etatinit.finale)