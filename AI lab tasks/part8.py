import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
hours_studied=[1,2,3,4,5,6,7]
exam_scores=[45,50,58,62,70,81,90]
print(np.corrcoef(hours_studied,exam_scores))

