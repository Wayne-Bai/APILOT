# Import the tensorflow library
import tensorflow as tf

# Option 1: Constructing a Checkpoint with Boilerplate
class Net(tf.Module):
    def __init__(self):
        self.weights = tf.Variable(tf.random.normal([784, 10]))

    def __call__(self, x):
        return tf.matmul(x, self.weights)

net = Net()
# Create a Checkpoint object and add the Net instance to it
ckpt = tf.train.Checkpoint(net=net)
ckpt.save('./save/net_weights')

# Option 2: Automatically Track Variables
class RegExp(tf.Module):
    def __init__(self):
        self.w = tf.Variable(tf.random.normal([784, 10]))
        self.b = tf.Variable(tf.zeros([10]))

    def __call__(self, x):
        return tf.matmul(x, self.w) + self.b

reg_exp = RegExp()
# With this approach, no need to manually create a tf.train.Checkpoint
reg_exp.save_weights('./save/model_weights')

# Option 3: With a tf.data.Dataset
model = tf.train.Checkpoint(w=tf.Variable(tf.random.normal([784, 10])))
checkpoint_path = './save/model_weights'
model.save(checkpoint_path)

# Option 4: Restore and use a Model from a Saved Checkpoint
status = model.load('./save/model_weights-1')
print(status.assert_consumed())

# Option 5: Full Model Signatures (full SavedModels)
class PairsForSums(tf.Module):
    @tf.function(input_signature=[tf.TensorSpec(shape=[None], dtype=tf.int32)])
    def pairs_for_sums(self, values):
        return tf.compat.v1.data.Dataset.from_tensor_slices(values)

    @tf.function(input_signature=[tf.TensorSpec(shape=[None], dtype=tf.int32)])
    def filtered(self, values):
        return tf.compat.v1.data.Dataset.from_tensor_slices(values).filter(lambda x: x> 5)
        
# Save model and restore later and call a non-fixed
# Signature function
model = PairsForSums()
tf.saved_model.save(model, './saved_model')
# later...
loaded = tf.saved_model.load('./saved_model')
loaded.pairs_for_sums(tf.constant([1, 2, 3])) # works 
loaded.filtered(tf.constant([1, 2, 3, 6, 7, 8]))  # works
