import pandas as pd

data = pd.read_csv(r"C:\Users\keert\Downloads\india_cancer_patients_2022_2025.csv")

print(data)
#%%
import pandas as pd

data = pd.read_csv(r"C:\Users\keert\Downloads\india_cancer_patients_2022_2025.csv")

print(data.head())
#%%
import pandas as pd

data = pd.read_csv(r"C:\Users\keert\Downloads\india_cancer_patients_2022_2025.csv")

print(data.tail())
#%%
import pandas as pd

data = pd.read_csv(r"C:\Users\keert\Downloads\india_cancer_patients_2022_2025.csv")

print(data.info())
#%%
import pandas as pd

data = pd.read_csv(r"C:\Users\keert\Downloads\india_cancer_patients_2022_2025.csv")

print(data.describe())
#%%
import pandas as pd

data = pd.read_csv(r"C:\Users\keert\Downloads\india_cancer_patients_2022_2025.csv")

df = data[['Patient_ID','Age','Cancer_Type','Survival_Months']]

df.columns = ['Patient','Age','Cancer','Survival']

print(df)
#%%
import pandas as pd

data = pd.read_csv(r"C:\Users\keert\Downloads\india_cancer_patients_2022_2025.csv")

df = data[['Patient_ID','Age','Cancer_Type','Survival_Months']]

df.columns = ['Patient','Age','Cancer','Survival']

today = df[df.Survival >= 24]

print(today)
#%%
import pandas as pd

data = pd.read_csv(r"C:\Users\keert\Downloads\india_cancer_patients_2022_2025.csv")

df = data[['Patient_ID','Age','Cancer_Type','Survival_Months']]

df.columns = ['Patient','Age','Cancer','Survival']

maxdt = df.sort_values(by='Survival', ascending=False)

print(maxdt)
#%%
import matplotlib.pyplot as plt
import seaborn as sns

tsd = df

plt.figure(figsize=(4,4))

sns.barplot(
    x='Cancer',
    y='Survival',
    data=tsd,
    hue='Cancer'
)

plt.xticks(rotation=90)
plt.title("Cancer Type vs Survival Months")
plt.xlabel("Cancer Type")
plt.ylabel("Survival Months")

plt.show()
