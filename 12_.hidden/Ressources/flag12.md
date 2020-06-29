### Comment obtenir le flag
En regardant le fichier `robots.txt` du site, on repère différentes informations intéressantes (tous les `user-agent` autorisés, utile pour la résolution du flag07) et deux pages: `/whatever` et `/.hidden`.  
On s'occupe ici de `hidden` (`http://[ip]/.hidden/`).

Cette page contient 26 dossiers, eux-mêmes contenant 26 dossiers, qui à nouveau contiennent 26 dossiers, chacun contenant un `README`. Tous les `README` nous envoient chercher une information au sein de cette arborescence mais sûrement un seul d'entre eux nous sera utile.  
Vu la taille à parcourir, nous décidons d'automatiser la tâche avec un script python ([`search_md5.py`](search_md5.py)). Ce script, dans sa version finale, n'affiche les messages des README que s'ils sont lus pour la première fois, et indique leur provenance dans l'arborescence. Il parcourt l'arborescence récursivement.
```
$> python3 search_md5.py [ip]

http://192.168.43.129/.hidden/amcbevgondgcrloowluziypjdh/acbnunauucfplzmaglkvqgswwn/ayuprpftypqspruffmkuucjccv/README
b'Demande \xc3\xa0 ton voisin de gauche  \n'

http://192.168.43.129/.hidden/amcbevgondgcrloowluziypjdh/acbnunauucfplzmaglkvqgswwn/becskiwlclcuqxshqmxhicouoj/README
b"Non ce n'est toujours pas bon ...\n"

http://192.168.43.129/.hidden/amcbevgondgcrloowluziypjdh/acbnunauucfplzmaglkvqgswwn/cqqssunxyhjgdwjoafgyzoollx/README
b'Demande \xc3\xa0 ton voisin du dessous \n'

http://192.168.43.129/.hidden/amcbevgondgcrloowluziypjdh/acbnunauucfplzmaglkvqgswwn/dupoqdxhvrbqhaqokxsiigjnph/README
b'Demande \xc3\xa0 ton voisin du dessus  \n'

http://192.168.43.129/.hidden/amcbevgondgcrloowluziypjdh/acbnunauucfplzmaglkvqgswwn/ftzcgojutitjfpqrdadyfewfov/README
b'Toujours pas tu vas craquer non ?\n'

http://192.168.43.129/.hidden/amcbevgondgcrloowluziypjdh/acbnunauucfplzmaglkvqgswwn/lmpanswobhwcozdqixbowvbrhw/README
b'Demande \xc3\xa0 ton voisin de droite  \n'

http://192.168.43.129/.hidden/amcbevgondgcrloowluziypjdh/acbnunauucfplzmaglkvqgswwn/mfmtemmsbpftlvuuuwitbydbbt/README
b"Tu veux de l'aide ? Moi aussi !  \n"

http://192.168.43.129/.hidden/whtccjokayshttvxycsvykxcfm/igeemtxnvexvxezqwntmzjltkt/lmpanswobhwcozdqixbowvbrhw/README
b'99dde1d35d1fdd283924d84e6d9f1d820\n'
```

Il s'avère que le fichier `README` qui nous intéresse est trouvé en dernier, à l'adresse `http://[ip]/.hidden/whtccjokayshttvxycsvykxcfm/igeemtxnvexvxezqwntmzjltkt/lmpanswobhwcozdqixbowvbrhw/README`  
Il contient le flag `99dde1d35d1fdd283924d84e6d9f1d820`

### Expliquer la faille
Idem flag11, les visiteurs ne devraient pas avoir accès à ce genre de dossiers, uniquement au site web.

### Comment la corriger
Les fichier ou dossiers `.hidden` ne sont pas censées contenir d'informations importantes. Ils sont généralement utilisés pour sauvegarder des préférences utilisateur ou des états utilitaires.  
Ils ne sont pas sécurisés car leur accès n'est pas restreint, mais cela pourrait se faire simplement avec un fichier [`.htaccess`](https://en.wikipedia.org/wiki/.htaccess).
