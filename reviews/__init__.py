import pickle
import random

from matplotlib import pyplot as plt

with open('./reviews/saved_topics.pkl', 'rb') as in_pkl:
    SAVED_TOPICS = pickle.load(in_pkl)

def random_asin():
    return random.choice(list(SAVED_TOPICS.keys()))

def negative_reason(tgt_asin):
    no_reason = {'reason': None, 'frequency': 0}
    if tgt_asin in SAVED_TOPICS:
        reasons = SAVED_TOPICS[tgt_asin]
        if len(reasons) > 0:
            sort_reasons = sorted(reasons, 
                key=lambda x: x['frequency'], reverse=True)
            return {k: v for k, v in sort_reasons[0].items() if k != 'reviews'}
    return no_reason

def explain(tgt_asin, reason):
    if reason is None:
        return "no negative review"
    else:
        # visualisation?
        reasons = SAVED_TOPICS[tgt_asin]
        for r in reasons:
            if r['reason'] == reason:
                return r['reviews']
        return "reason not found"