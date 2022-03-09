
import pandas as pd
import numpy as np

ser = pd.Series(['amrita', 'school', 'of', 'engineering', 'chennai', 'campus'])
newSeries = ser.map(lambda x: x[0].upper() + x[1:-1] + x[-1])

print(ser)
print(newSeries)

a = np.array(newSeries)
print(*a, sep= ' ')