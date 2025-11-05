def subject5_solution():
    print("=== SUJET 5: Tri Topologique - Ordonnancement de Tâches ===\n")
    graphe = {
        'A': ['B', 'C'], 
        'B': ['D'],    
        'C': ['D'],       
        'D': ['E'],
        'E': [] 
    }
    print("Graphe des dépendances:")
    for tache, dependances in graphe.items():
        print(f"  {tache} → {dependances}")
    visites = set()
    ordre_topologique = []
    print("\nStructures initialisées: visites, ordre_topologique")
    def parcourir(noeud):
        visites.add(noeud)
        print(f"  Visite de {noeud}")

        for voisin in graphe[noeud]:
            if voisin not in visites:
                print(f"    → Exploration de la dépendance {voisin}")
                parcourir(voisin)
        
        ordre_topologique.insert(0, noeud)
        print(f"  Ajout de {noeud} à l'ordre: {ordre_topologique}")
    print("\nDébut du tri topologique:")
    for noeud in graphe:
        if noeud not in visites:
            print(f"\nDépart depuis {noeud}:")
            parcourir(noeud)
    print("\n" + "="*50)
    print("RÉSULTAT FINAL:")
    print("="*50)
    print(f"Ordre d'exécution valide: {' → '.join(ordre_topologique)}")
    durees = {'A': 2, 'B': 3, 'C': 1, 'D': 4, 'E': 2}
    temps_total = 0
    print("\nCalcul des temps avec durées:")
    for tache in ordre_topologique:
        temps_total += durees[tache]
        print(f"  {tache} ({durees[tache]}h) → Temps cumulé: {temps_total}h")
    print(f"\nTemps total d'exécution: {temps_total}h")
subject5_solution()
