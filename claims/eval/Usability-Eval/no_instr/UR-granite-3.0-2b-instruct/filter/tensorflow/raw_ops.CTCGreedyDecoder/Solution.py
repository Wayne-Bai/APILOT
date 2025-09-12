import tensorflow as tf

class GreedyDecoder(tf.raw_op.RawOp):
    def __init__(self, **kwargs):
        super(GreedyDecoder, self).__init__(**kwargs)

    def _build(self, graph, name=None):
        self.input_logits = graph.input[0]
        self.input_shape = graph.get_input_shape(self.input_logits)
        self.output_decoding = graph.output[0]
        self.output_shape = graph.get_output_shape(self.output_decoding)

    def _run(self, session, feed_dict={}):
        input_logits = session.run(self.input_logits, feed_dict)
        input_shape = self.input_shape
        output_decoding = session.run(self.output_decoding, feed_dict)
        output_shape = self.output_shape

        # Perform greedy decoding on the logits
        decoding = []
        for logits in input_logits:
            decoding.append(tf.argmax(logits, axis=-1).numpy())

        return decoding

# Example usage
with tf.Session() as session:
    greedy_decoder = GreedyDecoder()
    decoding = greedy_decoder.run(session, feed_dict={...})
    print(decoding)
