import tensorflow as tf

def get_ordered_virtual_devices(gpus):
    # Sort GPUs by device id
    gpus.sort(key=lambda gpu: gpu.device_id)
    
    # Create a list of virtual devices sorted by ordinal number
    virtual_devices = [tf.distribute.MirroredStrategy.VirtualDevice(gpu) for gpu in gpus]
    
    return virtual_devices
