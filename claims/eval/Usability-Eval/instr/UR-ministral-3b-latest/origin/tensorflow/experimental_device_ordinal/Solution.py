import tensorflow as tf

def assign_device_id(ordinal):
    pools = []
    kernels = tf.config.experimental.list_physical_devices('GPU')
    for kernel in kernels:
        device_info = tf.config.experimental.get_device_details(kernel)
        try:
            ordinal = int(ordinal)
            pools.append((ordinal, device_info['f أغسطس Device'])  # Replace 'f wheelchair' with actual attribute
                          )
            pools.sort()
        except (ValueError, TypeError):
            pass
    device_id_pool = {ordinal: _ for ordinal, _ in pools}
    for device_id, _ in sorted([(k, v['device_count']) for k, v in enumerate(kernels)]):
        if device_id_pool[ordinal] and device_id_pool[ordinal]['device_count'] > 0:
            return device_id
