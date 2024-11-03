# DSA4262 Team Geneiuses

# Table of Contents

- [1. Introduction](#introduction)
- [2. Run pipeline](#run-pipeline)
- [3. Developer notes](#developer-notes)

# 1. Introduction

# 2, Run pipeline

```
$ cd code
$ python3 run_model.py --json_gz_file '../data/test_data.json'
```

# Developer notes
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
```
When prompted for passphrase, you may leave it blank.
```
$ cat ~/geneiuses_ec2.pub # copy the output 
```

1.4 Create SSH key in Github and paste the key in Github
```
$ eval "$(ssh-agent -s)"
$ ssh-add geneiuses_ec2
$ git clone git@github.com:chloetkl/dsa4262-geneiuses.git
```


## 2. Jupyter Instructions 

2.1 Run script to setup Jupyter within an EC2 Instance 
```
$ cd dsa4262-geneiuses
$ chmod +x setup.sh
$ ./setup.sh
```

2.2 Run Jupyter on port 8082
```
$ source ~/.bashrc
$ jupyter notebook --no-browser --port=8082
```
Copy either of the output links that are shown in the terminal under "Or copy and paste one of these URLs:". For example,
```
    Or copy and paste one of these URLs:
        http://localhost:8082/tree?token=0a9aaf83afb4ff8761a3bf142ee7be9bf70b4e1431f779ee                                                                                http://127.0.0.1:8082/tree?token=0a9aaf83afb4ff8761a3bf142ee7be9bf70b4e1431f779ee 

2.3 On a new terminal, run
`ssh -NL 8082:127.0.0.1:8082 ubuntu@<EC2 IP address> -i <Key Pair Path>`
Note: There is no output

2.4 Paste the output link from step 2.2 into your browser
