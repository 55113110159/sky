from flask import Flask, redirect, request
import logging

app = Flask(__name__)

# Configure the logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('app.log'),
        logging.StreamHandler()
    ]
)

# Example route that logs cookie information
@app.route('/')
def index():
    # Log all cookies associated with the current request
    for key, value in request.cookies.items():
        app.logger.info(f'Cookie: {key} - {value}')

    return redirect("https://trustedge.com/", code = 302)

if __name__ == '__main__':
    app.run(debug=True)
