import numpy as np

def machine_limits(max_precision):
    # Machine-based limits for floating point types.
    machine_eps = np.finfo(float).eps
    max_exponent = np.finfo(float).max_exponent
    min_exponent = np.finfo(float).min_exponent

    return {"eps": machine_eps, "max_exponent": max_exponent, "min_exponent": min_exponent}

if __name__ == "__main__":
    print(machine_limits(max_precision=50))
