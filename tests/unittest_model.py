#  Author: Sergios Karagiannakos
#  Date Accessed: October 21, 2024
#  Unit Testing with Deep Learning
#  Adapted from source URL:
#       https://theaisummer.com/unit-test-deep-learning/

from train_model import GenreClassificationCNN
import torch
import unittest
import wave
import os

# running in root dir: python3 -m unittest tests.unittest_model


class ModelTest(unittest.TestCase):
    def test_load_model(self):
        """Tests by loading the model and that it exists."""

        # get the relative path using os
        model_path = os.path.join(
            os.path.dirname(__file__), "../genre_classification_cnn.pth"
        )

        model = GenreClassificationCNN(num_classes=10)
        model.load_state_dict(torch.load(model_path))
        model.eval()

    # Author: Python
    # Date Accessed: October 28, 2024
    # Documentation that provides functions and exceptions to reading and
    #   writing WAV files.
    # Adapted from source URL:
    #      https://docs.python.org/3/library/wave.html
    def open_wav(self):
        """Method that opens a WAV file and returns it for testing."""

        # working WAV
        wav_path = "./tests/audio_datasets/Joint_C_Beat_Laboratory_War_with_Yourself.wav"

        # invalid WAV (corrupt)
        # wav_path = ("./audio_datasets/corrupt_file.wav")
        return wave.open(wav_path, mode='rb')

    # Tests several components of a WAV file for corruption
    def test_wav_no_channel(self):
        """Tests if the WAV file has no channel. This can indicate that the
        WAV file has no audible sound."""

        # call func to open file path
        wav_file = self.open_wav()

        # returns  number of audio channels:
        # 1 (mono), 2 (stereo), or 3 (surround sound)
        channels = wav_file.getnchannels()

        # no channel indicates a possible issue with WAV file (no sound)
        print("Channels: ", channels)
        self.assertGreater(channels, 0, f'ERROR: No channel detected. '
                           f'Channels: {channels}')

        wav_file.close()

    def test_wav_no_frame_rate(self):
        """Tests if the WAV file has a frame rate (sampling frequency)."""
        wav_file = self.open_wav()

        # gets sampling frequency (Hz)
        frame_rates = wav_file.getframerate()

        # having no frame rate indicates no frequency to the WAV -
        # sound could be distorted, missing or corrupt
        print("Frame Rates: ", frame_rates)
        self.assertGreater(frame_rates, 0, f'ERROR: No audio frames found. '
                           f'Sampling frequency: {frame_rates}')
        wav_file.close()

    def test_wav_no_audio_frames(self):
        """Tests if the WAV file is empty (no audio)."""
        wav_file = self.open_wav()

        # gets the number of audio frames -
        audio_frames = wav_file.getnframes()

        # having no audio frames indicate frame count is missing
        #   (invalid or corrupt)
        print("Audio Frames: ", audio_frames)
        self.assertGreater(audio_frames, 0,
                           f'ERROR: No audio frames found. '
                           f'Number of frames: {audio_frames}')

        wav_file.close()

    def test_model_prediction(self):
        """Tests if the model predictions are accurate."""
        pass

    # test genres
    def test_hip_hop_genre_prediction(self):
        """Tests if the model predicts the WAV file as hip hop accurately."""
        pass


if __name__ == '__main__':
    unittest.main()
