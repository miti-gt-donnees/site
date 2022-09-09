# Atelier "données"

Site web test rélaisé avec [Quarto](https://quarto.org/)

Le fonctionnement se rapproche de jupyterbook, l’outil utilisé pour le guide.
Les fichiers sont au format qmd qui est le format markdown avec en plus un en-tête qui permet d’ajouter des
infos pour indiquer le format de la page (table des matières, date, mot-clés). On pourra toujours faire les modifications
directement sur le gitlab.

Les dépendances sont nombreuses car Quarto est un outil orienté data science dans lequel
on peut ajouter du code R, Python ou Julia et même avoir quelque chose d’interactif 
comme ici https://quarto-dev.github.io/quarto-gallery/articles/html/html.html
On n’utilise rien de tout ca.

Le site est générée avec l'image docker python:3.9 

~~~
wget quarto-1.1.189-linux-amd64.deb
dpkg -i quarto-1.1.189-linux-amd64.de
~~~ 

Normalement les deux commandes ci-dessus suffisent pour Linux

Sur Mac

~~~
brew install quarto
git clone https://gitlab.math.unistra.fr/mi-gt-donnees/quarto.git
cd quarto
quarto preview
~~~

et on obtient une version locale de développement du site sur l'adresse indiquée en sortie

C’est un outil très “science ouverte” qui permet de lier le code, les résultats numériques avec la publication avec l’objectif d’une reproductibilité accessible et rapide.
