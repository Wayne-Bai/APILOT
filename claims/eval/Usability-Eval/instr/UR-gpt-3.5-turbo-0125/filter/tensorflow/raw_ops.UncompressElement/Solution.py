
import tensorflow as tf

def uncompress(dataset, compression_type='', component_types=[], component_shapes=[]):
    return tf.raw_ops.UncompressDataset(
        dataset=dataset,
        compression_type=compression_type,
        component_types=component_types,
        component_shapes=component_shapes
    )
