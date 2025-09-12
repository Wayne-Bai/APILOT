import tensorflow as tf

class DifferentiableGraph:
    def __init__(self):
        self.w = tf.Variable(0.0, trainable=True)
        self.x = tf.Variable(0.0, trainable=False)

    @tf.function
    def forward(self):
        return tf.nn.relu(self.x * self.w)

    @tf.function
    def backward(self, output_gradients):
        with tf.GradientTape() as tape:
            tape.watch(self.w)
            tape.watch(self.x)
            loss = tf.reduce_mean(output_gradients)
            x_grad = tape.gradient(loss, self.x)
            w_grad = tape.gradient(loss, self.w)
            return x_grad, w_grad
