### Comment obtenir le flag
Sur la page de téléversement d'image, on constate un délai de traitement quand le fichier envoyé est de type jpeg. Les autres formats d'image (png, bitmap, gif...) renvoient tous une erreur.  
En envoyant un fichier avec la double extension `.jpg.jpg`, on débloque le flag `46910d9ce35b385885a9f7e2b336249d622f29b267a1771fbacf52133beddba8`.

### Expliquer la faille
Le code existant vérifie déjà le type de fichier envoyé, mais en se contentant de vérifier l'extension du fichier.

### Comment la corriger
Avec l'extension PHP [`fileinfo`](https://www.php.net/manual/en/book.fileinfo.php), il est possible d'obtenir le mime type d'un fichier, pour vérifier qu'il s'agit bien d'une image :
```PHP
$finfo = new finfo(FILEINFO_MIME, "/usr/share/misc/magic.mgc");
$finfo->file('/tmp/image.jpg');
```

Pour éviter toute exécution de code pouvant provenir d'un fichier envoyé par l'utilisateur, il est important de placer ces fichiers dans un dossier à part, avec les droits adéquats (uniquement lecture/écriture).  
Pour tout fichier envoyé par l'utilisateur, il est important de vérifier et nettoyer le nom du fichier, par exemple en combinant [`basename`](https://www.php.net/manual/en/function.basename.php) et [`realpath`](https://www.php.net/manual/en/function.realpath.php).