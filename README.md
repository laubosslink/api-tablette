# api-tablette

API permettant d'échanger des données avec le serveur de stockage principal

## Lancer le serveur

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
**return**: id de l'information

#### Get
```
method:GET   url: /info/{id}
retour: info content
```
**return**: contenu

#### Supprimer (admin)
```
method:GET   url: /info/delete{id}
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
method:GET url: /comment/postID/
retour: id comment
```
**return**: commentaire id

#### Get
```
method:GET url: /comment/postID/{id}
retour: content
```
**return**: commentaire

####  Upvote/downvote
```
method:POST   url: /comment/postID/{id}/vote/{0,1}
```

#### supprimer (admin)
```
method:GET url: /comment/postID/{id}
```

#Service back-end API

#BDD

- images
- information mairie
- forum
  - posts
    - commentaires
