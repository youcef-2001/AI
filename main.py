
from barque import Barque,Move
from etat import EtatNerveux
from listeprio import ListePrio


mybarque = Barque("maBarque",2)
etatinit=EtatNerveux(3,3,3,0,None,True)
etatinit.describe()
listeprio=ListePrio([etatinit],1)

rangy=int((mybarque.places+1)*(mybarque.places+2)/2-1)#nombre de Moves
etatinit=mybarque.changeDeCote(etatinit,4)
etatinit.describe()
etatinit=mybarque.changeDeCote(etatinit,4)
etatinit.describe()
