import tensorflow.compat.v1 as tf
tf.enable_eager_execution()

import tensorflow_datasets as tfds
tfds.disable_progress_bar()

import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'  # or any {'0', '1', '2'}
os.environ['TFDS_DATA_DIR'] = 'gs://tfds-data/downloads'
