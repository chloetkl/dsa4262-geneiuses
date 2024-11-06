# DSA4262 Team Geneiuses

![](image/cover.png)

### Contents

- [1. Introduction](#1-introduction)
- [2. Run Pipeline](#2-run-pipeline)
- [3. Repository structure](#3-repository-structure)
- [4. Developer notes](#3-developer-notes)
- [5. References](#4-references)


# 1 Introduction

## Background
m6A RNA modifications are one of the most common and important chemical changes that occur on RNA molecules (Hong et al., 2022). These modifications can influence various aspects of RNA function, including its stability, how it is processed, and how it translates into proteins. They also play a critical role in cancer and understanding where and how these modifications happen can potentially uncover targets for early diagnosis and treatment of cancers (Sun et al., 2019).

## Problem Statement
In this project, we aim to identify m6A modifications in RNA sequences by analyzing direct RNA sequencing data from different human cell lines. The data comes from the SG-NEx project, which includes RNA samples from cell types such as lung (A549), colon (Hct116), liver (HepG2), blood (K562), and breast (MCF7). Studying m6A modifications in such cancer cell lines can provide valuable insights into the behavior of cancer cells and the mechanisms underlying cancer progression. Using machine learning, we hope to develop a method to predict where m6A modifications occur and analyze their patterns across these cell lines. This project provides an opportunity to combine data science and biology, using computational tools to uncover the hidden patterns of RNA modifications and contribute to a deeper understanding of gene regulation and expression in different cellular contexts.
2 Problem statement
We have divided our research problem into two parts. Task 1 explores how we can predict the modification of m6A at each transcript position using nanopore sequencing data. Task 2 investigates which features are correlated with m6A modifications among cell lines from the SG-Nex project and examines how m6A modifications differ across these cell lines.


# 2 Run pipeline

## 2.0 Prerequisite: set up
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

4. Run setup.sh
```
$ cd dsa4262-geneiuses
$ ./setup.sh
```

## 2.1 Run trained model on test data
1. Folder structure is shown below. **Add your test data**, like `test_data.json` to `/data `
   ```
     - /data
       - test_data.json
     - /code
       - run_model.py
     - /output
       - (test_data.csv)
   ```

3. Run script `run_model.py`.

| Argument           | Example / Default                                                                                      | Description                                                                                                                                          |
|--------------------|--------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------|
| `json_gz_file`     | (Required) Example: `--json_gz_file ../data/dataset0.json.gz`                                          | Path to the input JSON GZ file containing data for model predictions. Accepted formats: `.json`, `.json.gz`                                         |
| `selector`         | (Optional) Default: `'../model/selector.joblib.gz'`                                                    | Path to the selector file, which performs feature selection.                                                                              |
| `classifier`       | (Optional) Default: `'../model/rf_classifier.joblib.gz'`                                               | Path to the classifier file. This is the main model file (e.g., a trained random forest classifier) that will perform predictions.        |
| `output_path`      | (Optional) Default: `'default'`                                                                        | Specifies the path where the output should be saved. If not stated, the output name follows `json_gz_file` (e.g., `../output/dataset0.csv`). |
| `include_features` | (Optional) Default: `False`                                                                            | Allows specifying if additional features should be included in the output.                                                                |

Example script to run on test_data.json
```
$ cd code
$ python3 run_model.py --json_gz_file '../data/test_data.json' # insert relative path to test data from code
$ head ../output/test_data.csv # copy output path here to see format of output
```

## 2.2 Generate new training model on new train data and labels
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
| Argument           | Example / Default                                                                                      | Description                                                                                                                                          |
|--------------------|--------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------|
| `training_data_json` | (Required) Example: `--training_data_json '../data/dataset0.json.gz'`                                          | Path to the input JSON GZ file containing train data for model predictions. Accepted formats: `.json`, `.json.gz`                                         |
| `labels`         | (Required) Example: `'../data/data.info.labelled'`                                                    | Path to the labels file.                                                                              |
| `output_joblib_path`       | (Required) Default: `'../model/test_model.joblib'`                                               | Path for output model to be saved.        |

```
python3 get_model.py --training_data_json '../data/test_data.json' --labels '../data/data.info.labelled' --output_joblib_path '../model/test_model.joblib'
```

# 3 Repository structure

```
dsa4262-geneiuses
├── data                                            # Store all source data: train data, test data and SG-Nex data. test.json is stored here
├── code                   
│   ├── main.ipynb                                  # Notebook with machine learning and fine tuning (Task 1)
│   ├── prediction_and_visualisation.ipynb          # Notebook with codes to generate visualisationns (Task 2)
│   ├── run_model.py                                # Runs model to predict score based on test data
│   └── get_model.py                                # Generates new model given new training data
└── model
    ├── rf_classifier.joblib.gz                     # Trained Random Forest model
    └── selector.joblib.gz                          # Feature selection model
```

# 4 Developer notes
## 4.1 Create AWS instance and mount git repo

1. Create AWS EC2 instance
- Instance type: m6a.4xlarge
- EBS Volume: 50

2. Start instance and connect to instance on terminal
```
$ ssh -i <path to pem file> ubuntu@<instance ip address>
```

3. Mount Git repository. Any method can be used, the following steps are for ssh
```
$ ssh-keygen -t rsa -b 4096 -C "<Insert your git email>"
Enter file in which to save the key (/home/ubuntu/.ssh/id_rsa): geneiuses_ec2
```
When prompted for passphrase, you may leave it blank.
```
$ cat ~/geneiuses_ec2.pub # copy the output 
```

4. Create SSH key in Github and paste the key in Github
```
$ eval "$(ssh-agent -s)"
$ ssh-add geneiuses_ec2
$ git clone git@github.com:chloetkl/dsa4262-geneiuses.git
```


## 4.2 Jupyter Instructions 

1. Run script to setup Jupyter within an EC2 Instance 
```
$ cd dsa4262-geneiuses
$ chmod +x setup.sh
$ ./setup.sh
```

2. Run Jupyter on port 8082
```
$ source ~/.bashrc
$ jupyter notebook --no-browser --port=8082
```
Copy either of the output links that are shown in the terminal under "Or copy and paste one of these URLs:". For example,
```
    Or copy and paste one of these URLs:
        http://localhost:8082/tree?token=0a9aaf83afb4ff8761a3bf142ee7be9bf70b4e1431f779ee                                                                                http://127.0.0.1:8082/tree?token=0a9aaf83afb4ff8761a3bf142ee7be9bf70b4e1431f779ee
```

3. On a new terminal, run
`ssh -NL 8082:127.0.0.1:8082 ubuntu@<EC2 IP address> -i <Key Pair Path>`
Note: There is no output

4. Paste the output link from step 2.2 into your browser


# 5 References

- The SG-NEx data was accessed on [01-11-2024] at registry.opendata.aws/sg-nex-data.
- Chen, Y. et al. "A systematic benchmark of Nanopore long read RNA sequencing for transcript level analysis in human cell lines." bioRxiv (2021). doi: https://doi.org/10.1101/2021.04.21.440736
- Hong, J., Xu, K. & Lee, J.H. Biological roles of the RNA m6A modification and its implications in cancer. Exp Mol Med 54, 1822–1832 (2022). https://doi.org/10.1038/s12276-022-00897-8
- Sun, T., Wu, R., & Ming, L. (2019). The role of m6A RNA methylation in cancer. Biomedicine & Pharmacotherapy, 112, 108613. https://doi.org/10.1016/j.biopha.2019.108613

