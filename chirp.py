import numpy as np


# returns the chirp signal as list or 1D-array
def createChirpSignal(samplingrate: int, duration: int, freqfrom: int, freqto: int, linear: bool):
    # Create measurement time points over the entire duration
    t = np.linspace(0, duration, int(samplingrate * duration))

    # Determine phase/phase angle (describes the oscillation phase of the oscillation)
    if linear:
        # Calculate linear chirp rate and apply given formula
        c = (freqto - freqfrom) / duration
        phase = 2 * np.pi * (freqfrom + 0.5 * c * t) * t
    else:
        # Calculate exponential chirp rate and apply given formula
        k = np.log(freqto / freqfrom) / duration
        # phase = 2 * np.pi * freqfrom / np.log(k) * (k ** t - 1) # Does not work
        phase = 2 * np.pi * (freqfrom * duration / np.log(freqto / freqfrom) * (np.exp(k * t) - 1))

    # Return chirp signal
    return np.sin(phase)
