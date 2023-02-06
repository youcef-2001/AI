


class sommet:
    def __init__(self,val,) -> None:
        self.val=val
        self.voisin=[]



class graph:
    def __init__(self) :
        self.sommets=[]
        self.arc=[]
    def adds(self,e):
        self.sommets.append(e)