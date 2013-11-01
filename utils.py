import numpy as np
import itertools
from operator import mul

DEPTH = 6
Tk = 25

pru = np.loadtxt('data/pru.dat', delimiter=',')

def gen_data(init_idx, end_idx, M = 1500, d = 3, k = 1, data = pru):
    y = pru[init_idx:end_idx]
    v = np.zeros((d, M))
    for i in range(d):
        for j in range(M):
            v[i, j] = y[j + (d - 1) - (i - 1) * k - 2]

    return v

def gen_lags(j, v, depth = 4, d = 3):
    
    def _decreasing(l):
        return list(l) == sorted(l, reverse=True)
        
    def _vgrab(idx_arr):
        return map(lambda i: v[i, j], idx_arr)

    idx_list = [i for i in itertools.product(range(d), repeat = depth)]
    fidx = filter(_decreasing, idx_list)

    l = [reduce(mul, x, 1) for x in map(_vgrab, fidx)]

    return l

def gen_row(j, v, d = 3):
    ll = map(lambda x: gen_lags(j, v, depth = x, d = d), range(DEPTH))
    return list(itertools.chain(*ll))

def gen_preds(init_idx, end_idx, M = 1500, d = 3, k = 1, data = pru):
    y = data[init_idx:end_idx]
    v = gen_data(init_idx, end_idx)
    vT = [y[j + d + Tk - 2] for j in range(M)] 
    rows = map(lambda x: gen_row(x, v), range(M))
    W = np.matrix(rows)
    wtp = np.linalg.pinv(W.T)
    a = vT * wtp
    return a, W
