from sklearn.calibration import calibration_curve

def compute_calibration_curve(y_true, y_probs, n_bins=10, strategy='uniform'):
    """
    Compute the true probabilities and predicted probabilities for the calibration curve.

    Args:
    y_true : array-like, shape (n_samples,)
        True binary labels in range {0, 1} or {-1, 1} or {False, True}.
    y_probs : array-like, shape (n_samples,)
        The probabilities of the positive class.
    n_bins : int, default=10
        The number of bins to use for calibration.
    strategy : str, default='uniform'
        Strategy used to define the widths of the bins.
        Supported strategies are 'uniform' and 'quantile'.

    Returns:
    prob_true : array, shape (n_bins,)
        The true probability in each bin (fraction of positives).
    prob_pred : array, shape (n_bins,)
        The mean predicted probability in each bin.
    """
    return calibration_curve(y_true, y_probs, n_bins=n_bins, strategy=strategy)
