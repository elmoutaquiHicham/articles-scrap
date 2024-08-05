# Extraction d'Articles de Presse avec Newspaper3k

Ce projet permet de collecter et d'extraire des articles de presse provenant de divers sites web à l'aide de la bibliothèque `newspaper3k`. Les articles extraits sont sauvegardés dans un fichier CSV pour une analyse ultérieure.

## Table des Matières

- [Installation](#installation)
- [Utilisation](#utilisation)
- [Données d'Entrée](#données-dentrée)
- [Format de Sortie](#format-de-sortie)
- [Dépendances](#dépendances)
- [Contributions](#contributions)
- [Auteurs](#auteurs)

## Installation

### Prérequis

- Python 3.x
- Pip (pour l'installation des packages)

{
    "site1": {
        "link": "https://www.example.com"
    },
    "site2": {
        "link": "https://www.another-example.com"
    }
}

### Installation des Dépendances

Pour installer les bibliothèques nécessaires, utilisez la commande suivante :

```sh
pip install feedparser newspaper3k pandas numpy
