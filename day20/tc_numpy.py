import numpy as np
import pandas as pd
arr=np.array([10,20,30,5,6])

print(arr)
print(np.sum(arr))
print(np.mean(arr))

data={
    "Name":["John","paul","Dexter"],
    "Age":[21,20,35],
    "City":["Mumbai","Bangalore","Pune"]
}
df=pd.DataFrame(data)
print(df)
