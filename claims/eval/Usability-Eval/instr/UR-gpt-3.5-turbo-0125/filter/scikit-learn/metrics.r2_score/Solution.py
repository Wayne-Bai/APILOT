
import numpy as np

def r2_score(y_true, y_pred):
    y_true = np.array(y_true)
    y_pred = np.array(y_pred)
    y_avg = np.mean(y_true)
    
    ss_res = np.sum((y_true - y_pred) ** 2)
    ss_tot = np.sum((y_true - y_avg) ** 2)
    
    r2 = 1 - (ss_res / ss_tot)
    
    return r2

# Example usage
y_true = [3, -0.5, 2, 7]
y_pred = [2.5, 0.0, 2, 8]
print("R2 score:", r2_score(y_true, y_pred))
