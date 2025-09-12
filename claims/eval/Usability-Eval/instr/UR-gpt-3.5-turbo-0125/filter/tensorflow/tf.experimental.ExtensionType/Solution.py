
import tensorflow as tf

class ExtensionType:
    def __init__(self, name):
        self.name = name

# Additional custom ExtensionType classes can be derived from the base class 'ExtensionType'
class CustomExtensionType1(ExtensionType):
    def __init__(self, name):
        super().__init__(name)

class CustomExtensionType2(ExtensionType):
    def __init__(self, name):
        super().__init__(name)

# Usage example:
extension_instance1 = CustomExtensionType1("Extension1")
print(extension_instance1.name)

extension_instance2 = CustomExtensionType2("Extension2")
print(extension_instance2.name)
