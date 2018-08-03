## Project Introduction
The goal of this project is to learn how to make a simple article recommendation engine using a semi-recent advance 
in natural language processing called **word2vec** (or just word vectors). In particular, we're going to use a "database" from **Stanford's GloVe project** trained on a dump of Wikipedia. The project involves reading in a database of word vectors and a corpus of text articles then organizing them into a handy table (list of lists) for processing.

## How it works
To deploy the recommendation engine, I built a web server that displays a list of BBC articles. Once you click on an article title it will direct you to the text body of that article and recommend similar articles to read.

Check it out here: http://54.202.239.183:5000/



