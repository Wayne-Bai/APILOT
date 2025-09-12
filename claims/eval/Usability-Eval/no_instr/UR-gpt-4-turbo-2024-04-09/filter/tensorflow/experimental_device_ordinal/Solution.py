import tensorflow as tf

# Function to set the virtual device order based on ordinal numbers
def set_gpu_device_order():
    gpus = tf.config.experimental.list_physical_devices('GPU')
    if gpus:
        try:
            # Sorting the GPUs by their physical device id
            gpus_sorted = sorted(gpus, key=lambda gpu: gpu.name)
            tf.config.experimental.set_visible_devices(gpus_sorted, 'GPU')
            
            # Setting memory growth to avoid occupying full memory
            for gpu in gpus_sorted:
                tf.config.experimental.set_memory_growth(gpu, True)
            
            # Print out the order of GPUs after setting
            print("GPUs ordered by physical ID:", [gpu.name for gpu in gpus_sorted])
        except RuntimeError as e:
            print(e)

# Call the function to order the virtual devices
set_gpu_device_order()
