import pandas as pd
import yaml

with open("data/config.yml") as file:
    config = yaml.safe_load(file)
    print(config)

sensors = pd.read_excel("data/sensors.xlsx")
calibrations = pd.read_csv("data/calibrations.csv")

joined_sen_cal = pd.merge(sensors, calibrations, on="sensor_id").to_dict(orient="records")
print(joined_sen_cal)
