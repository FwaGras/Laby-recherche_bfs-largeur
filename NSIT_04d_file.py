class FileVide(Exception):
    """
        extraction à partir d'une file vide
    """
    pass

class File:
    def __init__(self):
        self.L = []
    
    def estVide(self):
        return self.L == []
    
    def ajoute(self,x):
        self.L.append(x)
        
    def extrait(self):
        assert not self.estVide(), "file vide"
        return self.L.pop(0)
    
    def taille(self):
        return len(self.L)
    
    def sommet(self):
        return self.L[0]
    
    def present(self, x):
        return x in self.L
