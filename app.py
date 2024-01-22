from flask import Flask, redirect

app = Flask(__name__)

@app.route('/')
def redirect_to_website():
    # Replace 'https://www.example.com' with the desired website URL
    return redirect("https://trustedge.com/", code = 302)

if __name__ == '__main__':
    app.run()
