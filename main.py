from chirp import createChirpSignal
from decomposition import createTriangleSignal, createSquareSignal, createSawtoothSignal

# TODO: Test the functions imported in lines 1 and 2 of this file.
import scipy
import numpy as np
import matplotlib.pyplot as plt

a1D = np.arange(0, 10, 0.5)
signal = scipy.signal.chirp(a1D, 2.0, 0.1, 4.0)
plt.plot(signal)
plt.show()
