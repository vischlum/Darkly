### Comment obtenir le flag
En se rendant sur la page member du site, on apercoit un formulaire pour recuperer des informations sur un membre a l'aide de son id.
En essayant une declaration SQL dans le formulaire on apercoit une vulnerabilite face au injection SQL, a l'aide du prefix 1 or 1, afin de ne pas recuperer seulement un membre selon son id, mais toute les informations des membres. Une de ces information nous indique qu'il y a surement un flag a recuperer, nous allons donc essayer d'afficher toute les table et colonnes de la bdd a l'aide de la requette adequate.
1 or 1 UNION select table_name, column_name FROM information_schema.columns
Apres avoir survole les informations recupere avec cette requette, on apercoit une table users qui nous interesse particulierement, avec plusieurs colonnes qu'il va falloir essayer de recuperer de la meme maniere que les tables et les colonnes precedemment.
Finalement, a l'aide de la requette suivante, on obtient une informations menant a la bonne piste:
1 or 1 UNION SELECT countersign, commentaire FROM users
Puisque celle-ci nous affiche un md5 a decrypter: 5ff9d0165b4f92b14994e5c685cdce28 : FortyTwo
Puis a encrypter en sha256.
On obtient ainsi le flag.

### Expliquer la faille
L'injection SQL se produit généralement lorsque vous demandez à un utilisateur d'entrer des données, comme son nom d'utilisateur/identifiant, et qu'au lieu d'un nom/identifiant, l'utilisateur vous donne une instruction SQL que vous exécuterez sans le savoir sur votre base de données.

### Comment la corriger
On peut mettre en place differente mesure pour se proteger contre les injection SQL.
On peut deja tester et filtrer les methode et parametres utilises en entree dans les applications pour la base de donnee. Celles-ci devraient etre en accord avec le type de donnees attendu par le formulaire.
Il est aussi important de retirer les messages d'erreurs externes emis par les applications, evitant ainsi d'indiquer des informations sur le systeme ou les structures utilisees par la base de donnee.
Evidemment, il faut avoir des services et applications a jour, eviter d'avoir un nombre inutiles de comptes utilisateur que le pirate pourra utiliser pour acceder au formulaire vulnerable.
Il est aussi interessant de chiffrer les donnees sensible dans la base de donnee.
Il est maintenant recommande de ne pas utiliser le module PHP mysql, de cette maniere les codes sont plus surs. La fonction mysqli_real_escape_string() du script PHP permet d'eviter d'emettre des caracteres speciaux aux bases de donnees SQL sous leur forme originale. Les caracteres problematiques des donnees utilisateurs seront remplaces par la variante SQL securisee ('\').
