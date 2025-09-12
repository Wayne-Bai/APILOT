from werkzeug import TestCase

class MyTestCase(TestCase):
    def make_line_iter(self, data, separator):
        for i in range(0, len(data), len(separator)):
            yield separator.join(data[i:i+len(separator)])
