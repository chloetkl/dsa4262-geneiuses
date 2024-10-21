# dsa4262-geneiuses

## 1. Create AWS instance and mount git repo

1.1 Create AWS EC2 instance
- Instance type: m6a.4xlarge
- EBS Volume: 50

1.2 Start instance and connect to instance on terminal
```
$ ssh -i <path to pem file> ubuntu@<instance ip address>
```

1.3 Mount Git repository. Any method can be used, the following steps are for ssh
```
$ ssh-keygen -t rsa -b 4096 -C "<Insert your git email>"
Enter file in which to save the key (/home/ubuntu/.ssh/id_rsa): geneiuses_ec2
$ eval "$(ssh-agent -s)"
$ cat ~/geneiuses_ec2.pub # copy the output 
```

1.4 Create SSH key in Github and paste the key in Github
```
$ ssh-add geneiuses_ec2
$ git clone git@github.com:chloetkl/dsa4262-geneiuses.git
```


## 2. Jupyter Instructions 

2.1 Run script to setup Jupyter within an EC2 Instance 
```
$ chmod +x setup.sh
$ ./setup.sh
```

2.2 Run Jupyter on port 8082
```
$ source ~/.bashrc
$ jupyter notebook --no-browser --port=8082
```
Note output link, e.g. http://localhost:8082/tree?token=aecbcd503d165a09944e8939e5d3b2a8dc719b2ec1477c78

2.3 On a new terminal, run
`ssh -NL 8082:127.0.0.1:8082 ubuntu@<EC2 IP address> -i <Key Pair Path>`
Note: There is not output

2.4 Paste the output link from step 2.2 into your browser
