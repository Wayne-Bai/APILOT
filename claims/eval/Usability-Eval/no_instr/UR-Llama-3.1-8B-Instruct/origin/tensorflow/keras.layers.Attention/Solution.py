import tensorflow as tf

class DotProductAttention(tf.keras.layers.Layer):
    """
    Dot-product attention layer, a.k.a. Luong-style attention.
    
    Args:
    - q (tf.Tensor): Query tensor.
    - k (tf.Tensor): Key tensor.
    - v (tf.Tensor): Value tensor.
    - d_model (int): Model dimension.
    - attention_mask (tf.Tensor): Attention mask.
    
    Returns:
    - context: Attention output.
    """
    def __init__(self, d_model, attention_mask=None):
        super(DotProductAttention, self).__init__()
        self.d_model = d_model
        self.attention_mask = attention_mask
    
    def build(self, input_shape):
        super(DotProductAttention, self).build(input_shape)
    
    def call(self, q, k, v):
        """
        Compute dot-product attention.
        
        Args:
        - q (tf.Tensor): Query tensor.
        - k (tf.Tensor): Key tensor.
        - v (tf.Tensor): Value tensor.
        
        Returns:
        - context: Attention output.
        """
        # Compute dot-product attention scores
        scores = tf.matmul(q, k, transpose_b=True) / tf.math.sqrt(self.d_model)
        
        # Apply attention mask
        if self.attention_mask is not None:
            scores = tf.multiply(scores, self.attention_mask)
        
        # Compute attention weights
        weights = tf.nn.softmax(scores)
        
        # Compute context
        context = tf.matmul(weights, v)
        
        return context

def create_dot_product_attention(d_model, attention_mask=None):
    """
    Create dot-product attention layer.
    
    Args:
    - d_model (int): Model dimension.
    - attention_mask (tf.Tensor): Attention mask.
    
    Returns:
    - dot_product_attention: Dot-product attention layer.
    """
    return DotProductAttention(d_model, attention_mask=attention_mask)

# Example usage
q = tf.constant([1, 2, 3])
k = tf.constant([4, 5, 6])
v = tf.constant([7, 8, 9])
d_model = 10
attention_mask = tf.constant([1, 0, 1])

dot_product_attention = create_dot_product_attention(d_model, attention_mask)
context = dot_product_attention(q, k, v)
print(context)
