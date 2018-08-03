from flask import Flask, render_template
from doc2vec import *
import sys

app = Flask(__name__)

@app.route("/")
def articles():
    """Show a list of article titles"""
    article_list = []
    for a in articles:
        title = a[1]
        url = "/article/"+a[0]
        article_list.append({"title":title, "url":url})
    return render_template('articles.html', articles=article_list)

@app.route("/article/<topic>/<filename>")
def article(topic,filename):
    """
    Show an article with relative path filename. Assumes the BBC structure of
    topic/filename.txt so our URLs follow that.
    """
    for a in articles:
        if a[0] == "%s/%s"%(topic, filename):
            curr_article = a
            break
    if curr_article:
        title = curr_article[1]
        text = curr_article[2]
        recommend_list = recommended(curr_article, articles, 5)
        recommend = list()
        for r in recommend_list:
            title = r[1]
            url = "/article/"+r[0]
            recommend.append({'title': title, 'url': url})
        return render_template('article.html', recommend=recommend, text=text.replace('\n', '<br />'), title = title)
    return "Page not found", 404





i = sys.argv.index('server:app')
glove_filename = sys.argv[i+1]
articles_dirname = sys.argv[i+2]

gloves = load_glove(glove_filename)
articles = load_articles(articles_dirname, gloves)
