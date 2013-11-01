import matplotlib.pyplot as plt
import itertools
import utils

training_start = 16000
training_end   = 18441

a, _ = utils.gen_preds(training_start, training_end, M = 1500)
W = utils.gen_preds(training_start, training_end, M = training_end - training_start - 1, pred=True) # change the m value
prediction_mat = a * W.T
prediction = list(itertools.chain(*prediction_mat.tolist()))

y = utils.pru[training_start:training_end]
plt.plot(y)
plt.plot(prediction)
plt.show()


