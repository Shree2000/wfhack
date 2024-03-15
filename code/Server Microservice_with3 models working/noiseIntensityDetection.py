import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
import noisereduce as nr

def findIntensity(path):

# Load the audio file
    print(path)
    rate, data = wavfile.read(path)

    # Perform noise reduction using noisereduce library
    reduced_noise = nr.reduce_noise(y=data, sr=rate)

    # Calculate the noise signal
    noise_signal = data - reduced_noise

    # Perform Fourier Transform on the original signal
    fft_data_original = np.fft.fft(data)

    # Perform Fourier Transform on the denoised signal
    fft_data_denoised = np.fft.fft(reduced_noise)

    # Perform Fourier Transform on the noise signal
    fft_data_noise = np.fft.fft(noise_signal)
    An=np.max(np.abs(noise_signal))
    Ao=np.max(np.abs(data))
    if(An>0.66*Ao):
        return "high"
    elif (An>0.4*An):
        return "medium"
    else:
        return "low"


