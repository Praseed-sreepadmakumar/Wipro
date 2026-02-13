import numpy as np
import pandas as pd

students = [
    {"name": "Alice", "score": 85},
    {"name": "Bob", "score": 92},
    {"name": "Charlie", "score": 78},
    {"name": "David", "score": 90},
    {"name": "Eva", "score": 88}
]

df=pd.DataFrame(students)
print(df)

score=np.array(df["score"])
print(score)
mean=np.mean(score)
median=np.median(score)
standard_deviation=np.std(score)
print("Mean:",mean)
print("Median:",median)
print("Standard Deviation:",standard_deviation)
df["above_average"] = df["score"] > mean
print(df)
