import cv2
import os

image_name = input("Saisissez le nom de l'image (ex: image.jpg) :")

image = cv2.imread(image_name)
face_cascade1 = cv2.CascadeClassifier('classifier/haarcascade_frontalface_default.xml')
face_cascade2 = cv2.CascadeClassifier('classifier/haarcascade_profileface.xml')

faces1 = face_cascade1.detectMultiScale(image, 1.3, 5)
faces2 = face_cascade2.detectMultiScale(image, 1.3, 5)
if not os.path.exists('visages'):
    os.makedirs('visages')

i = 1
for (x,y,w,h) in faces1:
    face_cropped = image[y:y+h, x:x+w]
    cv2.imwrite('visages/visage_' + str(i) + '.jpg', face_cropped)
    i += 1

for (x,y,w,h) in faces2:
    face_cropped = image[y:y+h, x:x+w]
    cv2.imwrite('visages/visage_' + str(i) + '.jpg', face_cropped)
    i += 1
