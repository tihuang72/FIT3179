import pandas as pd
#Energy Generation - stream graph
data = pd.read_excel("Visualisation 2\DataProcessing\EnergyGen.xlsx",sheet_name = "Sheet1")
columns = data.columns
out = pd.melt(data,id_vars = ["Fuel Type","Type"],value_vars = columns[2:],var_name="Year",value_name="Energy(GWh)")
out.to_csv("Visualisation 2\data\EnergyGenProcc.csv",index=False)