import tensorflow as tf

class ExtensionTypeBase:
    def __init__(self):
        pass

    def create_extension_type(self, name, base_class):
        return tf.Module(name=name, base_class=base_class)

    def get_extension_type(self, name):
        try:
            return tf.load_variable(name, "extension_type")
        except tf.errors.NotFoundError:
            return None

    def set_extension_type(self, name, extension_type):
        tf.save_variable(name, "extension_type", extension_type)

    def delete_extension_type(self, name):
        tf.load_variable(name, "extension_type").remove()
        tf.save_variable(name, "extension_type", None)
