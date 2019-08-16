from flask import Flask
from flask import render_template
from textblob import TextBlob
app = Flask(__name__)

@app.route("/")
def hello():
  return render_template('index.html')

if __name__ == '__main__':
    app.run()
