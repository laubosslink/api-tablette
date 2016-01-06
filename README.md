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

#### Create
```
method:POST   url: /image/
```
**return**: image id

#### Edit
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

#### Create
```
method:POST   url: /info/
```
Args:
  * **title**: the title useful as keywords
  * **content**: content for information

**return**: id de l'information

#### Get All
```
method:GET   url: /info/
```
**return**: Array of the info id

#### Get
```
method:GET   url: /info/{id}
```
**return**: content

#### Delete (admin)
```
method:GET   url: /info/delete/{id}
```

### Post forum

Feature:
  * Get
  * create
  * upvote/downvote
  * delete

#### Create
```
method:POST   url: /post/
```
Args:
  * **title**
  * **content**
  * picture: picture id (optional)

**return**: id du post

#### Get All
```
method:GET url: /post/
```
**return**: array of post id

#### Get
```
method:GET   url: /post/{id}
```
**return**: post

#### Upvote/downvote
```
method:POST   url: /post/{id}/vote/{0,1}
```

#### Supprimer (admin)
```
method:GET   url: /post/delete{id}
```

### Comment

Features:
  * Get
  * créer
  * upvote/downvote
  * delete

#### Create
```
method:GET url: /post/{post_id}/comment/
retour: id comment
```
**return**: commentaire id

#### Get All
```
method:GET url: /post/{post_id}/comment/
```
**return**: Array of comment id which are on post_id

#### Get
```
method:GET url: /post/{post_id}/comment/{id}
```
**return**: comment

####  Upvote/downvote
```
method:POST   url: /post/{post_id}/comment/{id}/vote/{0,1}
```

#### Delete (admin)
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
