import openai
from functools import lru_cache
import pandas as pd
from dotenv import load_dotenv
import os

# Specify the path to your .env file
dotenv_path = '.env'

# Load variables from the custom .env file
load_dotenv(dotenv_path)


@lru_cache()
def get_settings(setting):
    return os.getenv(setting)  # config = {"USER": "foo", "EMAIL": "foo@example.org"}


def resample_timeseries(data):
    frame = pd.DataFrame(data)
    frame.index = pd.to_datetime(frame.index)
    # get the number of days in the timeseries
    diff = frame.index.max() - frame.index.min()
    if 0 < diff.days <= 31:
        # resample to week
        resampled_data = frame.resample('W').mean()
    elif 31 < diff.days <= 365:
        # resample to quarter start
        resampled_data = frame.resample('QS').mean()
    else:
        # resample to year start
        resampled_data = frame.resample('BAS').mean()
    return resampled_data
