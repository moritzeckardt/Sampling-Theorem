import numpy as np


def createTriangleSignal(samples: int, frequency: int, k_max: int):
    # Create time points and empty signal
    t = np.linspace(0, 1, samples)
    signal = np.zeros(samples)

    # Apply triangle signal formula
    for k in range(k_max):
        upper_form = np.sin(2 * np.pi * (2 * k + 1) * frequency * t)
        formula = (-1) ** k * upper_form / (2 * k + 1) ** 2
        signal += formula

    signal *= (8 / np.pi ** 2)

    # Return the signal as 1D-array (np.ndarray)
    return signal


def createSquareSignal(samples: int, frequency: int, k_max: int):
    # Create time points and empty signal
    t = np.linspace(0, 1, samples)
    signal = np.zeros(samples)

    # Apply square signal formula
    for k in range(1, k_max):
        formula = (np.sin(2 * np.pi * (2 * k - 1) * frequency * t)) / (2 * k - 1)
        signal += formula

    signal *= 4 / np.pi

    # Return the signal as 1D-array (np.ndarray)
    return signal


def createSawtoothSignal(samples: int, frequency: int, k_max: int, amplitude: int):
    # Create time points and empty signal
    t = np.linspace(0, 1, samples)
    signal = np.zeros(samples)

    # Apply sawtooth signal formula
    for k in range(1, k_max):
        formula = np.sin(2 * np.pi * k * frequency * t) / k
        signal += formula

    signal *= amplitude / np.pi
    sawtooth = amplitude / 2 - signal

    # Return the signal as 1D-array (np.ndarray)
    return sawtooth
