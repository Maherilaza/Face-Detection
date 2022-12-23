# Détection de visages avec OpenCV
Ce code Python utilise OpenCV et plusieurs classifieurs de visages pour détecter les visages sur une photo et enregistrer ces visages dans un dossier.

# Prérequis:
. Python 3
. OpenCV

# Utilisation :
1. Téléchargez ou clonez ce répertoire sur votre ordinateur.
2. Ouvrez un terminal et naviguez jusqu'au répertoire du code.
3. Exécutez le code en tapant la commande suivante : python detect_faces.py
4. Suivez les instructions à l'écran pour saisir le nom de l'image à traiter.
5. Les visages détectés sur l'image seront enregistrés dans un dossier nommé 'visages'.

# Notes
. Assurez-vous de remplacer 'nom_du_classifieur_1.xml' et 'nom_du_classifieur_2.xml' par les noms des fichiers XML contenant les classifieurs de visages que vous souhaitez utiliser.

.Vous pouvez ajouter autant de classifieurs que vous le souhaitez en suivant la même approche.

.Vous pouvez également entraîner votre propre classifieur de visages en utilisant l'algorithme AdaBoost en utilisant la bibliothèque d'apprentissage automatique d'OpenCV, comme décrit dans la documentation d'OpenCV : https://docs.opencv.org/3.4/dc/d88/tutorial_traincascade.html. Cependant, cela peut être un processus complexe et nécessite une bonne connaissance de l'apprentissage automatique et de la bibliothèque d'OpenCV.

# Licence
Ce code est sous licence MIT. Vous êtes libre de l'utiliser et de le modifier à votre convenance.