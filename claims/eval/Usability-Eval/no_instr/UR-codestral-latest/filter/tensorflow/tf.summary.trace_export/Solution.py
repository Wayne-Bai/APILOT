import tensorflow as tf
from tensorflow.python.profiler import profiler_v2 as profiler

# define your computations here
# ...

with tf.Graph().as_default():
    # start trace
    tf.summary.trace_on(graph=True, profiler=True)
    with tf.Session() as sess:
        # run your computations here
        # ...

        # export the trace
        options = tf.profiler.export_options.TraceOptions(host_tracer_level=3)
        tf.profiler.export_op_trace(sess.graph, trace_file="op_trace.json", options=options)
        # stop the trace
        tf.summary.trace_export(name="trace", step=0, profiler_outdir="./logs")
