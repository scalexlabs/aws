# aws-rds-automation
Automatic aws-rds instance start and shutdown using aws-lambda.

### Getting Started
This project is built using Python(v2.7) as backend. This project is implemented for demonstration purpose and tutorial of Automatic AWS RDS instance start and shutdown using AWS lambda. 

## Contents
* Introduction
* Requirements/Setup
* Deployment
* Authors

### Introduction
This project is built using Python(v2.7) as backend. This project is implemented for demonstration purpose and tutorial of Automatic AWS RDS instance start and shutdown using AWS lambda service.  
This project includes an aim to automate the start and stop of RDS instance running over the AWS. This is achieved by using the python libraries such as Chalice(v1.0.2) and Boto3(v1.4.7).

### Setup
1. Install and Setup Python
    [Python](https://www.ics.uci.edu/~pattis/common/handouts/pythoneclipsejava/python.html)

2. Install pip 
    a.  Download the last pip version from here: http://pypi.python.org/pypi/pip#downloads
    b.  Uncompress it
    c.  Download the last easy installer for Windows: (download the .exe at http://pypi.python.org/pypi/setuptools)
    d.  Install it.
    e.  copy the uncompressed pip folder content into C:\Python2x\ folder (don't copy the whole folder into it just     the content), because python command doesn't work outside C:\Python2x folder and then run: 
        python setup.py install
    f.  Add your python C:\Python2x\Scripts to the path
    g.  You are done.
    (Now you can use pip install package to easily install packages)

3.  Install chalice pacakages for python using pip command
    [chalice install](https://chalice.readthedocs.io/en/latest/)
    ```bash
    pip install chalice
    ```

4.  Install Boto3 pacakages for python using pip command
    [Boto3 install](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html)
    ```bash
    pip install boto3
    ```

5. Ensure packages are installed.
    ```bash
    pip freeze
    ```

6. Set up the AWS Credentials
    [Configuring the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html)
    ```bash
    serverless config credentials --provider aws --key <AWSAccessKeyId> --secret <AWSSecretKey>
    ```

7. Set up AWS RDS Instance 
    [Setup RDS Instance](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_Tutorials.WebServerDB.CreateDBInstance.html)


8. Make desired changes in config.json for connection your RDS instance and save the file
    "RDS_REGION" :"<region-name>",
    "RDS_INSTANCE_NAME" : "<instance-name>"



### Deployment
Use following command for depoyment.
```bash
chalice deploy
```
        

### Authors
@scalexlabs