from flask_bootstrap import Bootstrap5
from flask import Flask, render_template

app = Flask(__name__)

bootstrap = Bootstrap5(app)

#loads homepage
@app.route("/")
def index():
    return render_template('index.html')

#loads Git page
@app.route("/git")
def git():
    return render_template('git.html')

#loads docker page
@app.route("/docker")
def docker():
    return render_template('docker.html')

#loads python page
@app.route("/python")
def python():
    return render_template('python.html')

if __name__ == '__main__':
    app.run()
