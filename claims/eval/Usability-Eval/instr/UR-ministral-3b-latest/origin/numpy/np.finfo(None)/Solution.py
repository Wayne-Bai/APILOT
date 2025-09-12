import numpy as np

# Machine limits for floating point types
limits = {}

e = np.real(2/5)
two_e = 2 * e
ten_e = 10 ** e

limits['min'] = np.finfo(e.dtype).min
limits['min_2'] = limits['min'] * 1e34  # minimum value for e*2

limits['max'] = np.finfo(e.dtype).max
limits['max_2'] = limits['max'] * 1e34  # maximum value for e*2

limits['epsilon'] = np.finfo(e.dtype).eps

limits['machine_precision'] = np.nextafter(1e-34, 1e-34)  # machine precision

print(limits)
