# DSA4262 Team Geneiuses

# Table of Contents

- [1. Introduction](#introduction)
- [2. Run pipeline](#run-pipeline)
- [3. Developer notes](#developer-notes)

# Introduction

# Run pipeline

## 0. Prerequisite: set up
1. Start AWS EC2 machine
    - Instance type: t3.large
  
2. Connect to that instance on terminal
```
$ ssh -i <path to pem file> ubuntu@<instance ip address>
```

3. Close the repository from GitHub
```
$ git clone https://github.com/chloetkl/dsa4262-geneiuses.git
```

4. Run set_up.sh
```
$ cd dsa4262-geneiuses
$ ./setup.sh
```

## 1. Run trained model on test data
1. Folder structure
   ```
     - /data
       - test_data.json
     - /code
       - run_model.py
     - /output
       - (test_data.csv)
   ```

3. Run script `run_model.py`. Arguments:
    - json_gz_file (required)
        - Description: Path to the input JSON GZ file containing data for model predictions. Accepted formats: .json, .json.gz
        - Example: --json_gz_file ../data/dataset0.json.gz
    - selector (optional, default='../model/selector.joblib.gz')
        - Description: Path to the selector file, which performs feature selection.
    - classifier (optional, default='../model/rf_classifier.joblib.gz')
        - Description: Path to the classifier file. This is the main model file (e.g., a trained random forest classifier) that will perform predictions.
    - output_path (optional, default='default')
        - Description: Specifies the path where the output should be saved.
        - If not stated, name follows json_gz_file e.g. Output path of ../data/dataset0.json.gz is ../output/dataset0.csv
    - include_features (optional, default=False)
        - Description: Allows specifying if additional features should be included in the output.
```
# Example script to run on test_data.json
$ cd code
$ python3 run_model.py --json_gz_file '../data/test_data.json' # insert relative path to test data from code
$ head ../output/test_data.csv # copy output path here to see format of output
```

## 2. Generate new training model on new train data and labels
1. Directory structure
```
- /data
    - (add training features here, e.g. dataset0.json.gz, see section on Jupyter notebook to add data easily)
    - (add training labels here, e.g. data.info.labelled)
- /code
    - get_model.py
- /model
    - (model output will be found here, e.g. test_output.joblib)
```
2. Run get_model.py. Arguments:
- training_data_json: training features path (.json or .json.gz)
- labels: labels path
- output_joblib_path: path for model to be saved (.joblib)
```
python3 get_model.py --training_data_json '../data/test_data.json' --labels '../data/data.info.labelled' --output_joblib_path '../model/test_model.joblib'
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
