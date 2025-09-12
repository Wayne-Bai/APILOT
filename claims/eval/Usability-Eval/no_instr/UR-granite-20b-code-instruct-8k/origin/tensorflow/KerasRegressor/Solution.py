import tensorflow as tf

class SklearnClassifier(tf.estimator.Estimator):
    """TensorFlow Estimator implementation of the scikit-learn API."""

    def __init__(self, model_fn, model_dir=None, config=None, warm_start_from=None):
        """ constructing a TensorFlow Estimator."""
        def _model_fn(features, labels, mode, params):
            return model_fn(features, labels, mode)

        super(SklearnClassifier, self).__init__(
            model_fn=_model_fn,
            model_dir=model_dir,
            config=config)

    def fit(self, x=None, y=None, input_fn=None, steps=None, batch_size=None,
            max_steps=None, monitors=None, max_iter=None):
        """See `train`."""
        return self.train(
            input_fn=input_fn,
            steps=steps,
            max_steps=max_steps,
            monitors=monitors)

    def predict(self, x=None, input_fn=None, batch_size=None, outputs=None,
                keys=None):
        """See `predict`."""
        return self.predict_raw(
            input_fn=input_fn,
            outputs=outputs,
            as_iterable=True)

    def score(self, x=None, y=None, input_fn=None, batch_size=None, steps=None):
        """See `evaluate`."""
        return self.evaluate(
            input_fn=input_fn,
            steps=steps)
