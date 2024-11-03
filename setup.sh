#!/bin/bash

sudo apt update -y

sudo apt install -y python3-pip

pip install jupyter
pip install nbstripout
pip install nbimporter

pip install pandas==2.0.3
pip install scikit-learn==1.3.2
pip install imbalanced-learn==0.12.4
pip install matplotlib==3.7.5
pip install seaborn==0.13.2

# Add local bin to PATH in .bashrc if not already present
if ! grep -q 'export PATH=$PATH:~/.local/bin' ~/.bashrc; then
    echo 'export PATH=$PATH:~/.local/bin' >> ~/.bashrc
fi

# Export PATH for the current session
export PATH=$PATH:/home/ubuntu/.local/bin

if [ ! -d "output" ]; then
    mkdir output
fi

# Activate nbstripout in the current Git repository
if [ -d .git ]; then
    nbstripout --install
else
    echo "No Git repository found. Please run this script in a Git repository to activate nbstripout."
fi
