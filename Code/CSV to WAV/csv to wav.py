import os
from statistics import mean
import pandas as pd
import matplotlib.pyplot as plt
import soundfile as sf

# assume we have columns 'time' and 'value'
df = pd.read_csv('R1-CD-1_TS-02092_2021-05-07-18-28-19_aligned.csv')

# compute sample rate, assuming times are in seconds
times = df['time_s'].values
n_measurements = len(times)
timespan_seconds = times[-1] - times[0]
sample_rate_hz = int(n_measurements / timespan_seconds)

# write data
data = df['ax_m/s/s'].values
sf.write('son_x.wav', data, sample_rate_hz)