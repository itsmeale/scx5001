import pandas as pd

from sspdata.datasets.feminicidio import extrair_feminicidios

YEARS = list(range(2015, 2022))
MONTHS = list(range(1, 13))

dataframes = list()


def extract_feminicide_data():
    for year in YEARS:
        for month in MONTHS:
            try:
                dataframes.append(extrair_feminicidios(year, month))
            except Exception:
                print(f"Could not extract data for y: {year}, m: {month}")
            print(f"{year}, {month} finished")

    unified_dataframe = pd.concat(dataframes)
    unified_dataframe.to_csv("data/raw/feminicide_ssp.csv")


if __name__ == '__main__':
    extract_feminicide_data()
