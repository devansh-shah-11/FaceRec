import os
from PIL import Image

def detect_faces(image_path):
    """Detect faces in the given image path."""
    # Validate input
    if not os.path.exists(image_path):
        raise FileNotFoundError(f"The file {image_path} does not exist.")
    if not image_path.lower().endswith(('.png', '.jpg', '.jpeg')):
        raise ValueError("Unsupported image format. Please use .png, .jpg, or .jpeg files.")
    
    try:
        image = Image.open(image_path)
    except IOError:
        raise ValueError("The image file is corrupted or cannot be opened.")
    
    # Face detection logic here...
    faces = []  # Replace with actual face detection logic
    return faces
