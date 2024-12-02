from flask import Flask, request, jsonify
from flask_cors import CORS
import torch
from train_model import GenreClassificationCNN, audio_to_melspectrogram
import os
import traceback
import logging

# Define the model
app = Flask(__name__)
CORS(app)

# Increase fto 50MB file size limit for flask
app.config['MAX_CONTENT_LENGTH'] = 50 * 1024 * 1024

# Genre labels
genre_to_label = {
    0: "blues",
    1: "classical",
    2: "country",
    3: "disco",
    4: "hiphop",
    5: "jazz",
    6: "metal",
    7: "pop",
    8: "reggae",
    9: "rock"
}


# Load the model once at startup
def load_model(model_path, num_classes=10):
    # Initialize the original model structure
    model = GenreClassificationCNN(num_classes=num_classes)

    # Apply quantization dynamically
    model = torch.quantization.quantize_dynamic(
        model,  # Model structure
        {torch.nn.Linear},  # Apply quantization to linear layers
        dtype=torch.qint8  # Use int8 quantization
    )

    try:
        # Load the state dictionary of the model
        model.load_state_dict(torch.load(model_path, map_location="cpu"))
        model.eval()  # Set the model to evaluation mode
    except Exception as e:
        print(f"Error loading model: {e}")
        return None

    return model


model = load_model("quantized_genre_classification_cnn.pth")  # Adjust the path if needed


# Helper function to process audio file
def preprocess_audio(file_path):
    # Convert audio to a Mel spectrogram
    spectrogram = audio_to_melspectrogram(file_path)
    if spectrogram is None:
        print("Error: Unable to process the audio file.")
        return None

    # Convert to torch tensor and resize to (64, 64)
    spectrogram = torch.tensor(spectrogram, dtype=torch.float32).unsqueeze(0).unsqueeze(0)  # Add batch and channel dimensions
    spectrogram = torch.nn.functional.interpolate(spectrogram, size=(64, 64), mode='bilinear', align_corners=False)
    return spectrogram


# Prediction function
def predict_top_genres(model, spectrogram, top_k=10):
    with torch.no_grad():
        output = model(spectrogram)
        probabilities = torch.exp(output)
        top_p, top_classes = probabilities.topk(top_k, dim=1)
        top_genres = [(genre_to_label[class_idx.item()], confidence.item()) for class_idx, confidence in zip(top_classes[0], top_p[0])]
        return top_genres


# API route to handle file upload and prediction
@app.route('/predict', methods=['POST'])
def predict():
    try:
        logging.debug("Request to backend success!")

        if 'file' not in request.files:
            logging.error("ERROR 400: No file in request")
            return jsonify({'error': 'No file uploaded'}), 400

        logging.info("File in the request.files!")

        file = request.files['file']
        file_path = "temp_audio.wav"
        logging.debug(f"Saving the uploaded file to file_path: {file_path}")
        file.save(file_path)

        spectrogram = preprocess_audio(file_path)
        os.remove(file_path)  # Clean up temporary file
        logging.debug("Removing temporary file")

        if spectrogram is None:
            logging.error("ERROR 500: Error processing audio file.")
            return jsonify({'error': 'Error processing audio file'}), 500

        top_genres = predict_top_genres(model, spectrogram, top_k=10)
        logging.info("Prediction is successful, top genres displayed")
        return jsonify({'top_genres': top_genres})

    except Exception as e:
        print(f"Error: {e}")
        logging.error("ERROR 500: Internal server")
        traceback.print_exc()
        return jsonify({'ERROR: Internal server.'}), 500

# Test
# @app.route('/predict', methods=['POST'])
# def predict_test():
#     return jsonify({"message": "Request was successful on Render."}), 200


# Root Route
@app.route('/')
def root():
    return "Hello! Music Genre Classification API is up and running."


# Handle CORS for responses
@app.after_request
def after_request(response):
    # origin = request.headers.get('Origin')

    # Origins for dev and prod instance
    # instance_origins = ["https://top-n-music-genre-classification.onrender.com", "http://localhost:3000"]

    # if origin in instance_origins:
    #     response.headers['Access-Control-Allow-Origin'] = origin
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'GET, POST, PUT, DELETE, OPTIONS'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type, Authorization'
    return response


# Run the app in development mode
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8000)
