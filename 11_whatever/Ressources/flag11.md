### Comment obtenir le flag
En regardant le fichier robots.txt du site, on apercoit differente informations interessante (tout les user-agent autorise, utile pour la resolution du flag.07) et deux pages: /whatever et /.hidden.
On s'occupe ici de whatever: http://[ip]/whatever/
Sur la page se trouve un fichier htpasswd contenant les informations d'un utilisateur:
root:8621ffdbc5698829397d97767ac13db3
le mdp est en md5, le dechiffrage nous donne: dragon
En essayant ces id sur la page de connection principale du site nous avons une erreur, nous cherchons donc une page de connection differente:
http://[ip]/admin/
Les id marchent sur celles-ci, nous avons donc le flag.

### Expliquer la faille
Le fichier robots.txt, aussi appele protocole d'exclusion des robots, est un fichier place a la racine d'un site web contenant une liste des ressources du site qui ne sont pas censees etre indexees par les robots d'indexation des moteurs de recherche. Ce n'est pas un element de securite, simplement une directive d'utilisation pour les robots bienveillants.
Car effectivement, un robot (ou un utilisateur) peut tout de meme aller voir ce fichier, ou les pages du site s'y trouvant afin de recuperer des informations qui ne lui sont pas destine comme des mail pour pratiquer le spam, ou autres. En l'occurence nous voyont l'existence d'un dossier contenant un fichier htpasswd, qui nous donne les id root de l'interface admin du site.

### Comment la corriger
Une premiere protection contre cette vulnerabilite serait d'interdire l'acces au fichier htpasswd, au lieu de la trouver dans le robots.txt peut etre la deplacer dans un fichier .htaccess.
De correctement crypter son contenu.
