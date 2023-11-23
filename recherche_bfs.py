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
    
    #itinéraire = [] #amélioration 1 : renvoyé la liste des arêtes parcourues pour trouver la sortie
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

    return sommet_visite #nx.shortest_path(laby, source, destination)