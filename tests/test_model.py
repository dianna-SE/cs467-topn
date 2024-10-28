#  Author: Sergios Karagiannakos
#  Date Accessed: October 21, 2024
#  Unit Testing with Deep Learning
#  Adapted from source URL:
#       https://theaisummer.com/unit-test-deep-learning/


# Ideas to test:
#   - Test if file is corrupted or not before passing
#       to neural network model (Some checks made)
#   - Test if model loads successfully with servers
#   - Edge cases (empty files, WAV but no sound, no file uploaded, etc.)
#          (Some checks made)
#   - Test that audio file is less than X seconds (not too long) or if able
#       to handle large files

import unittest
import wave
import torch

# may need to convert the model in .ipynb file to .py to properly test model ?
# run test: python3 -m unittest test_model.py


class ModelTest(unittest.TestCase):
    def load_model(self):
        """This method loads the model and returns it while handling exception
        errors."""

        # source:
        # https://pytorch.org/tutorials/beginner/saving_loading_models.html
        # accessed october 27, 2024
        # function to load model

        # (file to path -- assuming model is in .pth PYTORCH file)
        model_path = "../model.pth"

        # try block for less cryptic error
        try:
            model = torch.load(model_path, weights_only=True)
            model.eval()
            return model

        # tests missing file or incorrect path
        except FileNotFoundError:
            print(f"ERROR: Model does not exist at {model_path}.")
            return None

        # tests invalid or corrupt model files
        except Exception as event:
            print(f"ERROR: Failed to load model: {str(event)}")
            return None

    # Testing audio input and model in CLI (through unit testing)
    def test_invalid_model(self):
        """Tests if the model exists when loading it."""
        model = self.load_model()
        self.assertIsNotNone(model,
                             "ERROR: Invalid or model file does not exist.")

    # Author: Python
    # Date Accessed: October 28, 2024
    # Documentation that provides functions and exceptions to reading and
    #   writing WAV files.
    # Adapted from source URL:
    #      https://docs.python.org/3/library/wave.html
    def open_wav(self):
        """Method that opens a WAV file and returns it for testing."""

        # working WAV
        wav_path = (
            "./audio_datasets/Joint_C_Beat_Laboratory_"
            "War_with_Yourself.wav"
            )

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


if __name__ == '__main__':
    unittest.main()
