# Algorithmes de tri en Python

Ce module implémente les principaux algorithmes de tri classiques en Python. Chaque algorithme est optimisé et documenté avec sa complexité algorithmique.

## Algorithmes disponibles

### Tri par sélection
- Complexité : O(n²)
- Principe : Pour chaque position, trouve le plus petit élément restant et le place à la bonne position
- Fonctions :
    - `imin(L, a, b)` : Trouve l'index du minimum dans la liste L entre les indices a et b
    - `triSelection(L)` : Effectue le tri par sélection sur la liste L

### Tri par insertion
- Complexité : O(n²)
- Principe : Construit le tri final en insérant chaque élément à sa bonne place dans la partie déjà triée
- Fonctions :
    - `echange(L, i, j)` : Échange deux éléments dans la liste
    - `triInsertion(L)` : Effectue le tri par insertion sur la liste L

### Tri à bulles
- Complexité : O(n²)
- Principe : Compare et échange les éléments adjacents jusqu'à ce que la liste soit triée
- Fonction :
    - `triBulles(L)` : Effectue le tri à bulles sur la liste L

### Tri rapide (Quicksort)
- Complexité moyenne : O(n log n)
- Principe : Divise la liste autour d'un pivot et trie récursivement les sous-listes
- Fonctions :
    - `separe(L)` : Sépare la liste en deux sous-listes autour du premier élément
    - `triRapide(L)` : Effectue le tri rapide sur la liste L

### Tri fusion (Merge sort)
- Complexité : O(n log n)
- Principe : Divise la liste en deux, trie récursivement et fusionne les résultats
- Fonctions :
    - `fusion(L1, L2)` : Fusionne deux listes triées
    - `triFusion(L)` : Effectue le tri fusion sur la liste L

## Utilisation

```python
# Exemple d'utilisation
L = [64, 34, 25, 12, 11, 90]

# Tri par sélection
L_selection = triSelection(L.copy())

# Tri par insertion
L_insertion = triInsertion(L.copy())

# Tri à bulles
L_bulles = triBulles(L.copy())

# Tri rapide
L_rapide = triRapide(L.copy())

# Tri fusion
L_fusion = triFusion(L.copy())
```