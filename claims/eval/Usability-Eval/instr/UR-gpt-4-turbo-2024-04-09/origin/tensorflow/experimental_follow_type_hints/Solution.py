import tensorflow as tf

def optimize_with_annotations(func):
    def wrapper(*args, **kwargs):
        new_args = []
        annotations = func.__annotations__.get('args', {})
        for arg, value in zip(args, annotations.values()):
            if value is tf.Tensor:
                arg = tf.convert_to_tensor(arg)
            new_args.append(arg)
        return func(*new_args, **kwargs)
    return wrapper

@optimize_with_annotations
def process_tensors(x: tf.Tensor, y: tf.Tensor) -> tf.Tensor:
    return x + y

# Example usage
a = [1, 2, 3]
b = [4, 5, 6]
result = process_tensors(a, b)
print(result)  # Output Tensor after addition
