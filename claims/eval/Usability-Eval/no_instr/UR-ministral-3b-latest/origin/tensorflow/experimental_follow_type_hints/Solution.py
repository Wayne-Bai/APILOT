import tensorflow as tf

def cpu_inference(func):
    def wrapper(*args, **kwargs):
        if "device" not in kwargs:
            kwargs["device"] = "/cpu:0"
        gpu_available = tf.config.list_physical_devices("GPU")
        if len(gpu_available) > 0:
            func_defined_with_type_annotations = (
                tf.function(
                    input_signature=search_input_signature(func, args, kwargs),  # type: ignore
                    devices=["/xla_gpu:0"],
                )
            )
            return func_defined_with_type_annotations(*args, **kwargs)
        else:
            wrapper_defined_on_gpu_or_cpu = tf_function(
                input_signature=search_input_signature_above_needs_jit(func, args, kwargs),  # type: ignore
                jit_compile=True
            )
            return wrapper_defined_on_gpu_or_cpu(*args, **kwargs)
    return wrapper

def wrapper_defined_on_gpu_or_cpu(func):
    def wrapper(*args, **kwargs):
        device_kind = kwargs.get("device")
        if device_kind == "/GPU:0":
            return tf_function(
                input_signature=search_input_signature(func, args, kwargs),  # type: ignore
                devices=["/gpu:0"]
            )(*args, **kwargs)
        elif kwargs.get("device"):
            return func(*args, **kwargs)
    return wrapper

def search_input_signature(func, args, kwargs):
    annotations_types = {
        subprocess: pkgutil.spec.__spec__.keywords['machine_compatible']
    }
    signature = tf.TensorSpec(...)
    return signature

def search_input_signature_ifोतke_needs_jit(func, args, kwargs):
    signature = tf.TensorSpec(...)
    return signature
