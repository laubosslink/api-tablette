# api-tablette

API permettant d'échanger des données avec le serveur de stockage principal

## Dépendances

```
sudo pip install -r requirements.txt
```
**Note**: Pour windows consulter l'installation de pip (au lien suivant)[http://stackoverflow.com/questions/4750806/how-to-install-pip-on-windows]

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
method:POST   url: /image
```
Args:
  * **file**: image

**return**: image id

#### Edit
```
method:POST   url: /image/{id}
```
Args:
  * **file**: image

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
method:POST   url: /info
```
Args:
  * **title**: the title useful as keywords
  * **content**: content for information

**return**: id de l'information

#### Get All
```
method:GET   url: /info
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

# Service back-end API

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
