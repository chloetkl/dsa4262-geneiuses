#!/bin/bash

sudo apt update -y

sudo apt install -y python3-pip

pip install jupyter
pip install nbstripout

# Add Jupyter to PATH in .bashrc if not already present
if ! grep -q 'export PATH=$PATH:/home/ubuntu/.local/bin' ~/.bashrc; then
    echo 'export PATH=$PATH:/home/ubuntu/.local/bin' >> ~/.bashrc
fi

# Reload .bashrc to apply PATH changes
source ~/.bashrc

# Activate nbstripout in the current Git repository
if [ -d .git ]; then
    nbstripout --install
else
    echo "No Git repository found. Please run this script in a Git repository to activate nbstripout."
fi
