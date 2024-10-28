from model_optimization import \
    preprocess_image  # Replace with actual module name
import unittest
import numpy as np
from tensorflow.keras.preprocessing.image import img_to_array, load_img


def preprocess_image(image_path):
    """Preprocess the image for model prediction."""
    try:
        image = load_img(image_path, target_size=(224, 224))
    except FileNotFoundError:
        raise FileNotFoundError(f"Image not found at path: {image_path}")
    except Exception as e:
        raise ValueError(f"Error loading image: {str(e)}")

    image = img_to_array(image)
    if image.shape != (224, 224, 3):
        raise ValueError(
            f"Image shape is invalid. Expected (224, 224, 3), got {image.shape}."
        )

    image = image / 255.0  # Normalize
    image = np.expand_dims(image, axis=0)
    return image


class TestPreprocessImage(unittest.TestCase):
    def test_nonexistent_image_path(self):
        """Test case for a nonexistent image path."""
        with self.assertRaises(FileNotFoundError):
            preprocess_image("invalid_path.jpg")

    def test_invalid_image_format(self):
        """Test case for an invalid image format."""
        with self.assertRaises(ValueError):
            preprocess_image("test_images/invalid_format.txt")

    def test_invalid_image_shape(self):
        """Test case for an image with invalid shape."""
        # Simulate a grayscale image by resizing to (224, 224) and checking for failure.
        with self.assertRaises(ValueError):
            preprocess_image("test_images/grayscale_image.jpg")


if __name__ == "__main__":
    unittest.main()
