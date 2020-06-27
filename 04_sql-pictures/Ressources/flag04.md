### Comment obtenir le flag
En allant sur la page de recherche d'image: ?page=searchimg ; on apercoit un formulaire necessitant un id correspondant a une image. De la meme maniere que le flag.03, nous allons essayer d'appliquer une requete SQL sur ce formulaire pour recuperer les informations de la bdd.
1 or 1 UNION select table_name, column_name FROM information_schema.columns
Dans les informations recuperee, une table list_images nous interesse, avec plusieurs colonnes, que nous allons afficher.
Celle qui nous interesse se nomme title et comment:
1 or 1 UNION SELECT title, comment FROM list_images
Title: If you read this just use this md5 decode lowercase then sha256 to win this flag ! : 1928e8083cf461a51303633093573c46
Le decryptage de ce md5 nous donne: albatroz
L'encryptage de cette string nous donne le flag en sha256.

### Expliquer la faille
L'injection SQL se produit généralement lorsque vous demandez à un utilisateur d'entrer des données, comme son nom d'utilisateur/identifiant, et qu'au lieu d'un nom/identifiant, l'utilisateur vous donne une instruction SQL que vous exécuterez sans le savoir sur votre base de données.

### Comment la corriger
On peut mettre en place differente mesure pour se proteger contre les injection SQL.
On peut deja tester et filtrer les methode et parametres utilises en entree dans les applications pour la base de donnee. Celles-ci devraient etre en accord avec le type de donnees attendu par le formulaire.
Il est aussi important de retirer les messages d'erreurs externes emis par les applications, evitant ainsi d'indiquer des informations sur le systeme ou les structures utilisees par la base de donnee.
Evidemment, il faut avoir des services et applications a jour, eviter d'avoir un nombre inutiles de comptes utilisateur que le pirate pourra utiliser pour acceder au formulaire vulnerable.
Il est aussi interessant de chiffrer les donnees sensible dans la base de donnee.
Il est maintenant recommande de ne pas utiliser le module PHP mysql, de cette maniere les codes sont plus surs. La fonction mysqli_real_escape_string() du script PHP permet d'eviter d'emettre des caracteres speciaux aux bases de donnees SQL sous leur forme originale. Les caracteres problematiques des donnees utilisateurs seront remplaces par la variante SQL securisee ('\').
