import cv2
import os

# Demander à l'utilisateur de saisir le nom de l'image
image_name = input("Saisissez le nom de l'image :")

# Lire l'image et la stocker dans une variable
image = cv2.imread(image_name)

# Charger les classifieurs de visages
face_cascade1 = cv2.CascadeClassifier('classifier/haarcascade_frontalface_default.xml')
face_cascade2 = cv2.CascadeClassifier('classifier/haarcascade_profileface.xml')

# Détecter les visages sur l'image avec le premier classifieur
faces1 = face_cascade1.detectMultiScale(image, 1.3, 5)

# Détecter les visages sur l'image avec le second classifieur
faces2 = face_cascade2.detectMultiScale(image, 1.3, 5)

# Créer le dossier 'visages' s'il n'existe pas
if not os.path.exists('visages'):
    os.makedirs('visages')

# Parcourir le tableau de coordonnées des visages détectés avec le premier classifieur
i = 1
for (x,y,w,h) in faces1:
    # Découper le visage de l'image
    face_cropped = image[y:y+h, x:x+w]
    # Enregistrer le visage dans le dossier
    cv2.imwrite('visages/visage_' + str(i) + '.jpg', face_cropped)
    i += 1

# Parcourir le tableau de coordonnées des visages détectés avec le second classifieur
for (x,y,w,h) in faces2:
    # Découper le visage de l'image
    face_cropped = image[y:y+h, x:x+w]
    # Enregistrer le visage dans le dossier
    cv2.imwrite('visages/visage_' + str(i) + '.jpg', face_cropped)
    i += 1
