from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello web service Domestic Bank Group'

if __name__ == '__main__':
    app.run()
