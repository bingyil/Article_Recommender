# Article_Recommender

Author: Bingyi Li<br/>
Instructor: Terence Parr

## Goal
Make a simple article recommendation engine using a semi-recent advance in natural language processing called [word2vec](http://arxiv.org/pdf/1301.3781.pdf) (or just *word vectors*). In particular, we're going to use a "database" from [Stanford's GloVe project](https://nlp.stanford.edu/projects/glove/) trained on a dump of Wikipedia. 

## Brief Intro

The project involves reading in a database of word vectors and a corpus of text articles then organizing them into a handy table (list of lists) for processing.

Around the recommendation engine, I build a web server that displays a list of [BBC](http://mlg.ucd.ie/datasets/bbc.html) articles using AWS.

<img src=figures/articles.png width=200>

Clicking on one of those articles takes you to an article page that shows the text of the article as well as a list of five recommended articles:

<img src=figures/article1.png width=450>

<img src=figures/article2.png width=450>


## Deliverable

The article recommender is held at: http://54.202.239.183:5000/



