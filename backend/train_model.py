import os
import librosa
import audioread
import numpy as np
import torch
import torch.nn as nn
import torch.optim as optim
import torch.nn.functional as F
from torch.utils.data import Dataset, DataLoader


# 1. Convert audio to Mel spectrogram using librosa
def audio_to_melspectrogram(file_path, sr=22050, n_mels=64):
    try:
        # Use audioread to read the audio file
        with audioread.audio_open(file_path) as input_file:
            y = []  # Initialize an empty list to gather audio samples

            # Collect all audio buffers in the list
            for buf in input_file:
                buf_array = np.frombuffer(buf, dtype=np.int16) / 32768.0  # Convert buffer to float
                y.extend(buf_array)  # Dynamically append buffer data to y

            # Convert the list to a NumPy array for further processing
            y = np.array(y)

        # If the sample rate is different from the target, resample the audio
        if input_file.samplerate != sr:
            y = librosa.resample(y, orig_sr=input_file.samplerate, target_sr=sr)

        # Generate Mel Spectrogram
        spectrogram = librosa.feature.melspectrogram(y=y, sr=sr, n_mels=n_mels)
        spectrogram_db = librosa.power_to_db(spectrogram, ref=np.max)
        return spectrogram_db
    except Exception as e:
        print(f"Error processing {file_path}: {e}")
        return None  # In case of error, return None
    

# 2. Custom Dataset class to handle GTZAN data
class GenreDataset(Dataset):
    def __init__(self, file_paths, labels):
        self.file_paths = file_paths
        self.labels = labels

    def __len__(self):
        return len(self.file_paths)

    def __getitem__(self, idx):
        spectrogram = audio_to_melspectrogram(self.file_paths[idx])
        if spectrogram is None:
            # Return None if the file is corrupted
            return None
        
        spectrogram = torch.tensor(spectrogram, dtype=torch.float32).unsqueeze(0)  # Add channel dimension
        spectrogram = F.interpolate(spectrogram.unsqueeze(0), size=(64, 64)).squeeze(0)
        label = torch.tensor(self.labels[idx], dtype=torch.long)
        return spectrogram, label
    

# 3. CNN Model for Genre Classification
class GenreClassificationCNN(nn.Module):
    def __init__(self, num_classes=10):  # GTZAN has 10 genres
        super(GenreClassificationCNN, self).__init__()
        self.conv1 = nn.Conv2d(1, 16, kernel_size=3, stride=1, padding=1)
        self.conv2 = nn.Conv2d(16, 32, kernel_size=3, stride=1, padding=1)
        self.conv3 = nn.Conv2d(32, 64, kernel_size=3, stride=1, padding=1)
        self.pool = nn.MaxPool2d(kernel_size=2, stride=2, padding=0)
        self.fc1 = nn.Linear(64 * 8 * 8, 128)  # Can adjust based on input size
        self.fc2 = nn.Linear(128, num_classes)
        self.dropout = nn.Dropout(0.4)

    def forward(self, x):
        x = self.pool(F.relu(self.conv1(x)))
        x = self.pool(F.relu(self.conv2(x)))
        x = self.pool(F.relu(self.conv3(x)))
        x = x.view(-1, 64 * 8 * 8)  # Flatten
        x = F.relu(self.fc1(x))
        x = self.dropout(x)
        x = self.fc2(x)
        return F.log_softmax(x, dim=1)
    

# 3.5. collate added later to filter corrupted files
def collate_fn(batch):
    # Filter out corrupted files (None values)
    batch = [b for b in batch if b is not None]
    if len(batch) == 0:
        return None
    return torch.utils.data.dataloader.default_collate(batch)


# 4. Prepare GTZAN Dataset - Mapping genres to labels and loading the data
def create_dataloader(audio_dir, batch_size=32):
    genre_to_label = {
        "blues": 0,
        "classical": 1,
        "country": 2,
        "disco": 3,
        "hiphop": 4,
        "jazz": 5,
        "metal": 6,
        "pop": 7,
        "reggae": 8,
        "rock": 9
    }
    file_paths, labels = [], []
    
    # Traverse the GTZAN directories and gather file paths and labels
    for genre in genre_to_label:
        genre_folder = os.path.join(audio_dir, genre)
        for file_name in os.listdir(genre_folder):
            if file_name.endswith(".wav"):  # Only consider wav files
                file_paths.append(os.path.join(genre_folder, file_name))
                labels.append(genre_to_label[genre])

    # Create Dataset and DataLoader
    dataset = GenreDataset(file_paths, labels)
    return DataLoader(dataset, batch_size=batch_size, shuffle=True, num_workers=0, collate_fn=collate_fn)


# 5. Training loop for the model
def train_model(model, train_loader, criterion, optimizer, num_epochs=30):
    model.train()
    for epoch in range(num_epochs):
        running_loss = 0.0
        for i, data in enumerate(train_loader, 0):
            # Skip empty batches
            if data is None:
                continue
            
            inputs, labels = data

            optimizer.zero_grad()

            # Forward pass
            outputs = model(inputs)
            loss = criterion(outputs, labels)

            # Backward pass and optimization
            loss.backward()
            optimizer.step()

            running_loss += loss.item()
            if i % 100 == 99:
                print(f'Epoch [{epoch + 1}], Batch [{i + 1}], Loss: {running_loss / 100:.4f}')
                running_loss = 0.0

    print('Finished Training')


# Main function
if __name__ == "__main__":
    # 6. Path to the GTZAN dataset folder
    audio_dir = "/Users/duncanroepke/Downloads/Data/genres_original"  # This point to the folder where "blues", "classical", etc. are located

    # 7. Create DataLoader from GTZAN dataset
    train_loader = create_dataloader(audio_dir, batch_size=32)

    # 8. Initialize model, loss function, and optimizer
    num_classes = 10  # GTZAN has 10 genres
    model = GenreClassificationCNN(num_classes)
    criterion = nn.CrossEntropyLoss()
    optimizer = optim.Adam(model.parameters(), lr=0.0005)

    # 9. Train the model
    train_model(model, train_loader, criterion, optimizer, num_epochs=30)

    # 10. Save the trained model
    torch.save(model.state_dict(), "genre_classification_cnn.pth")
