from flask import Flask, redirect

app = Flask(__name__)

@app.route('/')
def hello():
    return redirect("https://trustedge.com/", code = 302)

if __name__ == "__main__":
    app.run()
