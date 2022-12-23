import cv2
import dlib
import tkinter as tk
import os
from PIL import Image, ImageTk

# Crée une fenêtre principale
root = tk.Tk()
root.title("Détecteur de visages")

# Champ de saisie pour demander à l'utilisateur le nom du dossier de destination
folder_name_entry = tk.Entry(root)
folder_name_entry.pack()

# Bouton pour lancer la détection de visages
detect_button = tk.Button(root, text="Détecter les visages", command=detect_faces)
detect_button.pack()

# Label pour afficher l'image avec les visages détectés
image_label = tk.Label(root)
image_label.pack()

# Crée un détecteur de visage en utilisant dlib.get_frontal_face_detector
face_detector = dlib.get_frontal_face_detector()

def detect_faces():
    # Ouvre la caméra
    camera = cv2.VideoCapture(0)

    # Récupère le nom du dossier de destination
    folder_name = folder_name_entry.get()

    # Crée le dossier s'il n'existe pas
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

    # Compteur pour donner un nom unique aux images sauvegardées
    count = 0

    # Récupère les frames de la caméra en boucle
    while True:
        ret, frame = camera.read()
        if not ret:
            break

        # Détecte les visages dans l'image en utilisant le détecteur de visage
        faces = face_detector(frame)

        # Dessine un rectangle autour de chaque visage détecté
        for face in faces:
            x, y, w, h = face.left(), face.top(), face.width(), face.height()
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

        # Affiche l'image avec les visages détectés dans le label
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame = frame.resize((400, 300))
        frame = Image.fromarray(frame)
        frame = ImageTk.PhotoImage(frame)
        image_label.configure(image=frame)
        image_label.image = frame
        root.update_idletasks()

        # Demande à l'utilisateur s'il souhaite sauvegarder l'image
        save = input("Sauvegarder l'image ? (o/n) ")
        if save == 'o':
            # Sauvegarde l'image dans le dossier
            image_name = f"{folder_name}/image_{count}.jpg"
            cv2.imwrite(image_name, frame)
            count += 1

    # Libère les ressources de la caméra
    camera.release()

# Affiche la fenêtre principale
root.mainloop()
       
