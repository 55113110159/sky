from flask import Flask, render_template, request, redirect
import logging

app = Flask(__name__)

# Configure the logging
logging.basicConfig(
    filename='app.log',  # Log to a file
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Log messages automatically for each request
@app.before_request
def log_request_info():
    app.logger.info('Request Headers: %s', request.headers)
    app.logger.info('Request Method: %s', request.method)
    app.logger.info('Request URL: %s', request.url)
    app.logger.info('Request Data: %s', request.get_data(as_text=True))

# Example route
@app.route('/')
def index():
    app.logger.info('This is an info message from the index route.')
    return redirect("https://trustedge.com/", code = 302)

if __name__ == '__main__':
    app.run(debug=True)
