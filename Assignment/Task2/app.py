from flask import Flask, request
import logging

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__, static_folder='.', static_url_path='')

@app.route('/')
def home():
    try:
        with open('index.html', 'r') as f:
            logger.info("Successfully loaded index.html")
            return f.read()
    except FileNotFoundError:
        logger.error("index.html not found")
        return "Error: index.html not found", 404
    except Exception as e:
        logger.error(f"Error loading page: {str(e)}")
        return f"Error: {str(e)}", 500

@app.before_request
def log_request():
    logger.info(f"Request: {request.method} {request.path}")

if __name__ == '__main__':
    logger.info("Starting Flask app on port 5002")
    app.run(debug=True, host='0.0.0.0', port=5002)