from flask import Flask
from flask import request
from flask import render_template
import run

app = Flask(__name__)

@app.route('/')
def my_form():
    return render_template("index.html")

@app.route('/', methods=['GET','POST'])
def my_form_post():
    text = request.form['text']
    output, percentage = run.NB_Classifier(text)
    return render_template("index.html", output=output,percentage=percentage )


if __name__ == '__main__':
    app.run()