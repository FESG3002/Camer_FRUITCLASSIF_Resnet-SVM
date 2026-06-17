# Projet de Reconnaissance de Fruits

Ce projet est une application de Reconnaissance de Fruits construite avec Python, utilisant TensorFlow pour l'apprentissage profond et CustomTkinter pour l'interface graphique utilisateur.

## Prérequis

Avant de commencer, assurez-vous d'avoir installé :
- Python 3.7 ou supérieur
- pip (installateur de paquets Python)

## Installation

1. Clonez le dépôt :
   ```
   git clone https://github.com/votreutilisateur/projet-reconnaissance-fruits.git
   cd projet-reconnaissance-fruits
   ```

2. Créez un environnement virtuel (optionnel mais recommandé) :
   ```
   python -m venv venv
   source venv/bin/activate  # Sur Windows, utilisez `venv\Scripts\activate`
   ```

3. Installez les paquets requis :
   ```
   pip install -r requirements.txt
   ```

## Fichiers Requis

Assurez-vous d'avoir les fichiers suivants dans votre répertoire de projet :
- `poidmodvg5.h5` : Fichier de poids pré-entraînés VGG16
- `svm_model2.pkl` : Modèle SVM entraîné pour la classification des fruits

## Lancement de l'Application

Pour lancer l'application de Reconnaissance de Fruits :

```
python main.py
```

## Utilisation

1. Cliquez sur le bouton "Parcourir" pour sélectionner une image d'un fruit.
2. Cliquez sur "Reconnaître" pour classifier le fruit.
3. L'application affichera le fruit prédit, le niveau de confiance, et un graphique à barres des probabilités pour chaque classe de fruit.

## Personnalisation

- Vous pouvez changer le mode d'apparence (Clair/Sombre) et l'échelle de l'interface utilisateur dans la barre latérale.
- Pour ajouter ou modifier les classes de fruits, mettez à jour la liste `class_names` dans la classe `FruitRecognitionApp`.

## Dépannage

Si vous rencontrez des problèmes :
- Assurez-vous que tous les paquets requis sont correctement installés.
- Vérifiez que les fichiers de modèle (`poidmodvg5.h5` et `svm_model2.pkl`) sont au bon endroit.
- Vérifiez que les images d'entrée sont dans un format supporté (jpg, png, jpeg).



