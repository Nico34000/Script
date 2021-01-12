#!/bin/bash
echo "UBUNTU POST-INSTALL SCRIPT"
echo "Updating APT..."
sudo apt-get update
clear
echo "Installing base packages"
sudo apt-get install --yes git git-extras build essential python3-pip
echo "Installing Discord"
sudo snap install discord
echo "Installing Visual studio code "
sudo snap install code 
echo " Bien joué mec ! "
