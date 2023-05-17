from chirp import createChirpSignal
from decomposition import createTriangleSignal, createSquareSignal, createSawtoothSignal
from matplotlib import pyplot as plt

# TODO: Test the functions imported in lines 1 and 2 of this file.
# Create linear chirp signal
linear_chirp = createChirpSignal(200, 1, 1, 10, True)
plt.plot(linear_chirp)
plt.show()

# Create exponential chirp signal
exponential_chirp = createChirpSignal(200, 1, 1, 20, False)
plt.plot(exponential_chirp)
plt.show()

# Create triangle signal
triangle_signal = createTriangleSignal(200, 2, 10000)
plt.plot(triangle_signal)
plt.show()

# Create square signal
square_signal = createSquareSignal(200, 2, 10000)
plt.plot(square_signal)
plt.show()

# Create sawtooth signal
sawtooth_signal = createSawtoothSignal(200, 2, 10000, amplitude=1)
plt.plot(sawtooth_signal)
plt.show()
