import scipy as sp

class QMC_Sampler(sp.stats.rv_continuous):
    """
    A generic Quasi-Monte Carlo sampler class meant for subclassing.
    """
    def __init__(self, dist, seed=None):
        super().__init__(seed=seed)
        self.dist = dist
        self.qmc_engine = None

    def _rvs(self, n):
        if self.qmc_engine is None:
            raise ValueError("QMC engine not initialized.")
        samples = self.qmc_engine.generate(n)
        return samples
