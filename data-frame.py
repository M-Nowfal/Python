import pandas as pd
import numpy as np

emplyee_data = {
  "emp_id": [1, 2, 3, 4],
  "name": ["Nowfal", "Yogaarasu", "SivaMuthu", "Saravanan"],
  "salary": [35000, 40000, np.nan, 32000],
  "designation": ["Developer", "Technisioan", "Learner", "Manager"],
}
df = pd.DataFrame(emplyee_data)

df["salary"] = df["salary"].fillna(df["salary"].mean())

print(df['name'])