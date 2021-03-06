#Julian Lechner IS218
from flask import Flask, render_template
from flask_bootstrap import Bootstrap5
from context_processors import utility_text_processors

app = Flask(__name__)

bootstrap = Bootstrap5(app)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
app.context_processor(utility_text_processors)

#loads homepage test
@app.route("/")
def create_app():
    with app.app_context(), app.test_request_context():
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
@app.route("/cicd")
def cicd():
    return render_template('CICD.html')

if __name__ == '__main__':
    app.run()
