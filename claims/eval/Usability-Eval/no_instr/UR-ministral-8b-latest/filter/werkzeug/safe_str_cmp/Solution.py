from werkzeug.utils import cached_property

class StringComparator:
    def __init__(self, string_to_compare):
        self.string_to_compare = string_to_compare

    @cached_property
    def length(self):
        return len(self.string_to_compare)

    def is_subsequence(self, other_string):
        length_comparison = self.length
        len_other = len(other_string)

        if length_comparison > len_other:
            return False

        j = 0  # index for other_string
        for i in range(length_comparison):
            if self.string_to_compare[i] == other_string[j]:
                j += 1
            if j == len_other:
                return True

        return False

# Example usage:
comparator = StringComparator("example")
print(comparator.is_subsequence("semplate"))  # Output: True
print(comparator.is_subsequence("amle"))      # Output: False
