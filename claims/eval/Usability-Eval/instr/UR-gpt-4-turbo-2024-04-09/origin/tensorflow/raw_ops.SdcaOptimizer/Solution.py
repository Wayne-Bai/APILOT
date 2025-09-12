import tensorflow as tf

def sdca_model(features, labels, options):
    # Create the SDCA optimizer using the new compatible method
    sdca_optimizer = tf.raw_ops.SdcaOptimizerV2(
        sparse_features_indices=[x.indices for x in features if isinstance(x, tf.IndexedSlices)],
        sparse_features_values=[x.values for x in features if isinstance(x, tf.IndexedSlices)],
        dense_features=[x for x in features if not isinstance(x, tf.IndexedSlices)],
        example_weights=tf.fill(dims=[tf.shape(labels)[0]], value=1.0),
        example_labels=tf.cast(labels, dtype=tf.float32),
        sparse_indices=[x.indices for x in features if isinstance(x, tf.IndexedSlices)],
        sparse_weights=[tf.Variable(tf.random.normal(x.values.shape)) for x in features if isinstance(x, tf.IndexedSlices)],
        dense_weights=[tf.Variable(tf.random.normal([x.shape[1]])) for x in features if not isinstance(x, tf.IndexedSlices)],
        loss_type='logistic_loss',
        l1=0.0,
        l2=1.0,
        num_loss_partitions=1,
        num_inner_iterations=1,
        adaptive=True,
        **options
    )
    return sdca_optimizer

# Example usage
feature_1 = tf.constant([[1.0, 2.0], [3.0, 4.0]])
feature_2 = tf.IndexedSlices(values=tf.constant([0.5, 0.8]), indices=tf.constant([0, 1]))
labels = tf.constant([0, 1])

sdca_optimizer_output = sdca_model([feature_1, feature_2], labels, options={})
print(sdca_optimizer_output)
