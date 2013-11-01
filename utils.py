import numpy as np
import itertools
from operator import mul

DEPTH = 5
Tk = 25

pru = np.loadtxt('data/pru.dat', delimiter=',')

def gen_data(init_idx, end_idx, M = 1500, d = 3, k = 1, data = pru):
    # reshapes the time series data according to the specified lags.
    # The parameter `M` must be at least as long as the length of the
    # time series, bounded by `init_idx` and `end_idx`
    y = pru[init_idx:end_idx]
    v = np.zeros((d, M))
    for i in range(d):
        for j in range(M):
            v[i, j] = y[j + (d - 1) - (i - 1) * k - 2]
    return v

def gen_lags(j, v, depth = 4, d = 3):
    # Generate the convolutions based on lags, according to the depth
    # and lag-length for each time period indexed by `j`.
    def _decreasing(l):
        # returns true if supplied list is decreasing
        return list(l) == sorted(l, reverse=True)
        
    def _vgrab(idx_arr):
        # converts the supplied index arrays to the time series data
        return map(lambda i: v[i, j], idx_arr)

    fidx = filter(_decreasing, itertools.product(range(d), repeat = depth))
    l = [reduce(mul, x, 1) for x in map(_vgrab, fidx)]
    return l

def gen_row(j, v, d = 3):
    # Accepts an index and the sequence of measurements and generates
    # the row systems matrix
    ll = map(lambda x: gen_lags(j, v, depth = x, d = d), range(DEPTH + 1))
    return list(itertools.chain(*ll))

def gen_preds(init_idx, end_idx, M = 1500, d = 3, k = 1, data = pru, pred = False):
    # Returns the systems equation matrix and the resulting vector of
    # parameters for the supplied data, initial, and final indices.  
    y = data[init_idx:end_idx]
    v = gen_data(init_idx, end_idx, M = M)

    rows = map(lambda x: gen_row(x, v), range(M))
    W = np.matrix(rows)

    if pred:
        return W
    else:
        vT = [y[j + d + Tk - 2] for j in range(M)] 
        a = vT * np.linalg.pinv(W.T)
        return a, W

