class Case:
    def __init__(self, x, y, valeur = False, numero = 0, open = False):
        self.x = x #Coor horizontal
        self.y = y #Coor vertical
        self.valeur = valeur    #Bombe ou pas
        self.numero = numero    #nbr bombes
        self.open = open  #discovered or not ( True / False)
    
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
        
    def voisins(self, grille):
    
        voisins = []
        nbligne = len(grille)
        nbcol = len(grille[0])
        if self.x-1 in range(nbligne):
            voisins.append((self.x-1,self.y))
            if self.y-1 in range(nbcol):
                voisins.append((self.x-1,self.y-1))
            if self.y+1 in range(nbcol):
                voisins.append((self.x-1,self.y+1))
        if self.x+1 in range(nbligne):
            voisins.append((self.x+1,self.y))
            if self.y-1 in range(nbcol):
                voisins.append((self.x+1,self.y-1))
            if self.y+1 in range(nbcol):
                voisins.append((self.x+1,self.y+1))
        if self.y-1 in range(nbcol):
                voisins.append((self.x,self.y-1))
        if self.y+1 in range(nbcol):
                voisins.append((self.x,self.y+1))  
                
        return voisins    

if __name__== "__main__":
    print("test")
    bla = Case(14,18)
    