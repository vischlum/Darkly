### Comment obtenir le flag
En voulant se connecter sur le site, n'aillant pas de compte, dirigeons-nous sur la page oubli de mot de passe.  
On observe qu'il n'y a pas de formulaire à remplir, seulement un bouton Submit qui ne nous permet pas de retrouver de mot de passe : "Sorry Wrong Answer."  
En inspectant les éléments de la page avec l'outil du navigateur, on aperçoit qu'un mail est relié au système de réinitialisation de mot de passe : envoi d'une requête POST vers `index.php?page=recover` avec les paramètres `mail=webmaster%40borntosec.com&Submit=Submit`.  
En modifiant la valeur du champ mail dans l'onglet Éléments de l'outil, on obtient le flag.  
Il est aussi possible d'observer et d'interagir avec ces valeurs a l'aide d'outils créant des requêtes POST.

### Expliquer la faille
Il ne faut pas baser l'utilisation du site sur une valeur qui peut facilement être lisible et modifiable côté utilisateur. Le danger peut être l'utilisation de cette page pour envoyer des mails à l'aide de ce système de récuperation de mot de passe.

### Comment la corriger
Pour palier à ce problème d'utilisation, on peut demander des informations à l'utilisateur pour lui envoyer la réponse à sa demande de récupération de mot de passe, et effectuer les manipulation sur le serveur, stockant ainsi les variables hors de portée de l'utilisateur.  
Pour plus de détails sur les bonnes pratiques en matière de formulaire de récupération de mot de passe, l'OWASP a [de bonnes recommandations](https://cheatsheetseries.owasp.org/cheatsheets/Forgot_Password_Cheat_Sheet.html) (par exemple l'envoi d'un code par SMS avant de pouvoir réinitialiser le mot de passe).
