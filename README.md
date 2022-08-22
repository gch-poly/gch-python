<img src="assets/polymtl_logo.png" height=100em/>

<h1 align="center">Collection d'exemples de programmation Python en Génie</h1>

[![Build and Deploy][ci-badge]][ci] [![lite-badge]][lite]

[ci-badge]: https://github.com/gch-poly/gch-python/actions/workflows/deploy.yml/badge.svg?branch=main
[ci]: https://github.com/gch-poly/gch-python/actions/workflows/deploy.yml
[lite-badge]: https://jupyterlite.rtfd.io/en/latest/_static/badge.svg
[lite]: https://gch-poly.github.io/gch-python/

## Introduction

Cette collection d'exemples est un outil d’auto-apprentissage destiné à couvrir l’ensemble des approches de programmation scientifique en génie à l'aide d'exemples concrets.

Ces exemples sont groupés en thèmes scientifiques qui sont couramment vu en génie chimique. Chaque thème est présenté sous forme d'un notebook Jupyter qui permet la modification et l'exécution du code.

- [Thème 1 - Introduction](https://gch-poly.github.io/gch-python/lab?path=theme1%2Ftheme1.ipynb)
- [Thème 2 - Calculs numériques](https://gch-poly.github.io/gch-python/lab?path=theme2%2Ftheme2.ipynb)
- [Thème 3 - Visualisation Graphique](https://gch-poly.github.io/gch-python/lab?path=theme3%2Ftheme3.ipynb)
- [Thème 4 - Données Tabulaires](https://gch-poly.github.io/gch-python/lab?path=theme4%2Ftheme4.ipynb)
- [Thème 5 - Résolution numérique d'équations différentielles](https://gch-poly.github.io/gch-python/lab?path=theme5%2Ftheme5.ipynb)
- [Thème 6 - Résolution analytique d'équations différentielles](https://gch-poly.github.io/gch-python/lab?path=theme6%2Ftheme6.ipynb)

## Ce repo

Le déploiement utilise [JupyterLite](https://github.com/jupyterlite/jupyterlite) afin de pouvoir ouvrir et exécuter des notebook Jupyter directement dans le navigateur. L'ensemble du contenu dans le dossier `content` est déployé de façon automatique en utilisant des Github Actions tirées du [template](https://github.com/jupyterlite/demo) fourni par JupyterLite. Chaque commit sur `main` enclenche l'action.

Le dossier `template` contient un notebook Jupyter qui sert de gabarit pour des nouveaux thèmes. Il contient tous les émojis et la structure Markdown à respecter.

Le module `pre-commit` est utilisé pour formatter automatiquement le code avant chaque commit.

Pour toute question ou commentaires, ne pas hésiter à ouvrir une Issue.

## Installation

Cloner le repo avec le CLI ou Github Desktop.

```
git clone https://github.com/gch-poly/gch-python.git
```
Naviguer dans le dossier `gch-python`.

Installer `pre-commit` et l'initialiser sur le repo.

```
pip install pre-commit
pre-commit install
```
