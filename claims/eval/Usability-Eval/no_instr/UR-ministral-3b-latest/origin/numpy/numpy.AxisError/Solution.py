import numpy as np

def altitude_error_code(objective_axis):
    try:
        alt = np.arange(5, objective_axis[obj])
        return alt
    except ValueError:
        return 'ValueError raised when an Axis supplied was invalid.'
    except IndexError:
        return 'IndexError raised when an Axis supplied was invalid.'
    except np.AxisError:
        return 'AxisError raised when an Axis supplied was invalid.'

