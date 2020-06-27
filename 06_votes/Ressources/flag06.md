### Comment obtenir le flag
Sur la page de vote `index.php?page=survey`, on voit un formulaire de vote à l'aide de tableau deroulant contenant des entiers allant de 1 à 10.  
Avec les outils de développement du navigateur, en inspectant les éléments, on observe que les valeurs de ce tableau sont indiquées en dur dans une balise `option`. Elles sont, au moment du clic, envoyées à une fonction javascript qui les applique aux résultats de la page.  
Il est ainsi possible de modifier directement la valeur de ces champs options (dans l'inspecteur d'éléments ou dans une requête POST).  
Ainsi on falsifie la valeur du vote, en rajoutant +100000 à n'importe qui, sans oublier de rajouter +1 au compteur de Ly qui, malheureusement se trouvait à 666 votes (comme la couleur du `body.css` du site d'ailleurs).  
On obtient ainsi le flag.

### Expliquer la faille
Il ne faut pas baser la sécurité et l'utilisation du site sur une valeur qui peut facilement être lisible et modifiable côté utilisateur si celle-ci peut avoir des impacts significatifs.

### Comment la corriger
À chaque fois que l'utilisateur va entrer des informations sur le site, il est indispensable de combiner vérification côté client et côté serveur, les seules vérifications côté client étant facilement contournables. En l'espèce, il aurait suffit de vérifier côté serveur que le paramètre `valeur` contienne bien un entier compris entre 1 et 10 avant de mettre à jour les résultats du vote (et renvoyer un message d'erreur sinon).  
