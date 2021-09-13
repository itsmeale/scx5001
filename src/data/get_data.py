import pandas as pd

from sspdata.datasets.feminicidio import extrair_feminicidios


years = list(range(2015, 2022))
months = list(range(1, 13))

dataframes = list()

for year in years:
    for month in months:
        try:
            dataframes.append(extrair_feminicidios(year, month))
        except Exception as e:
            print(f"Could not extract data for y: {year}, m: {month}")
        print(f"{year}, {month} finished")


unified_dataframe = pd.concat(dataframes)
unified_dataframe.to_csv("data/raw/feminicide_ssp.csv")