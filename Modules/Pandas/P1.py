import pandas as pd

data = {
    "Name":["Sam","John","Alex"],
    "Age":[23,25,24],
    "Salary":[50000,60000,55000]
}

df = pd.DataFrame(data)

print(df.iloc[0:1])
print()
print(df[df["Age"]>23])
print(df[
          (df["Age"]==23)
    &
          (df["Salary"]>50000)
      ])

print()
print(df["Salary"].mean())
print(df["Salary"].max())
print(df["Salary"].min())
print(df["Salary"].sum())
print()
print(df.describe())
df["Bonus"] = [5000,7000,6000]
print(df)
print()

df["Age+Salary"]= df["Age"]+df["Salary"]
print(df)