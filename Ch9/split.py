# from page 169 ch9 
import tensorflow as tf 
from tensorflow import keras
import numpy as np
import matplotlib
from matplotlib import pyplot as plt



def plot_series(time, series, format= '-', start= 0, end=None):
    plt.plot(time[start:end], series[start:end], format)
    plt.xlabel("Time")
    plt.ylabel("Value")
    plt.grid(True)
    


def trend(time, slope=0):
    return slope * time 

def seasonal_pattern(season_time):
    """Just an arbitrary pattern, you can change it if you wish""" 
    return np.where(season_time < 0.4,
        np.cos(season_time * 2 * np.pi),
        1 / np.exp(3 * season_time))

def seasonality(time, period, amplitude=1, phase=0):
    """Repeats the same pattern at each period"""
    season_time = ((time + phase) % period) /period 
    return amplitude * seasonal_pattern(season_time)

def noise(time, noise_level=1, seed=None):
    rnd = np.random.RandomState(seed)
    return rnd.randn(len(time)) * noise_level

time = np.arange(4 * 365 + 1, dtype="float32")
baseline = 10 
series = trend(time, .05)
baseline = 10 
amplitude = 15 
slope = 0.09
noise_level = 6

# create the series 
series = baseline + trend(time, slope)
+ seasonality(time, period=365, amplitude=amplitude)

# update with noise 
series += noise(time, noise_level, seed=42)


split_time = 1000
time_train = time[:split_time]
x_train = time[split_time:]
time_valid = time[split_time:]
x_valid = series[split_time:]
plt.figsize=(10,6)
plot_series(time_valid, x_valid)
plt.show()




