### Comment obtenir le flag
En allant sur le formulaire permettant de laisser des feedback sur le site, on peut essayer d'injecter du code malveillant a l'aide de balise script ou de plusieurs autres methode portant le nom cross-site scripting (xss)
\- script
\- \<script\>alert(42)\</sript\>
On obtient ainsi le flag.

### Expliquer la faille
Le principe de la faille est d'injecter des donnees arbitraires dans un site web, par exemple en deposant un message dans un forum, ou par des parametres d'URL. Si ces donnees arrivent telles quelles dans la page web transmise au navigateur sans avoir ete verifiees, alors il existe une faille : on peut s'en servir pour faire executer du code malveillant en langage de script par le navigateur web qui consulte cette page.

### Comment la corriger
Plusieurs techniques permettent d'eviter le XSS:
Retraiter systematiquement le code HTML produit par l'application avant l'envoi au navigateur;
Filtrer les variables affichees ou enregistrees avec des caracteres '<' et '>' (htmlspecialchars() en PHP - htmlentities()), ou prefixer les donnees utilisateur pour les distinguer des autres et ne jamais utiliser leurs valeurs dans une chaine executable sans filtrage prealable.
Par ailleurs, il est egalement possible de se proteger des failles XSS a l'aide d'equipements reseaux dedies tels que les pare-feux applicatifs. Ces derniers permettent de filtrer l'ensemble des flux HTTP afin de detecter les requetes suspectes.
