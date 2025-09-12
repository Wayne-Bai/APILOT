import tensorflow as tf

class LearningRateSchedule:
    def __init__(self, initial_learning_rate):
        self.initial_learning_rate = initial_learning_rate

    def __call__(self, step):
        raise NotImplementedError("Must be implemented by the subclass.")

class ConstantLearningRateSchedule(LearningRateSchedule):
    def __call__(self, step):
        return self.initial_learning_rate

class ExponentialLearningRateSchedule(LearningRateSchedule):
    def __init__(self, initial_learning_rate, decay_rate, decay_steps):
        super(ExponentialLearningRateSchedule, self).__init__(initial_learning_rate)
        self.decay_rate = decay_rate
        self.decay_steps = decay_steps

    def __call__(self, step):
        return self.initial_learning_rate * (self.decay_rate ** (step / self.decay_steps))

class PiecewiseConstantLearningRateSchedule(LearningRateSchedule):
    def __init__(self, initial_learning_rate, boundaries, values):
        super(PiecewiseConstantLearningRateSchedule, self).__init__(initial_learning_rate)
        self.boundaries = boundaries
        self.values = values

    def __call__(self, step):
        for i in range(len(self.boundaries)):
            if step < self.boundaries[i]:
                return self.values[i]
        return self.values[-1]

# Example usage:
if __name__ == "__main__":
    schedule = ConstantLearningRateSchedule(0.1)
    print(schedule(10))  # prints: 0.1

    schedule = ExponentialLearningRateSchedule(0.1, 0.9, 100)
    print(schedule(10))  # prints: 0.1 * (0.9 ** (10 / 100))

    schedule = PiecewiseConstantLearningRateSchedule(0.1, [100, 200], [0.1, 0.01, 0.001])
    print(schedule(10))  # prints: 0.1
    print(schedule(150))  # prints: 0.01
    print(schedule(250))  # prints: 0.001
