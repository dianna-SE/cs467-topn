#  Author: Sergios Karagiannakos
#  Date Accessed: October 21, 2024
#  Unit Testing with Deep Learning
#  Adapted from source URL:
#       https://theaisummer.com/unit-test-deep-learning/

import unittest
import wave

# To run these tests, run the command in the root directory:
#       python3 -m unittest tests.unittest_audio


class AudioTest(unittest.TestCase):
    """Unit tests to validate WAV files and several properties."""

    # Author: Python
    # Date Accessed: October 28, 2024
    # Documentation that provides functions and exceptions to reading and
    #   writing WAV files.
    # Adapted from source URL:
    #      https://docs.python.org/3/library/wave.html
    def open_wav(self, wav_path):
        """
        Opens a WAV file for unit testing.

        Returns:
            The opened WAV file object.
        """

        return wave.open(wav_path, mode='rb')

    def valid_wav(self):
        """
        Returns a valid wav file for unit testing.
        """
        return (
            "./tests/audio_datasets/"
            "Joint_C_Beat_Laboratory_War_with_Yourself.wav"
        )

    def corrupt_wav(self):
        """
        Returns a corrupt wav file for unit testing.
        """
        return "./tests/audio_datasets/corrupt_file.wav"

    def test_wav_channels(self):
        """
        Checks if the WAV file has at least one audio channel.

        Values include audio channels:
            - Mono (1)
            - Stero (2)
            - Surround sound (3)

        Raises:
            Assertion error if there is no channel detected when opening
            the WAV file.
        """

        # Opens a file path
        wav_file = self.open_wav(self.valid_wav())

        # Return the number of audio channels
        channels = wav_file.getnchannels()

        self.assertGreater(channels, 0, f'ERROR: No channel detected. '
                           f'Channels: {channels}')

        wav_file.close()

    def test_wav_frame_rates(self):
        """
        Checks if the WAV file has a frame rate
        (sampling frequency).

        Raises:
            Assertion error if there are no frequencies.
        """
        wav_file = self.open_wav(self.valid_wav())

        # Get the sampling frequency (Hz)
        frame_rates = wav_file.getframerate()

        self.assertGreater(frame_rates, 0, f'ERROR: No frequencies found. '
                           f'Sampling frequency: {frame_rates}')
        wav_file.close()

    def test_wav_audio_frames(self):
        """
        Checks if the WAV file does not contain any audio frames.

        Raises:
            Assertion error if no audio frames are found.
        """
        wav_file = self.open_wav(self.valid_wav())

        # Get the number of audio frames -
        audio_frames = wav_file.getnframes()

        self.assertGreater(audio_frames, 0,
                           f'ERROR: No audio frames found. '
                           f'Number of frames: {audio_frames}')

        wav_file.close()

    # Author: WA Production
    # Date Accessed: November 13, 2024
    # Understanding audio quality formats (WAV, MP3, FLAC)
    #     Examples of bit sizes and frame rates for WAV files
    # Adapted from source URL:
    #      https://blog.waproduction.com/how-to-understand-audio-quality-formats
    def test_sample_rate(self):
        """
        Checks that the sample rate is too low or
        high for model processing and handles it accordingly.

        Raises:
            Exception error if the sample rate is either too low
            or too high.
        """
        # Open wav file and get sample rate
        wav_file = self.open_wav(self.valid_wav())
        sample_rate = wav_file.getframerate()

        # Checks if the file is within frequency range for WAV file
        self.assertTrue(44100 <= sample_rate <= 96000,
                        f"ERROR: Sample rate {sample_rate} Hz is invalid."
                        "Recommended range is between 44.1-96 kHz.")

        wav_file.close()


if __name__ == '__main__':
    unittest.main()
