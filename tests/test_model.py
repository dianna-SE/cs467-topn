#  Author: Sergios Karagiannakos
#  Date Accessed: October 21, 2024
#  Unit Testing with Deep Learning
#  Adapted from source URL:
#       https://theaisummer.com/unit-test-deep-learning/

# Ideas to test:
#   - Test if file is corrupted or not before passing to neural network model
#   - Test if model loads successfully with servers
#   - Test that web application rejects non-WAV files
#   - Edge cases (empty files, WAV but no sound, no file uploaded, etc.)
#   - Test that audio file is less than X seconds (not too long) or if able
#       to handle large files

import unittest

# may need to convert the model in .ipynb file to .py to properly test model ?

class ModelTest(unittest.TestCase):
    def test_corrupt_file(self):
        """Tests whether a file is corrupt or not. Web application should....
        before sending the audio file to the neural network model."""
        pass


if __name__ == '__main__':
    unittest.main()
