import tensorflow as tf

class CustomForward(tf.raw_op.RawOp):
    def __init__(self, pred):
        super().__init__('CustomForward', inputs=[pred], outputs=[tf.Tensor])

    def compute(self, session):
        pred_value = session.run(self.inputs[0])
        output = tf.Tensor(pred_value)
        return output

# Create a graph
g = tf.Graph()

# Create a pred tensor
pred = g.add_fragment(tf.constant(5.0))

# Create a CustomForward op
custom_forward = CustomForward(pred)

# Create a session
with tf.Session(graph=g) as sess:
    # Run the graph
    sess.run(custom_forward)
