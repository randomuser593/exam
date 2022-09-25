import pandas as pd

a = [10,20,30,40,50,60,70,80,90,100]

print("Min: ", pd.Series(a).idxmin())
print("Max: ", pd.Series(a).idxmax())

