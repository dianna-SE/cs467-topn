import requests

# Define the URL for the Flask endpoint
url = "http://127.0.0.1:5000/predict"

# Path to the audio file you want to test
audio_file_path = "dance_song.wav"

# Send a POST request with the audio file
with open(audio_file_path, "rb") as audio_file:
    files = {"file": audio_file}
    response = requests.post(url, files=files)

# Print the response from the server
if response.status_code == 200:
    print("Top 10 Predicted Genres with Confidence Scores:")
    for genre, confidence in response.json().get("top_genres", []):
        print(f"{genre}: {confidence:.2f}")
else:
    print("Error:", response.json())
