### Comment obtenir le flag
Sur la page de *copyright*, on profite d'une petite musique, et on obtient le flag: `decrypt(e43ad1fdc54babe674da7c7b8f0127bde61de3fbe01def7d00f151c2fcca6d1c)` -> `TAMERE`.  
N'ayant plus d'information affichée, on décide à nouveau d'utiliser l'inspecteur d'éléments. On trouve ainsi des commentaires dans le code HTML. Deux d'entres eux nous intéressent particulièrement :
- `You must cumming from : "https://www.nsa.gov/" to go to the next step`
- `Let's use this browser : "ft_bornToSec". It will help you a lot.`

Le premier commentaire nous indique qu'il faut se servir de la valeur `Referer` du `header` afin d'indiquer que l'on vient de l'adresse suggérée.  
Le second commentaire nous tourne vers la valeur du `User-Agent` de notre session.  

Afin d'indiquer au site les paramètres voulus, nous utilisons `curl` dans le terminal : `curl -e "https://www.nsa.gov/" -A "ft_bornToSec" http://[ip]/index.php\?page\=e43ad1fdc54babe674da7c7b8f0127bde61de3fbe01def7d00f151c2fcca6d1c | grep flag`
```
\<center\>\<h2 style=\"margin-top:50px;"> The flag is : f2a29020ef3132e01dd61df97fd33ec8d7fcd1388cc9601e7db691d17d4d6188\</h2>\<br/>\<img src="images/win.png" alt="" width=200px height=200px>\</center> \<audio id="best_music_ever" src="audio/music.mp3"preload="true" loop="loop" autoplay="autoplay">
```  
On peut aussi le faire avec les outils de développement du navigateur.  

### Expliquer la faille
Le `referer` indique la page précédente depuis laquelle nous arrivons sur la page actuelle. Elle permet de débloquer ou non certains composants sur une page (par exemple des coupons de réduction sur des boutiques en ligne si l'on vient d'un site partenaire). Le `user-agent` spécifie le navigateur avec lequel on surfe et ses informations.  
En ayant la main sur ces deux informations, nous pouvons nous faire passer pour ce que nous ne sommes pas et accéder à des informations confidentielles.

Même si les commentaires ne sont pas directement visibles pour les visiteurs d'un site, ils sont bien visibles dans le code source de la page. Il est donc important de ne pas laisser traîner de données sensibles dans les commentaires avant la mise en production (cela vaut aussi pour les [`console.log`](https://developer.mozilla.org/en-US/docs/Web/API/Console/log) et les [`var_dump`](https://www.php.net/manual/en/function.var-dump)).


### Comment la corriger
Afin de vérifier l'identité de quelqu'un, il est préférable d'aussi rajouter une confirmation quelconque.  
Les développeurs doivent rester attentifs au moment de commit leur code (par exemple en faisant une recherche sur `console.log` ou `var_dump`).
