from matplotlib import pyplot as plt

from chirp import createChirpSignal
from decomposition import createTriangleSignal, createSquareSignal, createSawtoothSignal

# TODO: Test the functions imported in lines 1 and 2 of this file.
# TEST: Moritz
#import scipy
#import numpy as np
#import matplotlib.pyplot as plt

#a1D = np.arange(0, 1, 1/200)
#signal = scipy.signal.chirp(a1D, 1.0, 0.0, 1.0)
#plt.plot(signal)
#plt.show()

test = createChirpSignal(200, 1, 1, 10, True)
plt.plot(test)
plt.show()

test = createChirpSignal(200, 1, 1, 10, False)
plt.plot(test)
plt.show()
