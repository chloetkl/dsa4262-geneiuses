#!/bin/bash

sudo apt update -y

sudo apt install -y python3-pip

pip install jupyter
pip install nbstripout

# Add local bin to PATH in .bashrc if not already present
if ! grep -q 'export PATH=$PATH:~/.local/bin' ~/.bashrc; then
    echo 'export PATH=$PATH:~/.local/bin' >> ~/.bashrc
fi

# Export PATH for the current session
export PATH=$PATH:/home/ubuntu/.local/bin

# Activate nbstripout in the current Git repository
if [ -d .git ]; then
    nbstripout --install
else
    echo "No Git repository found. Please run this script in a Git repository to activate nbstripout."
fi
