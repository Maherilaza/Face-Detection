# GI-D-Face-Detector-
. Programme de détection de visages:
Ce programme a été conçu pour détecter les visages en temps réel en utilisant la caméra de l'appareil et enregistrer les images avec les visages détectés dans un dossier spécifié par l'utilisateur.

Prérequis:

Pour exécuter ce programme, vous devrez avoir installé les bibliothèques suivantes :
. 'cv2' : cette bibliothèque est utilisée pour capturer les frames de la caméra de l'appareil.
. 'dlib' : cette bibliothèque est utilisée pour détecter les visages dans les images.
. 'tkinter' : cette bibliothèque est utilisée pour créer l'interface graphique utilisateur (GUI).
. 'PIL' : cette bibliothèque est utilisée pour afficher les images avec les visages détectés dans la GUI.

Comment utiliser:
1. Exécutez le programme et une fenêtre GUI s'ouvrira.

2. Dans le champ de saisie en haut de la fenêtre, entrez le nom du dossier où vous souhaitez enregistrer les images avec les visages détectés. Le dossier sera créé s'il n'existe pas.

3. Cliquez sur le bouton "Détecter les visages" pour lancer le processus de détection de visages.

4. Le programme commencera à capturer les frames de la caméra de l'appareil et à les afficher dans la fenêtre GUI. Pour chaque frame, il détectera tous les visages présents dans l'image et dessinera un rectangle bleu autour d'eux.

5. Si vous souhaitez enregistrer une image avec les visages détectés, appuyez sur la touche "o" de votre clavier. L'image sera enregistrée dans le dossier spécifié avec un nom unique (par exemple "image_0.jpg", "image_1.jpg", etc.).

6. Pour arrêter le processus de détection de visages, fermez la fenêtre GUI ou appuyez sur la touche "q" de votre clavier.

Remarques :
. Le programme arrêtera de capturer les frames et se terminera lorsque la caméra de l'appareil sera éteinte ou qu'il n'y aura plus de frames à capturer.
. Le programme peut s'exécuter plus lentement sur les appareils avec une faible puissance de traitement.
. La précision de la détection de visages peut varier en fonction des conditions d'éclairage et de la qualité de la caméra.

J'espère que cette documentation vous aidera à comprendre et à utiliser efficacement le programme. N'hésitez pas à me contacter si vous avez des questions ou avez besoin de plus de précisions.
