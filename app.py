from flask import Flask, render_template, redirect, flash
import time

app = Flask(__name__)

@app.route('/')
def index():
    # Display a notification message
    flash('Please wait for a minute. You will be redirected shortly.')
    time.sleep(60)  # Simulate a one-minute wait

    # Redirect to the desired website after the wait
    return redirect("https://trustedge.com/", code = 302)

if __name__ == '__main__':
    app.run(debug=True)

