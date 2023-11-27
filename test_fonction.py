def premier_voisin(voisins:list, sommet_visite:list)->int:
    '''
    prend en paramètres la liste des voisins d’un sommet et la liste des sommets visités
    et qui renvoie parmi la liste des voisins visités, le premier sommet de la liste voisin.
    '''
    
    for visite in sommet_visite:
        print("débug visite:",visite)
        print("débug som_vis:",sommet_visite)
        print("débug voisins:",voisins)
        if visite in voisins:
            return visite
    #return None # aucun voisin visité n'a été trouvé parmi les voisins

assert premier_voisin([6, 3, 7], [1, 2, 3, 4, 5, 6, 7]) == 3
assert premier_voisin([6, 3, 7], [10, 7, 1, 2]) == 7