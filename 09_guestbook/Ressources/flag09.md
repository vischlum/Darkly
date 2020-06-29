### Comment obtenir le flag
En allant sur le formulaire permettant de laisser des feedbacks sur le site, on peut essayer d'injecter du code malveillant à l'aide de balise script ou de plusieurs autres methode portant le nom de [*Cross-site scripting*](https://www.owasp.org/index.php/Cross-site_Scripting_(XSS)) (XSS) : `\<script\>alert(42)\</script\>`  
On obtient ainsi le flag.

### Expliquer la faille
Le principe de la faille est d'injecter des données arbitraires dans un site web, par exemple en déposant un message dans un forum, ou par des paramètres d'URL. Si ces données arrivent telles quelles dans la page web transmise au navigateur sans avoir été vérifiées, alors il existe une faille : on peut s'en servir pour faire exécuter du code malveillant en langage de script par le navigateur web qui consulte cette page.

### Comment la corriger
Plusieurs techniques permettent d'eviter le XSS :
- retraiter systématiquement le code HTML produit par l'application avant l'envoi au navigateur
- [nettoyer](https://phpbestpractices.org/#sanitizing-html) tout contenu transmis par l'utilisateur (par exemple avec la fonction PHP [`htmlentitities`](https://www.php.net/manual/en/function.htmlentities.php))
-  préfixer les données utilisateur pour les distinguer des autres et ne jamais utiliser leurs valeurs dans une chaine exécutable sans filtrage préalable.

Par ailleurs, il est également possible de se protéger des failles XSS à l'aide d'équipements réseaux dédiés tels que les pare-feux applicatifs. Ces derniers permettent de filtrer l'ensemble des flux HTTP afin de détecter les requêtes suspectes.
