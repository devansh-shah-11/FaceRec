import numpy as np
import tensorflow as tf
import tensorflow.keras.backend as K
from tensorflow.keras.losses import Loss


class TripletLoss(Loss):
    def __init__(self, margin=1.0, **kwargs):
        super().__init__(**kwargs)
        self.margin = margin

    def call(self, y_true, y_pred):
        anchor, positive, negative = y_pred[:, 0], y_pred[:, 1], y_pred[:, 2]
        pos_dist = K.sum(K.square(anchor - positive), axis=-1)
        neg_dist = K.sum(K.square(anchor - negative), axis=-1)
        loss = K.maximum(pos_dist - neg_dist + self.margin, 0.0)
        return K.mean(loss)


class ContrastiveLoss(Loss):
    def __init__(self, margin=1.0, **kwargs):
        super().__init__(**kwargs)
        self.margin = margin

    def call(self, y_true, y_pred):
        y_true = K.cast(y_true, y_pred.dtype)
        pos_dist = K.sum(K.square(y_pred[:, 0] - y_pred[:, 1]), axis=-1)
        neg_dist = K.sum(K.square(y_pred[:, 0] - y_pred[:, 2]), axis=-1)
        loss = y_true * pos_dist + (1 - y_true) * \
            K.maximum(self.margin - neg_dist, 0.0)
        return K.mean(loss)


class ArcFaceLoss(Loss):
    def __init__(self, scale=64.0, margin=0.5, **kwargs):
        super().__init__(**kwargs)
        self.scale = scale
        self.margin = margin

    def call(self, y_true, y_pred):
        y_true = K.cast(y_true, y_pred.dtype)
        cosine = K.clip(y_pred, -1.0, 1.0)
        theta = tf.acos(cosine)
        target_logits = tf.cos(theta + self.margin)
        logits = y_true * target_logits + (1 - y_true) * cosine
        logits *= self.scale
        return tf.nn.softmax_cross_entropy_with_logits(labels=y_true, logits=logits)
