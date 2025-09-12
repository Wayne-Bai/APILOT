import nltk
from nltk.corpus import wordnet as wn
from math import log

# Function to calculate the Information Content value for a synset

def InformationContent(synset):
  synset_scores = []
  for syn in wn.all_synsets():
    d = 0
    for inst in syn.instances():
      if inst.score() is not None:
        d += inst.score()
  if synset.instance_count() > 0:
    sc = -log(synset.instance_count() / d)
  else:
    sc = 0
  synset_scores.append(sc)
  return sum(synset_scores)
