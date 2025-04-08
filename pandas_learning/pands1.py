import numpy as np
import pandas as pd

import warnings
# print(warnings.filterwarnings("ignore"))

df =pd.read_csv(r"C:\Users\user\OneDrive\Desktop\template.csv")


pd.set_option("display.max_rows",10)
print(df)
print(df.head(10))
print(df.shape)
print(df.info())
for x in df.columns.tolist():
    print(x)