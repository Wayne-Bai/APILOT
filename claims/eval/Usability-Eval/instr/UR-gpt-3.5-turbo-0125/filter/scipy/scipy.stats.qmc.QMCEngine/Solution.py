
from scipy.stats import qmc

class GenericQMC(qmc.QMCEngine):
    def __init__(self, dimension, randomize=None):
        super(GenericQMC, self).__init__(dimension, randomize)
    
    def sample(self, n, pre=None):
        return self.randomize(self.gen_samples(n, pre=pre))
