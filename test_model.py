import torch
from train_model import GenreClassificationCNN, audio_to_melspectrogram  # Import necessary components from train_model.py

# Define genre mapping (same as in your training code)
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


def load_model(model_path, num_classes=10):
    # Initialize the model and load the trained weights
    model = GenreClassificationCNN(num_classes=num_classes)
    model.load_state_dict(torch.load(model_path))
    model.eval()  # Set model to evaluation mode
    return model


def preprocess_audio(file_path):
    # Convert audio to a Mel spectrogram and resize to model's input size
    spectrogram = audio_to_melspectrogram(file_path)
    if spectrogram is None:
        print("Error: Unable to process the audio file.")
        return None

    # Convert to torch tensor and add batch and channel dimensions
    spectrogram = torch.tensor(spectrogram, dtype=torch.float32).unsqueeze(0).unsqueeze(0)
    spectrogram = torch.nn.functional.interpolate(spectrogram, size=(64, 64))
    return spectrogram


def predict_top_genres(model, spectrogram, top_k=10):
    # Run the model to get the prediction
    with torch.no_grad():  # Disable gradient calculation for inference
        output = model(spectrogram)
        probabilities = torch.exp(output)  # Convert log-softmax output to probabilities
        top_p, top_classes = probabilities.topk(top_k, dim=1)  # Get top-k predictions

        # Prepare top genres and confidence scores as a list of tuples
        top_genres = [(genre_to_label[class_idx.item()], confidence.item()) for class_idx, confidence in zip(top_classes[0], top_p[0])]
        return top_genres


# Main function to load model, process audio, and predict genre
if __name__ == "__main__":
    model_path = "genre_classification_cnn.pth"  # Path to the saved model
    audio_path = "INSERT PATH TO AUIDO FILE HERE"  # Path to the audio file to test

    # Load the model
    model = load_model(model_path)

    # Preprocess the audio file
    spectrogram = preprocess_audio(audio_path)
    if spectrogram is not None:
        # Predict the top 10 genres
        top_genres = predict_top_genres(model, spectrogram, top_k=10)
        print("Top 10 Predicted Genres with Confidence Scores:")
        for genre, confidence in top_genres:
            print(f"{genre}: {confidence:.2f}")
