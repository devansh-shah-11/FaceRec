from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.preprocessing.image import img_to_array, load_img
import numpy as np

def load_optimized_model():
    model = MobileNetV2(weights='imagenet', include_top=False, input_shape=(224, 224, 3))
    print("Loaded MobileNetV2 model for optimized face detection.")
    return model

def preprocess_image(image_path):
    image = load_img(image_path, target_size=(224, 224))
    image = img_to_array(image)
    image = image / 255.0  # Normalize image
    image = np.expand_dims(image, axis=0)
    return image

# Example usage
if __name__ == "__main__":
    model = load_optimized_model()
    preprocessed_image = preprocess_image("path/to/sample_image.jpg")
    features = model.predict(preprocessed_image)
    print("Extracted features:", features)
