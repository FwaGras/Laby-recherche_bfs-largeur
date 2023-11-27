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
    
    aretes_deBt = []
    voisins = [] # le premier élément est le voisin qui a permis à découvrir un sommet
    bt = []
    iti = [] #amélioration 1 : renvoyé la liste des arêtes parcourues pour trouver la sortie
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
             
    for sommet in range(len(sommet_visite )-1, -1, -1):
        for voisin in laby.neighbors(sommet):
            voisins.append(sommet)
            voisin_proche = voisins[0]
            voisins.clear()
            aretes_deBt.insert(0,sommet_visite)
            aretes_deBt.insert(1,voisin_proche)
            y = tuple(aretes_deBt)
            bt.append(y)
            aretes_deBt = list(y)
            aretes_deBt.clear()

    return sommet_visite #nx.shortest_path(laby, source, destination)
    