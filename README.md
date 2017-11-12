# smai-proj

## Requirements
1. python3
2. numpy
3. cPickle # use `pickle` instead as default pickle in python3 is cPickle and does not require a separate installation of the library
4. keras
5. tensorflow

## Lexical features

1. chars per e-mail
2. digits to total chars. ratio
3. ratio of spaces to total chars. | avg length of word
4. normalized freq. of special characters(commas and semi-colons)
5. words per email
6. avg. sentence length per email
7. unique words/total words per email

## Syntactic features

1. freq of function words
2. freq of punctuation
3. freq. of personal pronouns and adjective.

## Structural features

1. ratio of no. of paras to length of email in words.
2. avg no. of sentences per paragraph.

## Content features:
1. 

## Reference papers
https://arxiv.org/pdf/1609.06686.pdf

http://www.aclweb.org/anthology/E17-2106
