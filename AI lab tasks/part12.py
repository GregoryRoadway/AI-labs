import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
TP,TN,FP,FN=80,170,20,30
accuracy=(TP+TN)/(TP+TN+FP+FN)
print(accuracy)

