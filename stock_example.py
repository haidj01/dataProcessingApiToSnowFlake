import os
from restApi import api_request
import pandas as pd
import json

api_key = os.getenv('MARKET_STACK_KEY')
if api_key:
    params ={
        "access_key": api_key,
        "symbols": "AAPL",
    }
    url = "https://api.marketstack.com/v1/eod"
    response = api_request(url, params)
    df = pd.DataFrame(response['data'])
    df["date"] = pd.to_datetime(df["date"])
    print(df.head())
else:
    print("No API key provided")