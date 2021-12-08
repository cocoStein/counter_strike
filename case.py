class Case:
    def __init__(self, x, y, valeur = False, numero = 0):
        self.x = x #Coor horizontal
        self.y = y #Coor vertical
        self.valeur = valeur    #Bombe ou pas
        self.numero = numero    #nbr bombes
    
    def __str__(self):
       return str(self.numero)

    
    def checkbomb(self, list_plato):
        
        if self.valeur == False:
            
            if self.x == 0:
                    pass
            else:
                  
                try:    # Check millieu gauche
                    if list_plato[self.y][self.x - 1].valeur == True:
                        self.numero += 1
                except IndexError:
                    pass

                try:    # Check bas gauche
                    if list_plato[self.y + 1][self.x - 1].valeur == True:
                        self.numero += 1
                except IndexError:
                    pass
            
            if self.y == 0:
                pass
            else:
                try:    # Check haut millieu
                    if list_plato[self.y - 1][self.x].valeur == True:
                        self.numero += 1
                except IndexError:
                    pass
                try:   # Check haut gauche
                    if list_plato[self.y - 1][self.x + 1].valeur == True:
                        self.numero += 1
                except IndexError:
                    pass
            
            if self.y == 0 or self.x == 0:
                pass
            else:
                try:    # Check haut gauche
                    if list_plato[self.y - 1][self.x - 1].valeur == True:
                        self.numero += 1
                except IndexError:
                    pass

            try:    # Check millieu droite
                if list_plato[self.y][self.x + 1].valeur == True:
                    self.numero += 1
            except IndexError:
                pass

            

            try:    # Check bas millieu
                if list_plato[self.y + 1][self.x].valeur == True:
                    self.numero += 1
            except IndexError:
                pass

            try:    # Check bas droite
                if list_plato[self.y + 1][self.x + 1].valeur == True:
                    self.numero += 1
            except IndexError:
                pass
        else:
            self.numero = "X"
        

if __name__== "main":
    print("test")
    bla = Case(14,18)
    bla.checkbomb()