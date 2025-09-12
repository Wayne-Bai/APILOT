from werkzeug.utils import cached_property

class StringField:
    def __init__(self, string, required_length):
        if not isinstance(string, str):
            raise ValueError("Input must be a string")
        self.string = string
        self.required_length = required_length

    @cached_property
    def length(self):
        return len(self.string)

    def compare(self, other):
        if not isinstance(other, str):
            return False

        if self.required_length is not None:
            if self.length!= self.required_length or other.length!= self.required_length:
                return False

        return self.string == other
