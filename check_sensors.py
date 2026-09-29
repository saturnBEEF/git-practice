import json
from pathlib import Path

import pandas as pd
import yaml
##################################################
# Comments have been proofread and edited with AI
##################################################

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

# Filter sensors that are overdue for calibration
overdue_sensors = joined_sen_cal[
    joined_sen_cal["days_since_calibration"] > max_days
    ].to_dict(orient="records")

# Write the overdue sensors to a JSON file
with open(output_path, "w") as file:
    json.dump(overdue_sensors, file, indent=2)