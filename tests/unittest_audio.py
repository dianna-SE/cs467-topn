#  Author: Sergios Karagiannakos
#  Date Accessed: October 21, 2024
#  Unit Testing with Deep Learning
#  Adapted from source URL:
#       https://theaisummer.com/unit-test-deep-learning/

import unittest
import wave

# running in root dir: python3 -m unittest tests.unittest_audio


class AudioTest(unittest.TestCase):
    """Unit tests to validate WAV files and several properties."""

    # Author: Python
    # Date Accessed: October 28, 2024
    # Documentation that provides functions and exceptions to reading and
    #   writing WAV files.
    # Adapted from source URL:
    #      https://docs.python.org/3/library/wave.html
    def open_wav(self):
        """Method that opens a WAV file and returns the file
        object for testing."""

        # working WAV
        wav_path = (
            "./tests/audio_datasets/"
            "Joint_C_Beat_Laboratory_War_with_Yourself.wav"
        )

        # invalid WAV (corrupt)
        # wav_path = ("./audio_datasets/corrupt_file.wav")
        return wave.open(wav_path, mode='rb')

    # checks several components of a WAV file for invalid, missing, or corrupt
    def test_wav_channels(self):
        """Tests if the WAV file has at least 1 audio channel. Having
        no channel can indicate that the file contains no audible sound."""

        # call func to open file path
        wav_file = self.open_wav()

        # returns  number of audio channels:
        # 1 (mono), 2 (stereo), or 3 (surround sound)
        channels = wav_file.getnchannels()

        # no channel indicates a possible issue with WAV file (no sound)
        self.assertGreater(channels, 0, f'ERROR: No channel detected. '
                           f'Channels: {channels}')

        wav_file.close()

    def test_wav_frame_rates(self):
        """Tests if the WAV file has a frame rate (sampling frequency)."""
        wav_file = self.open_wav()

        # gets sampling frequency (Hz)
        frame_rates = wav_file.getframerate()

        # having no frame rate indicates no frequency to the WAV -
        # sound could be distorted, missing or corrupt
        self.assertGreater(frame_rates, 0, f'ERROR: No audio frames found. '
                           f'Sampling frequency: {frame_rates}')
        wav_file.close()

    def test_wav_audio_frames(self):
        """Tests if the WAV file is empty (no audio)."""
        wav_file = self.open_wav()

        # gets the number of audio frames -
        audio_frames = wav_file.getnframes()

        # having no audio frames indicate frame count is missing
        #   (eempty, invalid, or corrupt)
        self.assertGreater(audio_frames, 0,
                           f'ERROR: No audio frames found. '
                           f'Number of frames: {audio_frames}')

        wav_file.close()


if __name__ == '__main__':
    unittest.main()
