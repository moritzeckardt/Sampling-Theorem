import os
import numpy as np


def load_sample(filename, duration=4 * 44100, offset=44100 // 10):
    # Load file
    signal = np.load(filename)

    # Position of the highest absolute value of the signal
    peak_position = np.argmax(np.abs(signal))
    start = peak_position + offset
    end = start + duration
    return signal[start:end]


def compute_frequency(signal, min_freq=20):
    # Calculate fourier transform
    fourier_transform = np.fft.fft(signal)

    # Frequencies smaller than min_freq to 0
    fourier_transform[np.abs(fourier_transform) < min_freq] = 0

    # Find the highest peak
    max_magnitude_index = np.argmax(np.abs(fourier_transform))

    # Get the corresponding frequency from the index
    # fn(n) = f * (n * Ts) with max_magnitude_index / len(signal) representing Ts*n
    sample_rate = 44100
    return sample_rate * (max_magnitude_index / len(signal))


if __name__ == '__main__':
    expected_frequencies = [110, 220, 440, 880, 1760, 3520, None]
    audio_samples = os.listdir('introml_ex1\sounds')
    folder_path = 'introml_ex1\sounds'

    for file, expected_frequency in zip(audio_samples, expected_frequencies):
        sample = load_sample(os.path.join(folder_path, file))
        frequency = compute_frequency(sample)
        print(f'Audio Sample: {file}, Expected Frequency: {expected_frequency}Hz, Computed Frequency: {frequency}Hz')

# Link: https://en.wikipedia.org/wiki/Piano_key_frequencies
