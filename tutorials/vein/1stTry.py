# encoding=utf-8
from __future__ import print_function, division


"""
### Candidates
"""
from snorkel.models import candidate_subclass

Spouse = candidate_subclass("Spouse", ["person1", "person2"])



"""
### CandidateExtractor
"""
from snorkel.candidates import Ngrams, CandidateExtractor
from snorkel.matchers import PersonMatcher

