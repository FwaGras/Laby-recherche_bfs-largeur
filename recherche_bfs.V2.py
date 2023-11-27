#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#importation des bibliothèques
import networkx as nx
from NSIT_04d_file import *

def chercher_bfs(laby:nx.Graph, source:int = None, destination:int = None)->list:
    """ Cherche le chemin le plus court entre les sommets source et destination
        selon le parcours en largeur.
    """
    # Initialisation des sommets source et destination s'ils ne sont pas renseignés
    # Récupère la liste des sommets
    nodes = list(laby.nodes())
    # Si source n'est pas renseigné, alors on impose source = 0
    if source == None:
        source = nodes[0]
    # Si destination n'est pas renseigné, alors on impose destination = dernier sommet
    if destination == None:   
        destination = nodes[-1]
    
    sommet_visite = []
    f = File()
    f.ajoute(source)
    while f.estVide() != True:
        tmp = f.extrait()
        print(tmp)
        if tmp not in sommet_visite:
            sommet_visite.append(tmp)
        for voisin in laby.neighbors(tmp):
            if voisin not in sommet_visite and not f.present(voisin):
                f.ajoute(voisin)

    sommet_courant = sommet_visite[-1]
    itinéraire_inverse = []
    # On reste dans la boucle tant que l'on a pas rejoint le sommet de début
    while sommet_courant!= sommet_visite[0]:
        voisins = laby.neighbors(sommet_courant)
        print("débug sommet courant:",sommet_courant)
        # Je cherche maintenant le premier sommet de sommet_courant qui apparaît parmis les voisins
        # Cette fonction n'existe pas encore, on s'en occupe après
        prochain_sommet = premier_voisin(voisins, sommet_visite)
        arete = (sommet_courant, prochain_sommet)
        itinéraire_inverse.append(arete)
        # Il ne reste plus qu'à désigner le nouveau sommet courant
        sommet_courant = prochain_sommet
        print("débug iti inverse :",itinéraire_inverse)
        print("débug  nouveau sommet courant:",sommet_courant)

    itinéraire = [] # l'itinéraire attendu
    for i in range(len(itinéraire_inverse)-1, -1,-1):
        itinéraire.append(itinéraire_inverse[i][1], itinéraire_inverse[i][0]) #inverse l'ordre des noeuds dans les tuples (arêtes)

    return itinéraire.reverse()


def premier_voisin(voisins:list, sommet_visite:list)->int:
    '''
    prend en paramètres la liste des voisins d’un sommet et la liste des sommets visités
    et qui renvoie parmi la liste des voisins visités, le premier sommet de la liste voisin.
    '''
    
    for visite in sommet_visite:
        print("débug visite:",visite)
        print("débug som_vis:",sommet_visite)
        if visite in voisins:
            return visite
    return None # aucun voisin visité n'a été trouvé parmi les voisins