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

    def test_invalid_model(self):
        """Tests if the model exists when loading it."""
        model = self.load_model()
        self.assertIsNotNone(model,
                             "ERROR: Invalid or model file does not exist.")


if __name__ == '__main__':
    unittest.main()
