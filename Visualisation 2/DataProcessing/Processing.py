import pandas as pd
data = pd.read_excel("EnergyGen.xlsx",sheet_name = "Sheet1")
columns = data.columns
out = pd.melt(data,id_vars = ["Fuel Type","Type"],value_vars = columns[2:],var_name="Year",value_name="Energy(GWh)")
out.to_csv("EnergyGenProcc.csv",index=False)