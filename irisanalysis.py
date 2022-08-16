import numpy as np
import pandas as pd
df=pd.read_csv('iris.csv',header=0)
print(df[["sepal.length","variety"]])