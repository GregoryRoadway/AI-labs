import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
x=np.random.normal(50,10,10000)
plt.hist(x,bins=50)
plt.show()

