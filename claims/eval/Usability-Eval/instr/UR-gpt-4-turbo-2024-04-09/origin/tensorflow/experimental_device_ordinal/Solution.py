import tensorflow as tf

def set_virtual_device_order():
    gpus = tf.config.experimental.list_physical_devices('GPU')
    if gpus:
        try:
            # TensorFlow uses logical devices for operations
            # Clear any previous virtual devices to set it up freshly
            tf.config.experimental.set_virtual_device_configuration(None)

            # Sort GPUs by their IDs (usually the PCI bus order)
            gpus = sorted(gpus, key=lambda x: x.name)
            logical_gpus = []
            
            # Set memory growth to prevent TensorFlow from allocating all memory
            for gpu in gpus:
                tf.config.experimental.set_memory_growth(gpu, True)
        
            # Assign logical devices using memory growth settings
            for i, gpu in enumerate(gpus):
                # Assuming each physical GPU should map to only one logical GPU
                memory_limit = 1024 * 10  # example: 10GB per GPU, adjust as needed
                tf.config.experimental.set_virtual_device_configuration(
                    gpu,
                    [tf.config.experimental.VirtualDeviceConfiguration(memory_limit=memory_limit)]
                )
                logical_gpus.append(tf.config.experimental.list_logical_devices('GPU')[i])
            
            print(f"Physical GPUs sorted: {gpus}")
            print(f"Associated logical GPUs: {logical_gpus}")
        except RuntimeError as e:
            print(e)

set_virtual_device_order()
