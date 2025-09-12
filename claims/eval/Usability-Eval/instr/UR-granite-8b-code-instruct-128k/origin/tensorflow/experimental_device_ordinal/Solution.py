import tensorflow as tf

def generate_virtual_device(ordinal_number):
    virtual_device = "/job:localhost/replica:0/task:0/device:GPU:" + str(ordinal_number)
    return virtual_device
