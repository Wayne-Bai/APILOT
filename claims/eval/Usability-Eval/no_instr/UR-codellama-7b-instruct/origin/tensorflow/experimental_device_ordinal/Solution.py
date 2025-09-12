
from tensorflow import ConfigProto, Session, set_session
import os

# Create a session config to set the ordinal number of the device
config = ConfigProto()
config.gpu_options.per_process_gpu_memory_fraction = 0.25

# Set the ordinal number for each GPU device
for gpu in config.gpu_options.visible_device_list:
    os.environ['CUDA_DEVICE_ORDER'] = 'PCI_BUS_ID'
    os.environ['CUDA_VISIBLE_DEVICES'] = str(gpu) + ',' + str(gpu+1)

# Create a session with the new config and start it
set_session(Session(config=config))
