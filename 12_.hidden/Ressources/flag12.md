### Comment obtenir le flag
En regardant le fichier robots.txt du site, on apercoit differente informations interessante (tout les user-agent autorise, utile pour la resolution du flag.07) et deux pages: /whatever et /.hidden.
On s'occupe ici de hidden: http://[ip]/.hidden/
Cette page contient 26 dossier, eux-memes contenant 26 dossier, qui a nouveau contiennent 26 dossiers, chacun contenant un README. Tout les README nous envoient chercher une informations au sein de cette arborescence mais surement un seul d'entre eux nous sera utile. Vu la taille a parcourir, nous decidons d'automatiser la tache avec un script python (search_md5.py).
python3 search_md5.py [ip]
Ce script, dans sa version finale, n'affiche les messages des README que s'il sont lu pour la premiere fois, et indique leurs provenance dans l'arborescence.
Il parcours l'arborescence recursivement.

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

Il s'avere que le fichier README qui nous interesse est trouve en dernier, a cette adresse:
http://[ip]/.hidden/whtccjokayshttvxycsvykxcfm/igeemtxnvexvxezqwntmzjltkt/lmpanswobhwcozdqixbowvbrhw/README
Son contenu est donc le flag: 99dde1d35d1fdd283924d84e6d9f1d820

### Expliquer la faille
Le fichier robots.txt, aussi appele protocole d'exclusion des robots, est un fichier place a la racine d'un site web contenant une liste des ressources du site qui ne sont pas censees etre indexees par les robots d'indexation des moteurs de recherche. Ce n'est pas un element de securite, simplement une directive d'utilisation pour les robots bienveillants.
Car effectivement, un robot (ou un utilisateur) peut tout de meme aller voir ce fichier, ou les pages du site s'y trouvant afin de recuperer des informations qui ne lui sont pas destine comme des mail pour pratiquer le spam, ou autres. En l'occurence nous voyont l'existence d'un dossier contenant une multitude d'informations inutile permettant de cacher une seule informations utile.

### Comment la corriger
Les fichier ou dossier .hidden ne sont pas censees contenir d'informations importantes, ils sont generalement utilises pour sauvegarder des preferences utilisateur ou des etats utilitaire. Il ne sont pas securises car leurs access n'est pas restraint.
