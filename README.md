# E-Mail Author Identification

SMAI@IIIT-H (Monsoon 2017)

## Team 15

- [Kritika Prakash (20161039)](https://github.com/Kritikalcoder)
- [Aditya Srivastava (201425112)](https://github.com/IamAdiSri)
- [Karthik Chintapalli (201501207)](https://github.com/karthikchintapalli)
- [Vighnesh Chenthil Kumar (201501201)](https://github.com/vighneshck)

**Course Instructor**
- [Dr. Vineet Gandhi](https://faculty.iiit.ac.in/~vgandhi/)

**Project Mentor**
- [Ishit Mehta](https://github.com/ishit)

## Table of Contents
- [Overview](https://github.com/IamAdiSri/smai-proj#overview)
- [Method](https://github.com/IamAdiSri/smai-proj#method)
    - [Enron Email Dataset](https://github.com/IamAdiSri/smai-proj#enron-email-dataset)
    - [Data Preparation](https://github.com/IamAdiSri/smai-proj#data-preparation)
        - [Cleaning](https://github.com/IamAdiSri/smai-proj#cleaning)
    - [Models](https://github.com/IamAdiSri/smai-proj#models)
        1. [CNN implementation](https://github.com/IamAdiSri/smai-proj#cnn-implementation)
        2. [Bi-LSTM implementation](https://github.com/IamAdiSri/smai-proj#bi-lstm-implementation)
        3. [Hierarchical Bi-LSTM implementation](https://github.com/IamAdiSri/smai-proj#hierarchical-bi-lstm-implementation)
        4. [Augmented Hierarchical Bi-LSTM implementation](https://github.com/IamAdiSri/smai-proj#augmented-hierarchical-bi-lstm-implementation)
            - [Stylometry](https://github.com/IamAdiSri/smai-proj#stylometry)
- [Dependencies](https://github.com/IamAdiSri/smai-proj#dependencies)
- [Project Structure](https://github.com/IamAdiSri/smai-proj#project-structure)
- [References](https://github.com/IamAdiSri/smai-proj#references)

## Overview

Classify emails from the [**Enron email dataset**](https://www.cs.cmu.edu/~enron/) based on their predicted authorship, and used the trained classifier to identify authors of test samples.

## Method

### Enron Email Dataset

Available [here](https://www.cs.cmu.edu/~enron/), the dataset contains **0.5 million emails** from about **150 users**, who were employees of Enron.

The classifers use the authors as classess and the emails as samples to be assigned to those classes by authorship.

### Data Preparation

The number of author classes were fixed while maximising the number of emails per author, and while keeping the emails-per-author ratio similar for every author class.

This number was found to be **10** authors with **800-1000** emails each.

#### Cleaning

The Enron corpus contains all emails in raw form, including not only the message but also all the email metadata.

The data is cleaned to keep only the **subject** and **body** of the mails. All attached *forward chains* are removed, including forwarded threads, and *salutations*.

The data is also tokenised by word, sentence and paragraph, and is case normalised.

### Models

The following different models have been implemented and tested:

#### CNN implementation

The CNN can identify commonly used groups of words and phrases by an author. Also, the CNN captures localized chunks of information which is useful for finding phrasal units within long texts.
There are **three** layers to the CNN 
- First, the **embedding layer** generates a sequence of word-embeddings from a sequence of words
- Second, the **conv layer** performs the convolution operation using **128 5x5** filter
- Third, the **dense layer** is used for classification

#### Bi-LSTM implementation

The Bi-LSTM is a commonly used technique for text classification.

LSTMs are a special kind of RNN which are more capable of remembering long term dependencies in a sequence. This gives more context to the classifier which helps in author identification while processing a sequence of text.

There are **three** layers to the model 
- First, the **embedding layer** generates a sequence of word-embeddings from a sequence of words
- Second, the **bidirectional LSTM** generates email embeddings from the sequence of word embeddings
- Third, the **dense layer** is performs the classification

#### Hierarchical Bi-LSTM implementation

LSTMs are known to work best for a sequence of length of 10-15 elements. However, in this implementation the model can take the entire document, increasing the length and hence the overall context for classification.

There are **four** layers to this model 
- First, the **embedding layer** generates a sequence of word-embeddings from a sequence of words
- Second, the **first bidirectional LSTM** generates sentence embeddings from the sequence of word embeddings
- Third **second bidirectional LSTM** generates email embeddings from sentence embeddings
- Fourth, the **dense layer** is performs the classification

#### Augmented Hierarchical Bi-LSTM implementation

This model appends **stylometric features** to the final document embedding in the hierarchical Bi-LSTM, right before it is passed on to the dense layer. The classification is now performed these augmented documenting-embeddings.

##### Stylometry
The **stylometric features** extracted from the data and experimented with are
- **Lexical**
    1. Average sentence length
    2. Average word length
    3. total number of words
    4. Ratio of unique words to total number of words
    5. Total number of characters
- **Syntactic**
    1. Total number of function words
    2. Total number of personal pronouns
    3. Total number of adjectives

## Dependencies
1. [python2](https://python.org)
2. [numpy](https://numpy.org)
3. [cPickle](https://docs.python.org/2.2/lib/module-cPickle.html)
4. [keras](https://keras.io)
5. [tensorflow](https://tensorflow.org)
6. [nltk](https://nltk.org)
7. [MySQL](https://mysql.com) and [mysqldb](https://pypi.python.org/pypi/MySQL-python)

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
            - HierLSTM_withStylometry.py
            - HierLSTM.py
            - LSTM_final.py

        - README.md

## References
- [*CEAI: CCM-based email authorship identification model* - Serwat Nizamani, Nasrullah](https://www.sciencedirect.com/science/article/pii/S111086651300039X)

- [*Writeprints: A stylometric approach to identity-level identification and similarity detection in cyberspace* - Ahmed Abbasi, Hsinchun Chen](https://dl.acm.org/citation.cfm?id=1344413)

- [*Detection of Fraudulent Emails by Authorship Extraction* - A. Pandian, Mohamed Abdul Karim](http://research.ijcaonline.org/volume41/number7/pxc3877619.pdf)