import pandas as pd
#Energy Generation - stream graph
data = pd.read_csv("Visualisation 2\DataProcessing\Emissions.csv")
columns = data.columns
out = pd.melt(data,id_vars = ["Quarter"],value_vars = columns[1:],var_name="GHG",value_name="Value")
out.to_csv("Visualisation 2\data\Emissions2.csv",index=False)