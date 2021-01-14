# Estimation_Pi



### Table of Contents
You're sections headers will be used to reference location of destination.

- [Description](#description)
- [How To Use](#how-to-use)
- [References](#references)
- [License](#license)
- [Author Info](#author-info)

---

## Description
Les méthodes de Monte Carlo sont une large classe d'algorithmes de calcul qui reposent sur un échantillonnage aléatoire répété pour obtenir des résultats numériques. L'un des exemples de base pour démarrer avec l' algorithme de Monte Carlo est l' estimation de Pi .

L'idée est de simuler des points aléatoires (x, y) dans un plan 2D avec un domaine comme un carré d'unité de côté 1. Imaginez un cercle à l'intérieur du même domaine avec le même diamètre et inscrit dans le carré. Nous calculons ensuite le ratio du nombre de points qui se trouvaient à l'intérieur du cercle et le nombre total de points générés.

Ce calcul est basé sur l'heuristique suivante: Par définition 𝜋 est l'aire 𝐴(Cercle) d'un cercle de rayon 𝑟 = 1 (𝐴(Cercle) =  𝜋⋅𝑟2 est l'aire d'un cercle de rayon 𝑟).
On circonscrit alors ce cercle unité par un carré dont l'aire vaut 𝐴(Square) = 4. 
Le rapport de ces deux zones est donc égal à 𝐴(Circle)/𝐴(Square) = 𝜋/4 et donne la probabilité géométrique d'un point à l'intérieur du carré de se trouver à l'intérieur du cercle.
Supposons maintenant que nous choisissons un nombre énorme de points au hasard à l'intérieur du carré circonscrit, par exemple, en lançant des fléchettes ou en laissant tomber des gouttes de pluie dessus. Un certain nombre de ces points se retrouvera à l'intérieur de la zone décrite par le cercle tandis que le nombre restant de ces points se trouvera à l'extérieur (mais à l'intérieur du carré). Ainsi 𝑛(in) + 𝑛(out) = 𝑛 et la probabilité d'un point situé à l'intérieur de l'aire du cercle est 𝑛(in).

Heuristiquement, on a 𝐴(Circle)/𝐴(Square)≈ 𝑛(in)/𝑛  et donc 𝜋≈4 𝑛(in)/𝑛. 
Il va sans dire que cet algorithme n'est pas déterministe et que les résultats changeront probablement à chaque exécution. 
Soit la fonction suivante qui permet de simuler un point p avec deux coordonnées x et y pour déterminer si le point simulé est à l’intérieur ou à l'extérieur du cercle. 

L'algorithme
1. Initialisez circle_points, square_points et intervalle à 0.
2. Générez un point aléatoire x.
3. Générez un point aléatoire y.
4. Calculez d = x * x + y * y.
5. Si d <= 1, incrémentez circle_points.
6. Incrémenter les points_carrés.
7. Intervalle d'incrémentation.
8. Si l'incrément <NO_OF_ITERATIONS, répéter à partir de 2.
9. Calculer pi = 4 * (circle_points / square_points).
10. Terminez.



#### Technologies

- Pyspark

[Back To The Top](#read-me-template)

---

## How To Use
- Se placer dans le dossier source
- Dans le CMD, il suffit d'écrire cette commande pour compiler avec Spark le programme : spark-submit estimateur_pi.py
- Les résultats sont alors affichés dans la console CMD.

[Back To The Top](#read-me-template)

---
