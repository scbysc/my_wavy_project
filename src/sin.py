import numpy as np
import matplotlib.pyplot as plt

time = np.arange(0, 10, 0.1)
amplitude = np.sin(time)

plt.plot (time, amplitude)

plt.title('Sine curve')

plt.xlabel('Time')

plt.ylabel('Amplitude')

plt.show()