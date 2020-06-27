### Comment obtenir le flag
On observe que le site propose plusieurs liens redirigeant vers d'autres adresses comme un compte Facebook, Twitter ou encore Instagram avec une méthode GET : `http://[ip]/index.php?page=redirect&site=facebook`  
En remplaçant la valeur du champ `site` par une autre, on obtient le flag.

### Expliquer la faille
Il ne faut pas baser la redirection sur une valeur qui peut être modifiée côté utilisateur (en l'espèce le paramètre de la requête), car cela peut mener à l'utilisation de plusieurs vulnerabilités, comme l'exécution de code, ou la redirection vers des pages indésirables, et même du phishing.

### Comment la corriger
En restant sur l'emploi de redirections, il aurait mieux valu ne pas laisser l'utilisateur contrôler les paramètres de redirection. Cela peut se faire en utilisant un id relié en interne aux URL voulues au lieu d'une entrée.  
Il est aussi possible de vérifier le lien de redirection, qui devrait commencer par http:// ou https:// et invalider les autres URL pour éviter l'utilisation malsaine d'une URI à l'aide de javascript.  
Du point de vue du code, il faut toujours garder une condition « attrape-tout » si on n'entre pas dans les conditions précédemment testées (que ce soit un `else`, ou dans le cas d'un [`switch`](https://www.php.net/manual/en/control-structures.switch.php) un `default`).  
