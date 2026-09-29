import yaml
import pandas as pd

with open("git-practice/data/config.yml") as file:
    config = yaml.safe_load(file)
    print(config)

sensors = pd.read_excel("git-practice/data/sensors.xlsx")
calibrations = pd.read_csv("git-practice/data/calibrations.csv")

joined_sen_cal = pd.merge(sensors, calibrations, on="sensor_id").to_dict(orient="records")
print(joined_sen_cal)