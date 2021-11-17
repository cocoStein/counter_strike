class Case:
    def __init__(self, x, y, valeur = False):
        self.x = x #Coor horizontal
        self.y = y #Coor vertical
        self.valeur = valeur    #Bombe ou pas
    
    def __print__(self):
       return self.valeur

    


if __name__== "main":
    print("test")
