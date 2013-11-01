import matplotlib.pyplot as plt
import itertools
import utils

training_start = 16000
training_end   = 18441

a, _ = utils.gen_preds(training_start, training_end, M = 1500)
_ , W = utils.gen_preds(training_start, training_end, M = 1500) # change the m value
prediction_mat = a * W.T
prediction = list(itertools.chain(*prediction_mat.tolist()))

# y = pru[training_start:training_end]
# plt.plot(y[0:1500])
# plt.plot(prediction[0:1500])
# plt.show()


