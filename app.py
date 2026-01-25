from flask import Flask, jsonify, render_template, request
import os
from flask_cors import CORS, cross_origin
from src.cnnClassifier.utils.common import decodeImage
from src.cnnClassifier.pipeline.predict import PredictionPipeline

os.putenv('LANG', 'en_US.UTF-8')
os.putenv('LC_ALL', 'en_US.UTF-8')

app = Flask(__name__)
CORS(app)

class ClientApp:
    def __init__(self):
        self.filename = "inputimage.jpg"
        self.classifier = PredictionPipeline(self.filename)

@app.route("/", methods=['GET'])
@cross_origin()
def home():
    return render_template('index.html')

@app.route("/train", methods=['GET', 'POST'])
@cross_origin()
def trainRoute():
    # Disable training in production for security and resource management
    if os.environ.get('RENDER'):  # Check if running on Render
        return jsonify({"error": "Training is disabled in production"}), 403
    
    os.system("python main.py")
    return "Training done successfully"

@app.route("/predict", methods=['POST'])
@cross_origin()
def predictRoute():
    try:
        image = request.json['image']
        decodeImage(image, clApp.filename)
        result = clApp.classifier.predict()
        return jsonify(result)
    except KeyError:
        return jsonify({"error": "No image data provided"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/health", methods=['GET'])
@cross_origin()
def health_check():
    """Health check endpoint for monitoring"""
    return jsonify({"status": "healthy", "service": "Fruit Freshness Classifier"}), 200

clApp = ClientApp()
if __name__ == "__main__":
    
    
    # Get port from environment variable (Render will set this)
    port = int(os.environ.get('PORT', 8080))
    
    # Determine if in production
    debug_mode = os.environ.get('FLASK_ENV') != 'production'
    
    app.run(
        host='0.0.0.0', 
        port=port, 
        debug=debug_mode  # False in production, True locally
    )