# Introduction

Présentation du projet.

# Structure

Les données ne sont pas sur le github pour des soucis de confidentialité/espaces. 
On suppose que les données brutes se trouvent dans un dossier `data/raw`.
On entend par données brut les données télécharger à cette adresse : `https://www.kaggle.com/carlolepelaars/toy-dataset` ou les données envoyé par le client tel jour.
Les données pour les quelles, on souhaite faire des prédictions se trouvent dans le dossier `data/test`.
On trouve dans le dossier `rapport` les éléments nécessaires pour la présentation.
On trouve dans `src` les modules créés pour ce projet.
On trouve dans `model` les modeles de ML.
etc.

# Exécutables

* `process.py` va traiter les données brutes (`data/raw`) et créer un/des nouveau(x) fichiers dans `data/process`. Ici décrire les transformations opérées et nouveaux fichiers créés. Par exemple `toy_dataset.csv` est la version modifié du fichier du même nom dans laquelle on a ajouté une colonne des revenues mensuels. L'idée étant qu'avec une seule commande, on puisse passer des données brutes aux données nécessaires pour la suite. Ce programme pourra appeler des fonctions définis dans d'autres module qui se trouvent dans `src`.

* `train_model.py` entraîne un modèle KNN sur le fichier `data/process/db.csv` qui prédit la colonne col1 en utilisant les colonnes col2, col3. Le modèle est évalué en utilisant l'accuracy, le score est affiché dans le terminal. Le modèle est ensuite enregistré dans model/knn.h5.

* `predict.py` utilise model/knn.h5 pour prédire col1 du fichier `data/test/to_predict.csv` le résultat est ensuite enregistré dans un nouveau fichier : `data/test/prediction_knn.csv`.

* `get_graphs.py` créé un histogramme à partir de la colonne `monthly` du fichier traité `toy_databae.csv` et l'enregistre dans rapport/image.
