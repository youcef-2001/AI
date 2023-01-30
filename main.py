
from barque import Barque
from barque import Move


mybarque = Barque("maBarque",2)
result =mybarque.possibilities()
for ele in result :
    ele.describe()


