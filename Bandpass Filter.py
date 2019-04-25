import numpy as np
import pandas
from scipy import fftpack
from matplotlib import pyplot as plt

def lowpass_filter(trace,frequency_cutoff):
    fast_fourier_transform = fftpack.fft(trace)                                 # Take The Fourier Transform Of The Trace
    fast_fourier_transform[frequency_cutoff:len(fast_fourier_transform)] = 0    # Remove All Components Whos Frequency Is Greater Than The Cuttoff Frequency
    filtered_signal = fftpack.ifft(fast_fourier_transform)                      # Run The Inverse Fourier Transform To Get Back To A Signal
    real_filtered_signal = np.real(filtered_signal)
    return real_filtered_signal


def highpass_filter(trace,frequency_cutoff):
    fast_fourier_transform = fftpack.fft(trace)                                 # Take The Fourier Transform Of The Trace
    fast_fourier_transform[0:frequency_cutoff] = 0                              # Remove All Components Whos Frequency Is Less Than The Cuttoff Frequency
    filtered_signal = fftpack.ifft(fast_fourier_transform)                      # Run The Inverse Fourier Transform To Get Back To A Signal
    real_filtered_signal = np.real(filtered_signal)
    return real_filtered_signal


def bandpass_filter(trace,band_start,band_stop):
    fast_fourier_transform = fftpack.fft(trace)                                 # Take The Fourier Transform Of The Trace
    fast_fourier_transform[0:band_start] = 0                                    # Remove All Components Whos Frequency Is Less Than Band Start
    fast_fourier_transform[band_stop:len(fast_fourier_transform)] = 0           # Remove All Components Whos Frequency Is Greater Than Band Stop
    filtered_signal = fftpack.ifft(fast_fourier_transform)                      # Run The Inverse Fourier Transform To Get Back To A Signal
    real_filtered_signal = np.real(filtered_signal)
    return real_filtered_signal



