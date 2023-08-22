# opencv_fave_detector

Explanation of libraries and steps used:

1)tensorflow: This is the primary library used for building and training neural networks. We import it as tf.

2)numpy: This library is used for numerical operations, especially in handling arrays and matrices efficiently. We import it as np.

3)matplotlib: This library is used for data visualization, which we use here to display the test image and the prediction.



The CNN model is defined using tf.keras.Sequential, a sequential model in TensorFlow's Keras API. The model consists of convolutional layers with ReLU activation, max-pooling layers for downsampling, and fully connected layers.

The model is compiled using the Adam optimizer and binary cross-entropy loss for binary classification.

The model's architecture is summarized using model.summary().

The model is trained using the randomly generated images and labels.

A random test image is generated for demonstration.

The model predicts the probability of a face being present in the test image using model.predict().

The test image and the prediction probability are displayed using matplotlib.
