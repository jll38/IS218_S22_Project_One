from flask_bootstrap import Bootstrap5
from flask import Flask, render_template

app = Flask(__name__)

bootstrap = Bootstrap5(app)

@app.route("/")
def index():
    return render_template('index.html')
@app.route("/git")
def git():
    return render_template('git.html')
@app.route("/docker")
def docker():
    return render_template('docker.html')
@app.route("/python")
def python():
    return render_template('python.html')
if __name__ == '__main__':
    app.run()
