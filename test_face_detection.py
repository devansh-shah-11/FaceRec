import os
import unittest

from face_recognition_module import \
    detect_faces  # Replace with the actual module name


class TestFaceDetection(unittest.TestCase):
    def test_invalid_image_path(self):
        """Test case for an invalid image path."""
        invalid_path = "non_existent_directory/non_existent_image.jpg"
        with self.assertRaises(FileNotFoundError):
            detect_faces(invalid_path)

    def test_corrupted_image_file(self):
        """Test case for a corrupted image file."""
        # Create a corrupted image file for testing
        corrupted_image_path = "test_images/corrupted_image.jpg"
        with open(corrupted_image_path, "w") as f:
            f.write("This is not a valid image content")

        with self.assertRaises(ValueError):
            detect_faces(corrupted_image_path)

        # Clean up the corrupted image file after testing
        os.remove(corrupted_image_path)

    def test_unsupported_image_format(self):
        """Test case for an unsupported image format."""
        unsupported_image_path = "test_images/sample.txt"
        # Create a text file to simulate an unsupported image format
        with open(unsupported_image_path, "w") as f:
            f.write("This is a text file, not an image.")

        with self.assertRaises(ValueError):
            detect_faces(unsupported_image_path)

        # Clean up the text file after testing
        os.remove(unsupported_image_path)

    def test_empty_image_file(self):
        """Test case for an empty image file."""
        empty_image_path = "test_images/empty_image.jpg"
        # Create an empty file
        open(empty_image_path, "w").close()

        with self.assertRaises(ValueError):
            detect_faces(empty_image_path)

        # Clean up the empty image file after testing
        os.remove(empty_image_path)


if __name__ == "__main__":
    unittest.main()
