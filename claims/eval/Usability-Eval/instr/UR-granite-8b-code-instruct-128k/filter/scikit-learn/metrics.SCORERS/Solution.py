
from sklearn import metrics

scorers = metrics.SCORERS.keys()
for scorer in scorers:
    print(scorer)
