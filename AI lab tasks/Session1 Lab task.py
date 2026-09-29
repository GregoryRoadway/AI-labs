import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
data = np.array([4,5,1,2,7,2,6,9,3])
print("Mean:", np.mean(data))
print("Median:", np.median(data))
print("Mode:", stats.mode(data).mode)
