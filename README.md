# E-Mail Author Identification

SMAI@IIIT-H (2017)

## Team

- [Kritika Prakash]()
- [Aditya Srivastava](https://github.com/IamAdiSri)
- [Karthik Chintapalli]()
- [Vighnesh Chenthil Kumar]()

**Course Instructor**
- Dr. Vineeth Gandhi

**Project Mentor**
- Ishit Mehta

## Table of Contents
- [Overview](https://github.com/IamAdiSri/smai-proj#Overview)
- [Method](https://github.com/IamAdiSri/smai-proj#Method)
- [Dependencies](https://github.com/IamAdiSri/smai-proj#Dependencies)
- [Modules](https://github.com/IamAdiSri/smai-proj#Modules)
    - [Dataset](https://github.com/IamAdiSri/smai-proj#Dataset)
    - [Data Cleaning and Preprocessing](https://github.com/IamAdiSri/smai-proj#Data-Cleaning_and-Preprocessing)
    - [Feature Extraction](https://github.com/IamAdiSri/smai-proj#Feature-Extraction)
    - [Data Modeling](https://github.com/IamAdiSri/smai-proj#Data-Modeling)
- [Results, Observations and Analyses](https://github.com/IamAdiSri/smai-proj#Results-Observations-and-Analyses)
- [References](https://github.com/IamAdiSri/smai-proj#References)

## Overview

Classify emails from the [**ENRON email dataset**]() based on their predicted authorship, and used the trained classifier to identify authors of test samples.

## Method

// Explain method here, without referencing the code

## Dependencies
1. [python2](https://python.org)
2. [numpy](https://numpy.org)
3. [cPickle](https://docs.python.org/2.2/lib/module-cPickle.html)
4. [keras](https://keras.io)
5. [tensorflow](https://tensorflow.org)
6. [nltk](https://nltk.org)
7. [MySQL](https://mysql.com) and [MySQLdb](https://pypi.python.org/pypi/MySQL-python)

## Project Structure
    root/

        | data_preprocessing_scripts/
            - dataProcessing.py

        | extracted_features/
            - adjperemail.txt
            - avgsentlenperemail.txt
            - avgwordlenperemail.txt
            - charsperemail.txt
            - funcwordsperemail.txt
            - perpronperemail.txt
            - stylometricVector.txt
            - uniqbytotperemail.txt
            - wordsperemail.txt

        | feature_extraction_scripts/
            - adjperemail.py
            - avgsentlenperemail.py
            - avgwordlenperemail.py
            - charsperemail.py
            - funcwordsperemail.py
            - perpronperemail.py
            - stylometricVector.py
            - uniqbytotperemail.py
            - wordsperemail.py

        | models/
            - CNN.py
            - GRU_final.py

        - README.md

## Modules

// Explain code here

### Dataset
### Data Cleaning and Preprocessing
### Feature Extraction
### Data Modeling

## Results, Observations and Analyses

// Explain results and accuracies here

## References
https://arxiv.org/pdf/1609.06686.pdf

http://www.aclweb.org/anthology/E17-2106
