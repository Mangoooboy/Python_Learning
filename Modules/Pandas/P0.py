import pandas as pd
data = {
    "Name":["Sam","John","Smith"],
    "Age":[20,30,40],
    "Marks":[50,50,50]
}
df = pd.DataFrame(data)
print(df)
print()
print(df[["Marks","Name"]])
print(df.shape)