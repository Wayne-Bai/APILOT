from sklearn.model_selection import cross_val_score

scorers = cross_val_score(estimator=None, cv='auto', scoring=None, n_jobs=-1, return_train_score=False,)
print(scorers)
