import os
# Les deux lignes sous dessous permettent d'écrire a l'utilisateur que le programme est en cours d'initialisation
os.system("echo 'UBUNTU POST-INSTALL SCRIPT ' ")
os.system("echo 'Updating APT... '")
# Grace a apt-get update nous allons voir si il y'a des mise a jour possible
os.system("sudo apt-get update")
#Clear le terminal pour plus de visibilité pour l'utilisateur
os.system("clear")
#Nous prévenons l'utilisateur que l'installation des packages va démarrer
os.system("echo 'Installing base package' ")
# Cette ligne nous permettra d'installer git,git extra et python 3 avec les pip. Apt-get : Commande sous linux qui permet de trouver et d'installer les paquets qu'on lui demande.
os.system("sudo apt-get install --yes git git-extras build-essential python3-pip ")
#Clear le terminal pour plus de visibilité pour l'utilisateur
os.system("clear")
# L'utilisateur est prévenu que maintenant nous installerons Discord
os.system("echo 'Installing Discord'")
#Le format snap vise à permettre l'installation de nouvelles versions de logiciels dans les systèmes Linux.
# Ligne qui permet d'installer Discord
os.system("sudo snap install discord")
#Clear le terminal pour plus de visibilité pour l'utilisateur
os.system("clear")
# L'utilisateur est prévenu que maintenant nous installerons Visual studio code
os.system("echo 'Installing Visual studio code' ")
# Ligne qui permet d'installer Visual code studio
os.system("sudo snap install --classic code")

