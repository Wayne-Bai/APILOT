import tensorflow as tf
from tensorflow import keras

# Function to resize images
def resize_images(images, size):
    # Create a new TensorFlow session
    sess = tf.Session()

    # Define the image resizing operation
    resized_images = keras.layers.Lambda(lambda x: tf.image.resize_images(x, size))(images)

    # Evaluate the session with the input images
    sess.run(resized_images, feed_dict={images: images})

# Driver function to test the resizing operation
if __name__ == "__main__":
    # Define the input image shape and size
    image_shape = (28, 28, 1)
    new_size = (32, 32)

    # Create a sample image with random values
    images = tf.random.normal(image_shape)

    # Resize the image using the resize_images function
    resized_images = resize_images(images, new_size)

    # Print the resulting image shape
    print("Resized image shape: ", resized_images.get_shape())
