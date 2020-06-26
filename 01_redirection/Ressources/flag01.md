### Comment obtenir le flag
On observe que le site propose plusieurs lien redirigeant vers d'autre adresses comme un compte Facebook, Twitter ou encore Instagram avec une methode GET: http://[ip]/index.php?page=redirect&site=facebook
En remplaçant la valeur du champ [site] par une autre, on obtient le flag.

### Expliquer la faille
Il ne faut pas baser la redirecton sur une valeur qui peut être modifie côté utilisateur (en l'espèce le parametre de la requete), car cela peut mener a l'utilisation de plusieurs vulnerabilitee, comme l'execution de code, ou la redirection vers des pages indesirable, et meme de phishing.

### Comment la corriger
En restant sur l'emploi de redirection, il aurait mieux valu ne pas laisser l'utilisateur controler les parametres de redirection. Cela peut se faire en utilisant un id relie en interne aux url voulu au lieu d'une entree. Il est aussi possible de verifier le lien de redirection, qui devrait commencer par http:// ou https:// et invalider les autres url pour eviter l'utilisation malsaine d'un URI a l'aide de javascript.
