import os
import random

import numpy as np
from keras.preprocessing import image


class TripletGenerator:
    def __init__(self, dataset_path, batch_size=32, target_size=(160, 160)):
        self.dataset_path = dataset_path
        self.batch_size = batch_size
        self.target_size = target_size
        self.classes = os.listdir(dataset_path)
        self.class_indices = {cls: i for i, cls in enumerate(self.classes)}
        self.image_paths = {
            cls: [
                os.path.join(dataset_path, cls, img)
                for img in os.listdir(os.path.join(dataset_path, cls))
            ]
            for cls in self.classes
        }

    def __len__(self):
        return len(self.classes)

    def __getitem__(self, idx):
        cls = self.classes[idx]
        positive_images = random.sample(self.image_paths[cls], 2)
        negative_cls = random.choice([c for c in self.classes if c != cls])
        negative_image = random.choice(self.image_paths[negative_cls])

        anchor = self.load_and_preprocess_image(positive_images[0])
        positive = self.load_and_preprocess_image(positive_images[1])
        negative = self.load_and_preprocess_image(negative_image)

        return np.array([anchor, positive, negative]), np.array([1, 0])

    def load_and_preprocess_image(self, img_path):
        img = image.load_img(img_path, target_size=self.target_size)
        img_array = image.img_to_array(img)
        img_array = np.expand_dims(img_array, axis=0)
        img_array /= 255.0
        return img_array

    def generate(self):
        while True:
            for i in range(len(self)):
                yield self[i]
