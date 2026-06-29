# %%
import pandas as pd
data=pd.read_csv("E:\\covid_19_india.csv")
print(data)
# %%
import pandas as pd
data=pd.read_csv("E:\\covid_19_india.csv")
print(data.head())#head is the function which display top 5 data from the dataset
# %%
import pandas as pd
data=pd.read_csv("E:\\covid_19_india.csv")
print(data.tail())#head is the function which display top 5 data from the dataset
# %%
import pandas as pd
data=pd.read_csv("E:\\covid_19_india.csv")
df=data[['Date', 'Time', 'State/UnionTerritory', 'ConfirmedIndianNational']]
df.columns=['Dt','Tt','St','Cfmd']

# %%
import pandas as pd
data=pd.read_csv("E:\\covid_19_india.csv")
x = data.head()
y = data.tail()
print(x)
print(y)
# %%
import pandas as pd
data=pd.read_csv("E:\\covid_19_india.csv")
df=data[['Date', 'Time', 'State/UnionTerritory', 'ConfirmedIndianNational']]
df.columns=['Dt','Tt','St','Cfmd']
today = df.sort_values(by='St')
print(today)
# %%
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
data = pd.read_csv("E:\\covid_19_india.csv")
sns.barplot(x='State', y='Death', data=data)
plt.show()
# %%
pip install seaborn
# %%
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load data
data = pd.read_csv("E:\\covid_19_india.csv")

# Check column names
print(data.columns)

# Ensure numeric values
data['Death'] = pd.to_numeric(data['Death'], errors='coerce')

# Plot top 10 states by deaths
top_states = data.groupby('State')['Death'].sum().nlargest(10).reset_index()
sns.barplot(x='State', y='Death', data=top_states)
plt.xticks(rotation=45)
plt.show()

# %%
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load Dataset
data = pd.read_csv("C:\\Users\\keert\\Downloads\\archive\\India_lpg_dataset.csv")

# First 5 rows
print(data.head())

# Last 5 rows
print(data.tail())

# Dataset Summary
print(data.describe())

# Select required columns
df = data[['State','LPG_Connections','Refills','Complaints']]

# Rename columns
df.columns=['State','Connections','Refills','Complaints']

print(df.head())

# Sort by Complaints
today = df.sort_values(by='Complaints')
print(today)

# Highest Complaints
maxData = df.sort_values(by='Complaints', ascending=False)
print(maxData)

# Graph
plt.figure(figsize=(10,5))
sns.barplot(x='Complaints', y='State', data=maxData)
plt.title("LPG Crisis Complaints")
plt.show()
# %%
import pandas as pd

data = pd.read_csv("D:\\NetCraftz\\India_lpg_dataset.csv")
print(data)
import pandas as pd

data = pd.read_csv("D:\\NetCraftz\\India_lpg_dataset.csv")

print(data.head())  # head() displays the first 5 rows of the dataset
import pandas as pd

data = pd.read_csv(r"D:\NetCraftz\India_lpg_dataset.csv")

print(data.tail())  # tail() displays the last 5 rows of the dataset
import pandas as pd

data = pd.read_csv(r"D:\NetCraftz\India_lpg_dataset.csv")

print(data.info())
import pandas as pd

data = pd.read_csv(r"D:\NetCraftz\India_lpg_dataset.csv")

print(data.describe())
import pandas as pd

data = pd.read_csv(r"D:\NetCraftz\India_lpg_dataset.csv")

df = data[['Year', 'Production_MMT', 'Consumption_MMT', 'Price_INR']]
df.columns = ['Yr', 'Prod', 'Cons', 'Price']

import pandas as pd

data = pd.read_csv(r"D:\NetCraftz\India_lpg_dataset.csv")

df = data[['Year', 'Production_MMT', 'Consumption_MMT', 'Price_INR']]
df.columns = ['Yr', 'Prod', 'Cons', 'Price']
today = df[df.Yr == 2024]
print(today)
import pandas as pd

data = pd.read_csv(r"D:\NetCraftz\India_lpg_dataset.csv")

df = data[['Year', 'Production_MMT', 'Consumption_MMT', 'Price_INR']]
df.columns = ['Yr', 'Prod', 'Cons', 'Price']
maxdt = df.sort_values(by='Price', ascending=False)
print(maxdt)
import seaborn as sns

tsd = df
sns.barplot(x='Yr', y='Price', data=tsd, hue='Yr')
plt.show()
# %%
import pandas as pd

data = pd.read_csv("C:\\Users\\keert\\Downloads\\archive\\India_lpg_dataset.csv")

print(data.head())
# %%
import pandas as pd

data = pd.read_csv("C:\\Users\\keert\\Downloads\\archive\\India_lpg_dataset.csv")
print(data)
# %%
import pandas as pd

data = pd.read_csv(r"C:\\Users\\keert\\Downloads\\archive\\India_lpg_dataset.csv")

print(data.tail())
# %%
import pandas as pd

data = pd.read_csv(r"C:\\Users\\keert\\Downloads\\archive\\India_lpg_dataset.csv")

print(data.info())
# %%
import pandas as pd

data = pd.read_csv(r"C:\\Users\\keert\\Downloads\\archive\\India_lpg_dataset.csv")

print(data.describe())
# %%
import pandas as pd

data = pd.read_csv(r"C:\\Users\\keert\\Downloads\\archive\\India_lpg_dataset.csv")

df = data[['Year', 'Production_MMT', 'Consumption_MMT', 'Price_INR']]
df.columns = ['Yr', 'Prod', 'Cons', 'Price']
# %%
import pandas as pd

data = pd.read_csv(r"C:\\Users\\keert\\Downloads\\archive\\India_lpg_dataset.csv")

df = data[['Year', 'Production_MMT', 'Consumption_MMT', 'Price_INR']]
df.columns = ['Yr', 'Prod', 'Cons', 'Price']
today = df[df.Yr == 2024]
print(today)
# %%
import pandas as pd

data = pd.read_csv(r"C:\\Users\\keert\\Downloads\\archive\\India_lpg_dataset.csv")

df = data[['Year', 'Production_MMT', 'Consumption_MMT', 'Price_INR']]
df.columns = ['Yr', 'Prod', 'Cons', 'Price']
maxdt = df.sort_values(by='Price', ascending=False)
print(maxdt)
# %%
import seaborn as sns

tsd = df
sns.barplot(x='Yr', y='Price', data=tsd, hue='Yr')
plt.show()
