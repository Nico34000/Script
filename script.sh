#!/bin/bash
# Les deux lignes sous dessous permettent d'écrire a l'utilisateur que le programme est en cours d'initialisation
echo "UBUNTU POST-INSTALL SCRIPT"
echo "Updating APT..."
# Grace a apt-get update nous allons voir si il y'a des mise a jour possible
sudo apt-get update
#Clear le terminal pour plus de visibilité pour l'utilisateur
clear
#Nous prévenons l'utilisateur que l'installation des packages va démarrer
echo "Installing base packages"
# Cette ligne nous permettra d'installer git,git extra et python 3 avec les pip
sudo apt-get install --yes git git-extras python3-pip
# L'utilisateur est prévenu que maintenant nous installerons Discord
echo "Installing Discord"
# Ligne qui permet d'installer Discord
sudo snap install discord
# L'utilisateur est prévenu que maintenant nous installerons Visual studio code
echo "Installing Visual studio code "
# Ligne qui permet d'installer Visual code studio
sudo snap install code 
# ENJOY !!!
echo " All good, enjoy ! "
