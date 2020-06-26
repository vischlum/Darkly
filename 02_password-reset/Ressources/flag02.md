### Comment obtenir le flag
En voulant se connecter sur le site, n'aillant pas de compte dirigeons nous sur la page oubli de mot de passe.
On observe qu'il n'y a pas de formulaire a remplir, seulement un bouton Submit qui ne nous permet pas de retrouver de mot de passe. "Sorry Wrong Answer."
En inspectant les elements de la page avec l'outil du navigateur, on apercoit qu'un mail est relie au systeme de reinitialisation de mot de passe.
En modifiant la valeur du champ mail dans l'onglet Elements de l'outil, on obtient le flag.
Il est aussi possible d'observer et d'interagir avec ces valeurs a l'aide d'outils creant des requetes POST.

### Expliquer la faille
Il ne faut pas baser l'utilisation du site sur une valeur qui peut facilement être lisible et modifiable côté utilisateur. Le danger peut etre l'utilisation de cette page pour envoyer des mail a l'aide de ce systeme de recuperation de mot de passe.

### Comment la corriger
Pour palier a ce probleme d'utilisation, on peut demander des information a l'utilisateur pour lui envoyer la reponse a sa demande de recuperation de mot de passe, et effectuer les manipulation sur le serveur, stockant ainsi les variable a l'ecart de l'utilisateur.
