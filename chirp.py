import numpy as np

# returns the chirp signal as list or 1D-array
def createChirpSignal(samplingrate: int, duration: int, freqfrom: int, freqto: int, linear: bool):
    # Create
    time = np.linspace(0, duration, int(samplingrate * duration))
    print(time)

createChirpSignal(10, 20, 2, 2, True)