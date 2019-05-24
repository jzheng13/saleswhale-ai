import sys

import reviews

if __name__ == '__main__':

    if len(sys.argv) > 1:
        tgt_asin = sys.argv[1]
    else:
        tgt_asin = review.random_asin()

    print("Product ASIN: {}".format(tgt_asin))

    neg_reason = reviews.negative_reason(tgt_asin)
    reason = neg_reason['reason']
    freq = neg_reason['frequency']

    print(neg_reason)

    print(reviews.explain(tgt_asin, neg_reason))
