import unittest
from face_recognition_module import detect_faces, generate_embeddings

class TestFaceRecognition(unittest.TestCase):
    def test_detect_faces(self):
        # Test with a sample image
        image_path = "test_images/sample.jpg"
        faces = detect_faces(image_path)
        self.assertGreater(len(faces), 0, "No faces detected in the sample image.")

    def test_generate_embeddings(self):
        # Test with a dummy face data
        face_data = "sample_face_data"
        embedding = generate_embeddings(face_data)
        self.assertIsNotNone(embedding, "Embedding generation failed for the given face data.")
        self.assertEqual(len(embedding), 128, "Embedding length should be 128 dimensions.")  # Example dimension

if __name__ == "__main__":
    unittest.main()

