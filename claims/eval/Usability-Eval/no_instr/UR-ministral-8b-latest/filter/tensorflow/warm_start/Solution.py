import tensorflow as tf
import threading

# Create a dataset
dataset = tf.data.Dataset.range(1000)

# Create a custom iterator
class CustomIterator:
    def __init__(self, dataset):
        self.dataset = dataset
        self.prefetched_elements = []

    def prefetch(self, num_ingoing=2, num_outgoing=64):
        # Prefetch elements
        iterations = self.dataset.prefetch(num_outgoing).repeat()
        for i in range(num_ingoing * num_outgoing):
            new_element = next(iterations)
            self.prefetched_elements.append(new_element)
        self._lock = threading.Lock()

    def __iter__(self):
        return self

    def __next__(self):
        while not self.prefetched_elements:
            with self._lock:
                self.prefetch()

        while len(self.prefetched_elements) > 0:
            element = self.prefetched_elements.pop(0)
            with self._lock:
                self.prefetch()

        raise StopIteration

# Wrap the Dataset with the CustomIterator
custom_iterator = CustomIterator(dataset)

# Iteration using the wrapped iterator
for element in custom_iterator:
    print(element)
