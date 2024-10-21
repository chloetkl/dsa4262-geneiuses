#!/bin/bash

# Update system packages
sudo apt update -y

# Install pip for Python 3
sudo apt install -y python3-pip

# Install Jupyter Notebook
pip install jupyter

# Add Jupyter to PATH in .bashrc if not already present
if ! grep -q 'export PATH=$PATH:/home/ubuntu/.local/bin' ~/.bashrc; then
    echo 'export PATH=$PATH:/home/ubuntu/.local/bin' >> ~/.bashrc
fi

# Reload .bashrc to apply PATH changes
source ~/.bashrc
