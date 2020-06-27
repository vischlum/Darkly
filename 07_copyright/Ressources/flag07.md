### Comment obtenir le flag
En allant sur la page survey: http://[ip]/?page=e43ad1fdc54babe674da7c7b8f0127bde61de3fbe01def7d00f151c2fcca6d1c ; On profite d'une petite musique, et on obtient le flag: decrypt(e43ad1fdc54babe674da7c7b8f0127bde61de3fbe01def7d00f151c2fcca6d1c) -> TAMERE.
N'aillent plus d'information affichee, on decide a nouveau d'utiliser l'inspecteur d'elements; apparait alors des commentaires dans le code html.
Deux d'entres eux nous interessent particulierement:
\- You must cumming from : "https://www.nsa.gov/" to go to the next step
\- Let's use this browser : "ft_bornToSec". It will help you a lot.
Le premier commentaire nous indique qu'il faut se servir de la valeur referer (Referrer) de la variable header afin d'indiquer que l'on vient de l'adresse suggeree.
Le second commentaire nous tourne vers la valeur du User-Agent de notre session.
Afin d'indiquer a notre navigateur et au site le referer et le user-agent desire, nous utilisons curl dans le Terminal a l'aide de cette commande:
curl -e "https://www.nsa.gov/" -A "ft_bornToSec" http://[ip]/index.php\?page\=e43ad1fdc54babe674da7c7b8f0127bde61de3fbe01def7d00f151c2fcca6d1c | grep flag
On peut aussi le faire avec des outils de navigateuret des extensions.
Avec le grep de flag, nous recuperons le flag.

### Expliquer la faille
Le referer indique la page precedente sur laquelle nous nous trouvions avant d'arriver a l'adresse actuelle, elle permet de debloquer ou non certains composant sur une page, comme des coupons de reduction sur des shop en ligne si l'on vient d'un site partenaire. Le user-agent specifie le navigateur avec lequel on surf et ses informations.
En aillant la main sur ces deux informations nous pouvont nous faire passer pour ce que nous ne sommes pas et acceder a des informations confidentielle.

### Comment la corriger
Afin de verifier l'identite de quelqu'un, il est preferable d'aussi rajouter une confirmation quelconque.
