from scipy.stats import qmc

class QuasiMCSampler:
    def __init__(self):
        self.d = None

    def initialize(self, d):
        self.d = d

    def generate_sample(self, n):
        return qmc.halton(d=self.d, n=n).random()
