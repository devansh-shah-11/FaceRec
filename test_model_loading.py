import unittest

from model_optimization import \
    load_optimized_model  # Replace with the actual module name


class TestModelLoading(unittest.TestCase):
    def test_model_loading(self):
        """Test if the optimized model loads correctly."""
        model = load_optimized_model()
        self.assertIsNotNone(
            model, "The model should not be None after loading.")
        self.assertTrue(
            hasattr(model, "predict"),
            "The loaded model should have a 'predict' method.",
        )

    def test_model_input_shape(self):
        """Test if the model input shape is as expected."""
        model = load_optimized_model()
        input_shape = model.input_shape
        self.assertEqual(
            input_shape,
            (None, 224, 224, 3),
            "Model input shape should be (None, 224, 224, 3).",
        )


if __name__ == "__main__":
    unittest.main()
