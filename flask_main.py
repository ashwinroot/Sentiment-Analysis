from flask import Flask
from flask import request
from flask import render_template
import Sentiment_Classifier

app = Flask(__name__)

@app.route('/')
def my_form():
    Sentiment_Classifier.train()
    return render_template("index.html")

@app.route('/', methods=['GET','POST'])
def my_form_post():
    text = request.form['text']

    my_output = Sentiment_Classifier.NB_Classifier(text)
    nb_output = Sentiment_Classifier.NLTK_NB(text)
    return render_template("index.html", my_output=my_output,nb_output=nb_output )


if __name__ == '__main__':
    app.run()