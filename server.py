from flask import Flask, render_template

from os.path import isfile
from os import getcwd


app = Flask("milin")
app.debug= True

@app.route("/")
def home():
   return render_template('index.html')

if __name__ == '__main__':
    app.run(host="127.0.0.2")
