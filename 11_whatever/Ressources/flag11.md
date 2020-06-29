### Comment obtenir le flag
En regardant le fichier `robots.txt` du site, on repère différentes informations intéressantes (notamment que tous les `user-agent` sont autorisés, utile pour la résolution du flag07) et deux pages: `/whatever` et `/.hidden`.  
On s'occupe ici de `whatever` (`http://[ip]/whatever/`)

Sur la page se trouve un fichier `htpasswd` contenant les informations d'un utilisateur : `root:8621ffdbc5698829397d97767ac13db3`  
Le mot de passe est le hash MD5 de `dragon`.

En essayant ces identifiants sur la page de connexion principale du site, nous avons une erreur. Nous essayons alors sur la page de connexion du panel d'administration (`http://[ip]/admin/`).  
Nous pouvons nous connecter, et obtenons ainsi le flag.

### Expliquer la faille
Le fichier `robots.txt`, aussi appelé protocole d'exclusion des robots, est un fichier placé à la racine d'un site web contenant une liste des ressources du site qui ne sont pas censées etre indexées par les robots d'indexation des moteurs de recherche. Ce n'est pas un élément de sécurité, simplement une directive d'utilisation pour les robots bienveillants.  
Les identifiants pour accéder au panel d'administration ne devraient pas être accessibles à n'importe quel visiteur (robot ou humain).  

### Comment la corriger
Une première protection contre cette vulnerabilité serait d'interdire l'accès au fichier `htpasswd`, avec un simple fichier [`.htaccess`](https://en.wikipedia.org/wiki/.htaccess) (puisque le site utilise Apache comme serveur web).  
Il serait aussi intéressant de mieux [chiffrer le mot de passe](https://httpd.apache.org/docs/2.4/fr/misc/password_encryptions.html) en utilisant l'algorithm `bcrypt` (au lieu du MD5).
