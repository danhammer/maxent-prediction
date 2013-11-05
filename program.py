import matplotlib.pyplot as plt
import itertools
import utils
from transfer import transferEntropy
from grab_data import *


training_start = 16000
training_end   = 18441

a, _ = utils.gen_preds(training_start, training_end, M = 1500)
W = utils.gen_preds(training_start, training_end, M = training_end - training_start - 1, pred=True) # change the m value
prediction_mat = a * W.T
prediction = list(itertools.chain(*prediction_mat.tolist()))

# y = utils.pru[training_start:training_end]
# plt.plot(y[0:1500])
# plt.plot(prediction)
# plt.show()


unemp = grab_series("UNRATE")
unemp = map(float, list(unemp['value']))[0:520]
fedfunds = grab_series("FEDFUNDS")
fedfunds = map(float, list(fedfunds['value']))[0:520]

