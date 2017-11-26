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
- [Overview]()
- [Dependencies]()
- [Modules]()
    - [Dataset]()
    - [Data Cleaning and Preprocessing]()
    - [Feature Extraction]()
    - [Data Modeling]()
- [Results, Observations and Analyses]()
- [References]()

## Overview

Classify emails from the [**ENRON email dataset**]() based on their predicted authorship, and used the trained classifier to identify authors of test samples.

## Dependencies
1. [python2]()
2. [numpy]()
3. [cPickle]()
4. [keras]()
5. [tensorflow]()
6. [nltk]()
7. [MySQL]() and [MySQLdb]()

## Project Structure
    root/
        | data_preprocessing_scripts/
            | dataProcessing.py
        | extracted_features/
            | adjperemail.txt
            | avgsentlenperemail.txt

        | feature_extraction_scripts/
        | models/

## Modules

### Dataset
### Data Cleaning and Preprocessing
### Feature Extraction

    #### Lexical features

    1. chars per e-mail (Done)
    2. digits to total chars. ratio
    3. ratio of spaces to total chars. | avg length of word (Done)
    4. normalized freq. of special characters(commas and semi-colons)
    5. words per email (Done)
    6. avg. sentence length per email (Done)
    7. unique words/total words per email (Done)

    #### Syntactic features

    1. freq of function words (Done)
    2. freq of punctuation
    3. freq. of personal pronouns and adjective. (Done)

    #### Structural features

    1. ratio of no. of paras to length of email in words.
    2. avg no. of sentences per paragraph.

    #### Content features:
    1. 

### Data Modeling

## Results, Observations and Analyses

## References
https://arxiv.org/pdf/1609.06686.pdf

http://www.aclweb.org/anthology/E17-2106
