#  Author: Sergios Karagiannakos
#  Date Accessed: October 21, 2024
#  Unit Testing with Deep Learning
#  Adapted from source URL:
#       https://theaisummer.com/unit-test-deep-learning/

from train_model import GenreClassificationCNN
import torch
import unittest
import os

# running in root dir: python3 -m unittest tests.unittest_model


class ModelTest(unittest.TestCase):
    """Unit test to validate several properties of neural network model."""
    def load_model(self):
        """Helper method that reuses logic to load the model."""

        # getting relative path through os
        model_path = os.path.join(
            os.path.dirname(__file__), "../genre_classification_cnn.pth"
        )

        # initialize the model
        num_classes = 10
        model = GenreClassificationCNN(num_classes)
        model.load_state_dict(torch.load(model_path))
        model.eval()

        return model

    def test_model_parameters(self):
        """Tests that the model contains parameters. No parameters indicate
        the model was not initialized correctly or the weights did not load."""
        model = self.load_model()

        # initialize and retrieve all weights and biases of model
        model_parameters = len(list(model.parameters()))
        self.assertTrue(model_parameters > 0,
                        "ERROR: Parameters missing or not loaded.")

    # Author: Pytorch
    # Date Accessed: October 30, 2024
    # Generating a random number and returns a tensor. Used to
    # generate a test input and comparing against model prediction
    #  Adapted from source URL:
    #       https://pytorch.org/docs/stable/generated/torch.randn.html

    def test_valid_prediction(self):
        """Tests if the model produces a prediction from a tensor input and
        if the output shape matches expected shape."""
        model = self.load_model()

        # initialize random tensor with correct shape and dimensions
        # for model processing and generate prediction
        # a valid tensor input should have 4 dimensions: batch, channels, 
        #   height, width
        valid_tensor = torch.randn(1, 1, 64, 64)
        prediction = model(valid_tensor)

        # check that the output shape matches expected shape
        # model should product 1 prediction, 10 values (10 genres in dataset)
        self.assertEqual(prediction.shape, (1, 10),
                         "ERROR: Prediction is mismatched.")

    def test_model_invalid_input_shape(self):
        """Tests that the model raises an error when given an input with the
        incorrect input shape. Tensors are how the model receives data to
        make predictions."""
        model = self.load_model()

        # creates a tensor with random values with invalid shapes
        #   and missing dimensions (1, 2, 3)
        invalid_tensor = torch.randn(1, 2, 3)

        # model should raise an error for invalid input shape
        with self.assertRaises(RuntimeError):
            model(invalid_tensor)


if __name__ == '__main__':
    unittest.main()
