import pandas as pd
from pathlib import Path
import yaml
import json

# Load configuration from YAML file
# Create a Path object for the config file
with open("data/config.yml") as file:
    config = yaml.safe_load(file)
    max_days = config["max_days_since_calibration"]
    output_file = config["output_file"]
    output_path = Path(__file__).parent / output_file

# Read sensor and calibration data
sensors = pd.read_excel("data/sensors.xlsx")
calibrations = pd.read_csv("data/calibrations.csv")

# Merge the two DataFrames on the sensor_id column
joined_sen_cal = pd.merge(sensors, calibrations, on="sensor_id")
print(joined_sen_cal)

# Filter sensors that are overdue for calibration and write it to a JSON file
overdue_sensors = joined_sen_cal[joined_sen_cal["days_since_calibration"] > max_days]
with open(output_path, "w") as file:
    json.dump(overdue_sensors.to_dict(orient="records"), file, indent=2)