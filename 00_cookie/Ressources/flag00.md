### Comment obtenir le flag
Avec les outils de développement du navigateur, on observe que le site définit un cookie contenant un champ `i_am_admin` avec la valeur `68934a3e9455fa72420237eb05902327`. Cette valeur correspond au hash MD5 de `false`.  
En remplaçant la valeur de ce champ par `b326b5062b2f0e69046810717534cb09` (hash MD5 de `true`) et en rechargant la page, on obtient une pop-in :
> Good job! Flag : df2eb4ba34ed059a1e3e89ff4dfc13445f104a1a52295214def1c4fb1693a5c3
Il est aussi possible d'observer et d'interagir avec les cookies à l'aide de l'outil [Netcat](https://en.wikipedia.org/wiki/Netcat) dans le terminal.

### Expliquer la faille
Il ne faut pas baser la sécurité du site sur une valeur qui peut facilement être lisible et modifiable côté utilisateur (en l'espèce le contenu d'un cookie).

### Comment la corriger
En restant sur l'emploi du champ d'un cookie, il aurait mieux valu utiliser la fonction [`password_hash`](https://www.php.net/manual/en/function.password-hash.php) qui utilise non seulement un algorithme plus sécurisé que le MD5 mais gère aussi le *salt* de la valeur (pour éviter une attaque par dictionnaire).  
[Pour plus de détails sur les bonnes pratiques en matière de *hashing* de mot de passe](https://phptherightway.com/#password_hashing)  
Il serait aussi intéressant de paramétrer le cookie en [`HttpOnly`](https://www.owasp.org/index.php/HttpOnly).
