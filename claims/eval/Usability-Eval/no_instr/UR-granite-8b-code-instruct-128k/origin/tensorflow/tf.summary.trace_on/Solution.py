
import tensorflow as tf

# Start a trace for recording computation graphs and profiling information.
trace = tf.profiler.trace(
options=tf.profiler.ProfileOptionBuilder.float_operation(),
session=sess)
