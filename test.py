import pandas as pd

df = pd.read_csv('mydata.csv')
df['Admitted_Date'] = pd.to_datetime(df['Admitted_Date'])
mask = df['Discharged_Date'].str.len() == 4
#print mask

df['Discharged_Date'] = pd.to_datetime(df['Discharged_Date'])
df.loc[mask, 'Discharged_Date' ] +=  pd.offsets.YearEnd()
print df
