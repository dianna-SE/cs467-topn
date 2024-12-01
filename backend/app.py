from flask import Flask, request, jsonify
from flask_cors import CORS
import torch
from train_model import GenreClassificationCNN, audio_to_melspectrogram  
import os
import traceback

# Define the model
app = Flask(__name__)
# Use for development instance
CORS(app, resources={r"/*": {"origins": ["https://top-n-music-genre-classification.onrender.com", "http://localhost:3000/"]}})

# # Use for production instance
# CORS(app, resources={r"/*": {"origins": ["https://top-n-music-genre-classification.onrender.com"]}})

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
    model = GenreClassificationCNN(num_classes=num_classes)
    model.load_state_dict(torch.load(model_path, map_location="cpu"))
    model.eval()
    return model


model = load_model("genre_classification_cnn.pth")  # Adjust the path if needed


# Helper function to process audio file
def preprocess_audio(file_path):
    spectrogram = audio_to_melspectrogram(file_path)
    if spectrogram is None:
        print("Error: Unable to process the audio file.")
        return None
    spectrogram = torch.tensor(spectrogram, dtype=torch.float32).unsqueeze(0).unsqueeze(0)
    spectrogram = torch.nn.functional.interpolate(spectrogram, size=(64, 64))
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

        if request.method == 'OPTIONS':
            return '', 200

        if 'file' not in request.files:
            return jsonify({'error': 'No file uploaded'}), 400

        file = request.files['file']
        file_path = "temp_audio.wav"
        file.save(file_path)

        spectrogram = preprocess_audio(file_path)
        os.remove(file_path)  # Clean up temporary file

        if spectrogram is None:
            return jsonify({'error': 'Error processing audio file'}), 500

        top_genres = predict_top_genres(model, spectrogram, top_k=10)
        return jsonify({'top_genres': top_genres})

    except Exception as e:
        print(f"Error: {e}")
        traceback.print_exc()
        return jsonify({'error': 'Internal server error. Please check logs for more details.'}), 500


# Root Route
@app.route('/')
def root():
    return "Hello! Music Genre Classification API is up and running."


# Handle CORS for responses
@app.after_request
def after_request(response):
    origin = request.headers.get('Origin')

    # Origins for dev and prod instance
    instance_origins = ["https://top-n-music-genre-classification.onrender.com", "http://localhost:3000"]

    if origin in instance_origins:
        response.headers['Access-Control-Allow-Origin'] = origin

    # Allow specific HTTP methods and headers
    response.headers['Access-Control-Allow-Methods'] = 'GET, POST, PUT, DELETE, OPTIONS'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type, Authorization'

    return response


# Run the app in development mode
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8000)
