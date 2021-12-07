class Case:
    def __init__(self, x, y, valeur = False, numero = 0):
        self.x = x #Coor horizontal
        self.y = y #Coor vertical
        self.valeur = valeur    #Bombe ou pas
        self.numero = numero    #nbr bombes
    
    def __str__(self):
       return str(self.numero)

    def check(self, list):

        #check en haut 
        if list[self.y] == 0:
            pass
        else:
            if list[self.x] == 0:
                pass
            else:
                if list[self.y - 1][self.x - 1].valeur == True:
                    self.numero += 1
            if list[self.y - 1][self.x].valeur == True:
                    self.numero += 1
            if list[self.x] == len(list):
                pass
            else:        
                if list[self.y - 1][self.x + 1].valeur == True:
                    self.numero += 1
                
        #check cotés gauche
        if list[self.x] == 0:
            pass
        else:
            if list[self.y][self.x - 1].valeur == True:
                    self.numero += 1

        #check en bas 
        if list[self.y] == len(list):
            pass
        else:
            if list[self.y + 1][self.x - 1].valeur == True:
                self.numero += 1
            if list[self.y + 1][self.x].valeur == True:
                self.numero += 1
            if list[self.y + 1][self.x + 1].valeur == True:
                self.numero += 1
        
        #check cotés droit
        if list[self.x] == len(list):
            pass
        else:
            if list[self.y - 1][self.x + 1].valeur == True:
                    self.numero += 1

    def checkbomb(self, list):
        # check en haut

        try:
            if list[self.y - 1][self.x - 1].valeur == True:
                self.numero += 1
        except IndexError:
            pass
        
        

if __name__== "main":
    print("test")