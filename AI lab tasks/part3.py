import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
data = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
print("Mean:", np.mean(data))
print("Median:", np.median(data))
print("Mode:", stats.mode(data).mode)
