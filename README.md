# api-tablette

API permettant d'échanger des données avec le serveur de stockage principal

## Lancer le serveur

```
python setup.py -d DEBUG
```
**Note**: utiliser l'option -h|--help pour avoir de l'aide

## Services

### Dessin

Fonctionnalités:
  * créer
  * éditer
  * envoyer
  * sauvegarder
  * suppression

#### Créer
```
method:POST   url: /image/
```
**return**: l'id de l'image

#### Editer
```
method:POST   url: /image/{id}
```
**data**: image

#### Get
```
method:GET   url: /image/{id}
```

#### Supprimer (admin)
```
method:GET   url: /image/delete/{id}
```

### Info

#### Créer
```
method:POST   url: /info/
retour: id de l'info
```
Args:
  * **title**: the title useful as keywords
  * **content**: content for information

**return**: id de l'information

#### Get
```
method:GET   url: /info/{id}
retour: info content
```
**return**: contenu

#### Supprimer (admin)
```
method:GET   url: /info/delete/{id}
```

### Post forum

Fonctionnalités:
  * lire
  * créer
  * upvote/downvote
  * supprimer

#### Créer
```
method:POST   url: /post/
```
Args:
  * **title**
  * **content**
  * picture: picture id (optional)
**return**: id du post

#### Get
```
method:GET   url: /post/{id}
```
**return**: image

#### Upvote/downvote
```
method:POST   url: /post/{id}/vote/{0,1}
```

#### Supprimer (admin)
```
method:GET   url: /post/delete{id}
```

### Commentaires

Fonctionnalités:
  * lire
  * créer
  * upvote/downvote
  * supprimer

#### Créer
```
method:GET url: /post/{post_id}/comment/
retour: id comment
```
**return**: commentaire id

#### Get
```
method:GET url: /post/{post_id}/comment/{id}
retour: content
```
**return**: commentaire

####  Upvote/downvote
```
method:POST   url: /post/{post_id}/comment/{id}/vote/{0,1}
```

#### supprimer (admin)
```
method:GET url: /post/{post_id}/comment/{id}
```

#Service back-end API

#BDD

- images
- information mairie
- forum
  - posts
    - commentaires


# Fonction de la base de donnée

- créer post/dessin/info
- get all post/dessin/info
- get un dessin
- get un post + get all comment associé
- upvote ou downvote un post/comment/dessin
- delete post/comment/dessin/info
