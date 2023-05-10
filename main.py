from chirp import createChirpSignal
from decomposition import createTriangleSignal, createSquareSignal, createSawtoothSignal
from matplotlib import pyplot as plt

# TODO: Test the functions imported in lines 1 and 2 of this file.
# Create linear chirp signal
linear_chirp = createChirpSignal(200, 1, 1, 10, True)
plt.plot(linear_chirp)
plt.show()

# Create exponential chirp signal
exponential_chirp = createChirpSignal(200, 1, 1, 10, False)
plt.plot(exponential_chirp)
plt.show()
