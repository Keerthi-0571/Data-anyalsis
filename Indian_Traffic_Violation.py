import pandas as pd

data = pd.read_csv(r"C:\Users\keert\Downloads\Indian_Traffic_Violations.csv")

print(data)
#%%
import pandas as pd

data = pd.read_csv(r"C:\Users\keert\Downloads\Indian_Traffic_Violations.csv")

print(data.head())
#%%
import pandas as pd

data = pd.read_csv(r"C:\Users\keert\Downloads\Indian_Traffic_Violations.csv")

print(data.tail())
#%%
import pandas as pd

data = pd.read_csv(r"C:\Users\keert\Downloads\Indian_Traffic_Violations.csv")

print(data.info())
#%%
import pandas as pd

data = pd.read_csv(r"C:\Users\keert\Downloads\Indian_Traffic_Violations.csv")

print(data.describe())
#%%
import pandas as pd

data = pd.read_csv(r"C:\Users\keert\Downloads\Indian_Traffic_Violations.csv")

df = data[['Violation_Type','Fine_Amount','Driver_Age','Penalty_Points']]

df.columns = ['Violation','Fine','Age','Points']

print(df)
#%%
import pandas as pd

data = pd.read_csv(r"C:\Users\keert\Downloads\Indian_Traffic_Violations.csv")

df = data[['Violation_Type','Fine_Amount','Driver_Age','Penalty_Points']]

df.columns = ['Violation','Fine','Age','Points']

today = df[df.Points >= 5]

print(today)
#%%
import pandas as pd

data = pd.read_csv(r"C:\Users\keert\Downloads\Indian_Traffic_Violations.csv")

df = data[['Violation_Type','Fine_Amount','Driver_Age','Penalty_Points']]

df.columns = ['Violation','Fine','Age','Points']

maxdt = df.sort_values(by='Fine', ascending=False)

print(maxdt)
#%%
import matplotlib.pyplot as plt
import seaborn as sns

tsd = df

plt.figure(figsize=(5,4))

sns.barplot(
    x='Violation',
    y='Fine',
    data=tsd,
    hue='Violation'
)

plt.xticks(rotation=90)
plt.title("Traffic Violation Fine Amount")
plt.xlabel("Violation Type")
plt.ylabel("Fine Amount")

plt.show()
