#  Author: Sergios Karagiannakos
#  Date Accessed: October 21, 2024
#  Unit Testing with Deep Learning
#  Adapted from source URL:
#       https://theaisummer.com/unit-test-deep-learning/

from train_model import GenreClassificationCNN
import torch
import unittest
import os

# To run these tests, run the command in the root directory:
#       python3 -m unittest tests.unittest_model


# Author: Python Enhancement Proposals
# Date Accessed: November 11, 2024
# Python Documentation Standards
# Adapted from source URL:
#       https://peps.python.org/pep-0257/

class ModelTest(unittest.TestCase):
    """Unit test to validate several properties of neural network model."""

    def load_model(self):
        """
        Loads the pre-trained GenreClassificationCNN model for testing.

        Returns:
            GenreClassificationCNN: Initialized model with loaded weights.

        """

        # Get the relative path through os
        model_path = os.path.join(
            os.path.dirname(__file__), "../genre_classification_cnn.pth"
        )

        # Initialize the model
        num_classes = 10
        model = GenreClassificationCNN(num_classes)
        model.load_state_dict(torch.load(model_path))
        model.eval()

        # Output in CLI to observe model layers
        print(model)

        return model

    def test_model_parameters(self):
        """
        Checks if the model has parameters loaded for proper initialization.
        """
        model = self.load_model()

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
        """
        Checks that the model predicts shape accurately with given input.
        """
        model = self.load_model()

        # Initialize random tensor with correct shape and dimensions
        #   or model processing and generate prediction

        # A valid tensor input should have 4 dimensions: batch, channels,
        #       height, and width
        valid_tensor = torch.randn(1, 1, 64, 64)
        prediction = model(valid_tensor)

        # Check that the output shape matches expected shape

        # The model should product 1 prediction, 10 values (10 genres in
        #   the dataset)
        self.assertEqual(prediction.shape, (1, 10),
                         "ERROR: Prediction is mismatched.")

    def test_model_invalid_input_shape(self):
        """
        Checks if the model raises an error when given
        a tensor with incorrect dimensions.

        Raises:
            Runtime error if model identifies the tensor.
        """
        model = self.load_model()

        # Create a tensor with random values with invalid shapes
        #   and missing dimensions (1, 2, 3)
        invalid_tensor = torch.randn(1, 2, 3)

        with self.assertRaises(RuntimeError):
            model(invalid_tensor)

    # Author: PyTorch
    # Date Accessed: November 12, 2024
    # Pytorch - Creating test methods for model behavior for tensors with:
    #       - Zero scalar value
    #       - Filled scalar value
    #       - Proper initializiation of linear, convoluted, pooling layers
    #         and more
    # Adapted from source URL:
    #       https://pytorch.org/

    def test_zero_tensor_value(self):
        """
        Tests if the model can handle tensors with a
        zero scalar value.

        Raises:
            Assertion error if model contains NaN or infinite values.
        """
        model = self.load_model()

        # Generate and get model output
        zero_tensor = torch.zeros(1, 1, 64, 64)
        output = model(zero_tensor)

        # Fails test if the model displays an error for zero tensor value
        self.assertFalse(torch.isnan(output).any() or
                         torch.isinf(output).any(),
                         "ERROR: Model output contains NaN or infinite values "
                         "for a tensor with a zero scalar value.")

    def test_high_tensor_value(self):
        """
        Checks the model's output with high tensor values The model
        should display an error with NaN or infinite values.

        Raises:
            Assertion error if model contains NaN or infinite values.
        """
        model = self.load_model()

        # Generate and get model output
        high_tensor = torch.full((1, 1, 64, 64), 999, dtype=torch.float)
        output = model(high_tensor)

        # Fails test if model displays error for high tensor value
        self.assertFalse(torch.isnan(output).any() or
                         torch.isinf(output).any(),
                         "ERROR: Model output contains NaN or infinite values "
                         "for a tensor with a high-filled scalar value.")

    def append_layers(self, layer_type):
        """
        Helper method that appends a specific type of layer from the model.
        """
        model = self.load_model()

        # Find layers in model's children and append to list
        layers = []

        for layer in model.children():
            if isinstance(layer, layer_type):
                layers.append(layer)

        return layers

    def test_model_linear_layers(self):
        """
        Checks for existing fully connected (linear) layers.

        Raises:
            Assertion layer if no linear layers exist.
        """

        linear_layers = self.append_layers(torch.nn.Linear)

        # CLI output to see layers
        print("Linear layers: ", linear_layers)

        self.assertGreater(len(linear_layers), 0,
                           "ERROR: No linear layers were found in the model.")

    def test_model_convolutional_layers(self):
        """
        Checks for existing convolutional layers.

        Raises:
            Assertion layer if no convolutional layers exist.
        """
        conv_layers = self.append_layers(torch.nn.Conv2d)

        print("Convolutional layers: ", conv_layers)

        self.assertGreater(len(conv_layers), 0,
                           "ERROR: No convolutional layers were"
                           "found in the model.")

    def test_model_dropout_layers(self):
        """
        Checks for existing dropout layers.

        Raises:
            Assertion layer if no dropout layers exist.
        """
        dropout_layers = self.append_layers(torch.nn.Dropout)

        print("Dropout layers: ", dropout_layers)
        self.assertGreater(len(dropout_layers), 0, "ERROR: No dropout layers"
                           "were found in the model.")

    # Future test for layer:
    #       - test_model_pooling_layers


if __name__ == '__main__':
    unittest.main()
