### Comment obtenir le flag
En allant sur la page de vote: http://[ip]/index.php?page=survey
On apercoit un formulaire de vote a l'aide de tableau deroulant contenant des entier allant de 1 a 10.
Avec les outils de développement du navigateur, en inspectant les elements, on observe que les valeurs de ce tableau sont indiquee en dur dans une balise option. Elles sont, au moment du clique, envoyee a une fonction javascript qui les applique au resultats de la page.
Il est ainsi possible de modifier directement la valeur de ces champs options dans l'inspecteur d'elements ou dans une requette POST effectuee depuis un Terminal.
Ainsi on falsifie la valeur du vote, en rajoutant +100000 a n'importe qui, sans oublier de rajouter +1 au compteur de Ly qui, malheureusement se trouvait a 666 vote (comme la couleur du body.css du site d'ailleurs).
On obtient ainsi le flag.

### Expliquer la faille
Il ne faut pas baser la sécurité et l'utilisation du site sur une valeur qui peut facilement être lisible et modifiable côté utilisateur si celle-ci peut avoir des impacts significatif.

### Comment la corriger
Corriger ce genre de vulnerabilite ce fait basiquement en controlant l'entree que donne l'utilisateur.
