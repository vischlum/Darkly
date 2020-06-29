### Comment obtenir le flag
Grâce à `information_schema` (cf supra), on sait qu'il existe une base `Member_Brute_Force` contenant la table `db_default` avec les champs `id`, `password` et `username`.  
Depuis la page de recherche des membres, on peut récupérer le contenu de cette table avec la requête `1 UNION SELECT username,password FROM Member_Brute_Force.db_default`.  On trouve ainsi deux utilisateurs (`root` et `admin`) ayant pour mot de passe `3bf1114a986ba87ed28fc1b5884fc2f8` (il s'agit du hash MD5 de `shadow`).  
En se connectant au site avec ces identifiants (peu importe que ce soit `root` ou `admin`), on obtient le flag `b3a6e43ddf8b4bbb4125e5e7d23040433827759d4de1c04ea63907479a80a6b2`

### Expliquer la faille
Idem flag03 (injection SQL + attaque par dictionnaire)  

### Comment la corriger
Idem flag03 (requêtes préparées + `password_hash`)  
On pourrait aussi imaginer sécuriser la connexion avec un compte administrateur en mettant en place une [authentification à deux facteurs](https://en.wikipedia.org/wiki/Multi-factor_authentication) (par exemple en demandant un code envoyé par SMS en plus du mot de passe).