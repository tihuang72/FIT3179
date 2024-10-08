import pandas as pd
#Energy Generation - stream graph
data = pd.read_csv("Visualisation 2\DataProcessing\LGA2016zones.csv")
columns = data.columns
out = pd.melt(data,id_vars = ["LGA_CODE_2016","LGA_NAME_2016"],value_vars = columns[2:],var_name="EnergyType",value_name="Capacity")
out.to_csv("Visualisation 2\data\SolarLGA2016.csv",index=False)