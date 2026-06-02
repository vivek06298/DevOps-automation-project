from flask import Flask, jsonify
from datetime import datetime
import logging
import os

app = Flask(__name__)

LOG_DIR = "logs"
LOG_FILE = os.path.join(LOG_DIR, "app.log")

os.makedirs(LOG_DIR, exist_ok=True)

logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

@app.route("/")
def home():
    logging.info("Home endpoint was accessed")
    return jsonify({
        "message": "DevOps Automation Project is running perfectly now on server"
    }), 200

@app.route("/health")
def health():
    logging.info("Health endpoint check passed")
    return jsonify({
        "status": "healthy",
        "timestamp": datetime.utcnow().isoformat() + "Z"
    }), 200

if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))
    logging.info("Starting Flask application on port %s", port)
    app.run(host="0.0.0.0", port=port)