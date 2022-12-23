import subprocess

# Installer les bibliothèques et modules Python nécessaires à l'exécution du code
subprocess.run(["pip", "install", "-r", "requirement.txt"])

# Lancer le programme principal
subprocess.run(["python", "main.py"])
