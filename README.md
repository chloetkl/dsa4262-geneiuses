# dsa4262-geneiuses

# Jupyter Instructions 

## Installing Jupyter within an EC2 Instance 
`sudo apt update
sudo apt install python3-pip
pip install jupyter`

### Write Jupyter to PATH
`nano ~/.bashrc
export PATH=$PATH:/home/ubuntu/.local/bin # Add this line`

## Running Jupyter
`source ~/.bashrc
cd dsa4262-geneiuses
jupyter notebook --no-browser --port=8082
`
Note output link, e.g. http://localhost:8082/tree?token=aecbcd503d165a09944e8939e5d3b2a8dc719b2ec1477c78

On a separate terminal, run
`ssh -NL 8082:127.0.0.1:8082 ubuntu@<EC2 IP address> -i <Key Pair Path>`