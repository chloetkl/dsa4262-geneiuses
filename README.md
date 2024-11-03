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
le '../data/test_data.json'
Input file is not a .gz file. Unzipping not required
Step 1/6: Processing JSON completed.
Step 2/6: Cleaning features completed.
Step 3/6: Feature selection completed.
[Parallel(n_jobs=1)]: Done  49 tasks      | elapsed:    0.0s
[Parallel(n_jobs=1)]: Done 199 tasks      | elapsed:    0.0s
[Parallel(n_jobs=1)]: Done  49 tasks      | elapsed:    0.0s
[Parallel(n_jobs=1)]: Done 199 tasks      | elapsed:    0.0s

Tabulated Prediction Counts:
   prediction  count
0           0    108
1           1     13
Step 4/6: Prediction using model completed.
     transcript_id transcript_position     score
0  ENST00000084795                 233  0.056420
1  ENST00000205636                3411  0.034202
2  ENST00000216254                1007  0.088522
3  ENST00000216968                1159  0.018773
4  ENST00000220913                 999  0.024692
Step 5/6: Cleaning results completed.
Step 6/6: Results written to ../output/test_data.csv

$ head ../output/test_data.csv # copy output path here to see format of output

```

## 2. Generate new training model on new train data and labels
```

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
