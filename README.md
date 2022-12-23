# GI-D-Face-Detector-
Le code crée une interface graphique pour détecter les visages en temps réel avec la caméra de l'appareil et enregistrer les images dans un dossier choisi par l'utilisateur.

Face Detection Program
This program is designed to detect faces in real-time using the device's camera and save the images with detected faces to a user-specified folder.

Requirements:

. 'cv2' : This library is used to capture frames from the device's camera.
. 'dlib' : This library is used to detect faces in the images.
. 'tkinter' : This library is used to create the graphical user interface (GUI).
. 'PIL' : This library is used to display the images with detected faces in the GUI.

HOW TO USE

1. Run the program and a GUI window will appear.

2. In the text field at the top of the window, enter the name of the folder where you want to save the images with detected faces. The folder will be created if it does not exist.

3. Click the "Detect Faces" button to start the face detection process.

4. The program will start capturing frames from the device's camera and displaying them in the GUI window. For each frame, it will detect any faces present in the image and draw a blue rectangle around them.

5. If you want to save an image with detected faces, press the "o" key on your keyboard. The image will be saved to the specified folder with a unique name (e.g. "image_0.jpg", "image_1.jpg", etc.).

6. To stop the face detection process, close the GUI window or press the "q" key on your keyboard.

NOTES

. The program will stop capturing frames and terminate when the device's camera is turned off or there are no more frames to capture.

. The program may run slower on devices with low processing power.

. The face detection accuracy may vary depending on the lighting conditions and the quality of the camera.

. I hope this documentation helps you understand and use the program effectively. Let me know if you have any questions or need further clarification.